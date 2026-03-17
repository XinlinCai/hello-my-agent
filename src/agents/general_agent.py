from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from config.settings import DASHSCOPE_API_KEY
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from src.tools import calculator
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

# 工具列表
tools = [calculator]

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
