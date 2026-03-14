from dotenv import load_dotenv
from langchain_classic.agents import initialize_agent, AgentType
from langchain_community.llms import Tongyi
from src.tools import calculator
from config.settings import DASHSCOPE_API_KEY

load_dotenv()

# 初始化千问模型
llm = Tongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",
    temperature=0.7,
    max_tokens=1500
)

# 工具列表（这里只用了计算器，你可以继续添加其他工具）
tools = [calculator]

# 初始化 Agent 使用 ReAct 框架
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


def run_agent(query: str):
    """使用 invoke 替代已弃用的 run 方法"""
    result = agent.invoke({"input": query})
    return result["output"]
