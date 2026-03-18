from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from config.settings import DASHSCOPE_API_KEY
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from src.tools import discover_tools
from src.core.prompts import get_system_prompt

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


def run_general_agent(query: str, verbose: bool = True):
    """
    运行通用 Agent
    
    参数:
        query: 用户问题
        verbose: 是否打印思考过程，默认 True
    
    返回:
        Agent 的回答
    """
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]
    response = general_agent_executor.invoke({"messages": messages})
    
    # 打印思考链路过程
    if verbose and "messages" in response:
        print("\n" + "─" * 70)
        print("🧠 通用 Agent 思考过程:")
        print("─" * 70)
        
        for i, msg in enumerate(response["messages"]):
            msg_type = type(msg).__name__
            
            # 跳过系统提示词
            if msg_type == "SystemMessage":
                continue
            
            # 用户输入
            if msg_type == "HumanMessage":
                print(f"\n👤 用户问题:")
                print(f"   {msg.content[:100]}..." if len(msg.content) > 100 else f"   {msg.content}")
            
            # AI 思考（包含工具调用）
            elif msg_type == "AIMessage":
                # 检查是否有工具调用
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    for tool_call in msg.tool_calls:
                        print(f"\n💭 思考:")
                        print(f"   决定使用工具：{tool_call.get('name', 'unknown')}")
                        print(f"   工具参数：{tool_call.get('args', {})}")
                
                # 显示 AI 的思考内容（如果有）
                if msg.content and not (hasattr(msg, 'tool_calls') and msg.tool_calls):
                    content = msg.content.strip()
                    if content:
                        print(f"\n💭 思考:")
                        # 只显示简短的思考内容
                        lines = content.split('\n')
                        for line in lines[:5]:  # 限制显示 5 行
                            if line.strip():
                                print(f"   {line}")
                        if len(lines) > 5:
                            print(f"   ... (还有 {len(lines) - 5} 行)")
            
            # 工具执行结果
            elif msg_type == "ToolMessage":
                print(f"\n✅ 工具执行结果:")
                content = msg.content.strip()
                # 如果结果太长，只显示前 200 字符
                if len(content) > 200:
                    print(f"   {content[:200]}...")
                    print(f"   (结果长度：{len(content)} 字符)")
                else:
                    print(f"   {content}")
        
        print("\n" + "─" * 70)
    
    if "messages" in response and len(response["messages"]) > 0:
        return response["messages"][-1].content
    return "抱歉，我无法回答这个问题。"
