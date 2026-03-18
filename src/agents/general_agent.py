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


def run_general_agent(query: str):
    """运行通用 Agent"""
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]
    response = general_agent_executor.invoke({"messages": messages})
    if "messages" in response and len(response["messages"]) > 0:
        return response["messages"][-1].content
    return "抱歉，我无法回答这个问题。"
