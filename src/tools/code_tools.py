"""
编程专用工具集
提供代码执行、格式化、语法检查等功能
"""

from langchain_classic.tools import tool
import ast


@tool
def execute_python_code(code: str) -> str:
    """
    执行 Python 代码并返回结果。
    
    Args:
        code: 要执行的 Python 代码字符串
        
    Returns:
        执行结果或错误信息
    """
    try:
        # 简单的代码执行（仅用于演示，生产环境需要更严格的安全控制）
        namespace = {"__builtins__": __builtins__}
        exec(code, namespace)
        return f"代码执行成功。\n输出：{namespace.get('result', '无返回值')}"
    except Exception as e:
        return f"代码执行失败：{str(e)}"


@tool
def validate_python_syntax(code: str) -> str:
    """
    验证 Python 代码的语法是否正确。
    
    Args:
        code: 要验证的 Python 代码字符串
        
    Returns:
        验证结果（语法正确/错误信息）
    """
    try:
        ast.parse(code)
        return "✅ 语法检查通过：代码语法正确"
    except SyntaxError as e:
        return f"❌ 语法错误：{e.msg} (第 {e.lineno} 行)"
    except Exception as e:
        return f"验证过程出错：{str(e)}"


@tool
def format_code(code: str, language: str = "python") -> str:
    """
    格式化代码，使其符合编码规范。
    
    Args:
        code: 要格式化的代码
        language: 编程语言（目前仅支持 python）
        
    Returns:
        格式化后的代码
    """
    if language.lower() != "python":
        return f"暂不支持 {language} 语言的格式化，目前仅支持 Python"
    
    try:
        # 使用 ast 解析并重新生成代码（基础格式化）
        tree = ast.parse(code)
        formatted = ast.unparse(tree)
        return f"格式化后的代码:\n```python\n{formatted}\n```"
    except Exception as e:
        return f"格式化失败：{str(e)}\n💡 请检查代码语法是否正确"


@tool
def explain_code_complexity(code: str) -> str:
    """
    分析代码的复杂度并提供优化建议。
    
    Args:
        code: 要分析的 Python 代码
        
    Returns:
        复杂度分析和优化建议
    """
    try:
        tree = ast.parse(code)
        
        # 统计基本信息
        func_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
        class_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
        line_count = len(code.strip().split('\n'))
        
        analysis = []
        analysis.append(f"📊 代码分析报告:")
        analysis.append(f"- 代码行数：{line_count} 行")
        analysis.append(f"- 函数数量：{func_count} 个")
        analysis.append(f"- 类数量：{class_count} 个")
        
        # 简单复杂度评估
        if line_count > 50:
            analysis.append("\n⚠️ 建议：代码超过 50 行，考虑拆分成多个函数")
        if func_count > 5:
            analysis.append("⚠️ 建议：函数较多，确保每个函数职责单一")
            
        return "\n".join(analysis)
    except Exception as e:
        return f"分析失败：{str(e)}"
