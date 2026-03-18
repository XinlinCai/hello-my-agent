from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from config.settings import DASHSCOPE_API_KEY
from src.tools.code_tools import execute_python_code, validate_python_syntax, format_code, explain_code_complexity
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from src.core.prompts import get_system_prompt

load_dotenv()

# 初始化千问模型（使用 ChatTongyi，支持工具绑定）
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",
    temperature=0.7,
    max_tokens=2500
)

# 获取编程专家 Agent 的系统提示词
system_prompt = get_system_prompt("programming_expert")

# 编程专用工具列表
tools = [
    execute_python_code,      # 执行 Python 代码
    validate_python_syntax,   # 验证语法
    format_code,              # 格式化代码
    explain_code_complexity,  # 分析复杂度
]

# 使用 LangGraph 创建 ReAct Agent（支持多参数工具）
programming_agent_executor = create_react_agent(llm, tools)


def run_programming_agent(query: str) -> str:
    """
    运行编程专家 Agent
    
    参数:
        query: 用户关于编程的问题或需求
    
    返回:
        Agent 的回答
    """
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
        response = programming_agent_executor.invoke({"messages": messages})
        if "messages" in response and len(response["messages"]) > 0:
            return response["messages"][-1].content
        return "抱歉，我无法回答这个问题。"
    except Exception as e:
        return f"处理编程请求时发生错误：{str(e)}"
