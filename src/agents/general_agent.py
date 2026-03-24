from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from config.settings import DASHSCOPE_API_KEY
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from src.tools import discover_tools
from src.core.prompts import get_system_prompt
from src.core.memory.manager import MemoryManager

load_dotenv()

# 初始化千问模型（使用 ChatTongyi，支持工具绑定）
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",
    temperature=0.7,
    max_tokens=1500
)

# 获取通用 Agent 的系统提示词
system_prompt = get_system_prompt("general")

# ========== 工具加载策略 ==========
# 
# 策略 1: 使用基础工具列表（稳定，推荐生产环境）
# tools = get_all_tools()
#
# 策略 2: 自动发现所有工具（开发/测试环境）
# tools = discover_tools(auto_discover=True, verbose=False)
#
# 策略 3: 智能模式 - 排除示例和测试工具
# tools = discover_tools(
#     auto_discover=True,
#     verbose=True,  # 显示加载日志
#     exclude_patterns=['demo_*']  # 排除特定文件
# )
#
# ===================================

# 当前使用策略：智能模式（排除 example_* 和 test_* 文件）
tools = discover_tools(
    auto_discover=True,
    verbose=False,  # 生产环境设为 False
    exclude_patterns=None  # 使用默认排除规则
)

# 使用 LangGraph 创建 ReAct Agent（支持多参数工具）
general_agent_executor = create_react_agent(llm, tools)

# 初始化记忆管理器
agent_memory = MemoryManager(user_id="default_user")


def run_general_agent(query: str, verbose: bool = True):
    """
    运行通用 Agent
    
    参数:
        query: 用户问题
        verbose: 是否打印思考过程，默认 True
    
    返回:
        Agent 的回答
    """
    # 使用记忆管理器构建优化的上下文
    messages = agent_memory.get_context(query, system_prompt)
    messages.append(HumanMessage(content=query))
    
    response = general_agent_executor.invoke({"messages": messages})
    
    # 打印思考链路过程
    print_thought_process(response, verbose)
    
    if "messages" in response and len(response["messages"]) > 0:
        ai_response = response["messages"][-1].content
        # 保存交互到记忆
        agent_memory.add_interaction(query, ai_response)
        return ai_response
    return "抱歉，我无法回答这个问题。"


def print_thought_process(response: dict, verbose: bool = True):
    """
    打印 Agent 的思考链路过程

    Args:
        response: Agent 的响应字典
        verbose: 是否打印详细日志
    """
    if not verbose or "messages" not in response:
        return

    print("\n" + "=" * 70)
    print("🧠 通用 Agent 思考链路")
    print("=" * 70)

    tool_usage_summary = []  # 记录工具使用情况

    for i, msg in enumerate(response["messages"]):
        msg_type = type(msg).__name__

        # 跳过系统提示词
        if msg_type == "SystemMessage":
            continue

        # 用户输入
        if msg_type == "HumanMessage":
            print(f"\n👤 用户问题:")
            preview = msg.content[:100] + "..." if len(msg.content) > 100 else msg.content
            print(f"   {preview}")

        # AI 思考（包含工具调用）
        elif msg_type == "AIMessage":
            # 检查是否有工具调用
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                for tool_call in msg.tool_calls:
                    tool_name = tool_call.get('name', 'unknown')
                    tool_args = tool_call.get('args', {})

                    print(f"\n💭 思考决策:")
                    print(f"   🔹 使用方法：{tool_name}")
                    print(f"   🔹 调用参数：{tool_args}")

                    # 记录工具使用
                    tool_usage_summary.append({
                        'method': tool_name,
                        'args': tool_args
                    })

            # 显示 AI 的思考内容（如果有）
            if msg.content and not (hasattr(msg, 'tool_calls') and msg.tool_calls):
                content = msg.content.strip()
                if content:
                    print(f"\n💭 思考内容:")
                    lines = content.split('\n')
                    for line in lines[:5]:
                        if line.strip():
                            print(f"   {line}")
                    if len(lines) > 5:
                        print(f"   ... (还有 {len(lines) - 5} 行)")

        # 工具执行结果
        elif msg_type == "ToolMessage":
            print(f"\n✅ 方法执行结果:")
            content = msg.content.strip()
            if len(content) > 200:
                print(f"   {content[:200]}...")
                print(f"   (结果长度：{len(content)} 字符)")
            else:
                print(f"   {content}")

    # 打印方法使用总结
    if tool_usage_summary:
        print("\n" + "-" * 70)
        print("📊 方法调用统计:")
        method_count = {}
        for usage in tool_usage_summary:
            method = usage['method']
            method_count[method] = method_count.get(method, 0) + 1

        for method, count in method_count.items():
            print(f"   • {method}: {count} 次")

    print("\n" + "=" * 70)
