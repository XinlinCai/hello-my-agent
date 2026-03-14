from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """一个简单的计算器工具，输入数学表达式，返回计算结果。"""
    try:
        # 安全地计算表达式（仅用于演示，生产环境需谨慎）
        result = eval(expression, {"__builtins__": {}}, {})
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {e}"
