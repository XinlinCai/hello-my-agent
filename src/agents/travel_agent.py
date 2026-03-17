from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from config.settings import DASHSCOPE_API_KEY
from src.tools import get_travel_info, calculate_budget, check_weather
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from src.core.prompts import get_system_prompt

load_dotenv()

# 初始化千问模型（使用 ChatTongyi，支持工具绑定）
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",
    temperature=0.8,
    max_tokens=2500
)

# 获取旅行 Agent 的系统提示词
system_prompt = get_system_prompt("travel")

# 旅行规划专用工具列表
tools = [
    get_travel_info,  # 获取目的地信息
    calculate_budget,  # 计算预算
    check_weather,  # 查询天气
]

# 使用 LangGraph 创建 ReAct Agent（支持多参数工具）
travel_agent_executor = create_react_agent(llm, tools)


def run_travel_agent(query: str) -> str:
    """
    运行旅行规划 Agent
    
    参数:
        query: 用户关于旅行的问题或需求
    
    返回:
        Agent 的回答
    """
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
        response = travel_agent_executor.invoke({"messages": messages})
        if "messages" in response and len(response["messages"]) > 0:
            return response["messages"][-1].content
        return "抱歉，我无法回答这个问题。"
    except Exception as e:
        return f"处理旅行规划请求时发生错误：{str(e)}"
