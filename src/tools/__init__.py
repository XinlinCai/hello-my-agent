"""
工具管理模块
自动发现和注册所有可用工具
支持工具分类、去重、元数据管理
"""
import importlib
from pathlib import Path
from langchain_classic.tools import BaseTool
from typing import Dict, List, Optional

# 手动导入已知工具（保证稳定性）
from .calculator_tool import calculator
from .travel_tools import get_travel_info, calculate_budget, check_weather
from .code_tools import execute_python_code, validate_python_syntax, format_code, explain_code_complexity

# 导入 RAG 工具（从 rag 模块）
from src.rag.retriever import knowledge_retrieval_tool  # noqa: F401

# 基础工具列表（始终包含，按功能分类）
BASE_TOOLS_CONFIG = {
    "calculation": ["calculator"],
    "travel": ["get_travel_info", "calculate_budget", "check_weather"],
    "programming": [
        "execute_python_code",
        "validate_python_syntax",
        "format_code",
        "explain_code_complexity",
    ],
    "knowledge": ["knowledge_retrieval_tool"],  # RAG 知识检索
}

# 扁平化工具列表
BASE_TOOLS = []
for tools in BASE_TOOLS_CONFIG.values():
    BASE_TOOLS.extend(tools)

__all__ = BASE_TOOLS.copy()


def get_all_tools() -> List:
    """
    获取所有已注册的基础工具
    
    Returns:
        list: 包含所有基础工具函数的列表
    """
    tools = []

    # 从当前模块获取已导入的工具
    for tool_name in BASE_TOOLS:
        if tool_name in globals():
            tools.append(globals()[tool_name])

    return tools


def get_tools_by_category() -> Dict[str, List]:
    """
    按分类获取工具
    
    Returns:
        dict: {分类名：[工具列表]}
    """
    result = {}
    for category, tool_names in BASE_TOOLS_CONFIG.items():
        result[category] = [
            globals()[name] for name in tool_names if name in globals()
        ]
    return result


def discover_tools(
        auto_discover: bool = True,
        verbose: bool = False,
        exclude_patterns: Optional[List[str]] = None
) -> List:
    """
    自动发现工具目录中的所有工具文件
    
    核心思路:
    1. 先加载基础工具（保证稳定性）
    2. 扫描新文件时，通过工具名称去重（而不是文件名）
    3. 默认排除测试/示例文件
    
    Args:
        auto_discover (bool): 是否启用自动发现
        verbose (bool): 是否打印详细日志
        exclude_patterns (list): 要排除的文件模式（如 ['example_*', 'test_*']）
        
    Returns:
        list: 工具函数列表
    """
    if not auto_discover:
        return get_all_tools()
    
    # 使用字典避免重复（核心：按工具名称去重，而非文件名）
    tools_dict = {}  # {tool_name: tool_object}
    
    # 1. 先添加基础工具
    for tool in get_all_tools():
        tool_name = tool.name if hasattr(tool, 'name') else str(tool)
        tools_dict[tool_name] = tool
    
    initial_count = len(tools_dict)
    current_dir = Path(__file__).parent
    
    # 默认排除模式（测试文件、示例文件、私有文件）
    default_excludes = ['example_*', 'test_*', '_*']
    if exclude_patterns:
        default_excludes.extend(exclude_patterns)
    
    # 2. 扫描并发现新工具
    for py_file in current_dir.glob('*.py'):
        # 跳过 __init__.py
        if py_file.name == '__init__.py':
            continue
        
        # 跳过符合排除模式的文件
        skip = False
        for pattern in default_excludes:
            if pattern.endswith('*'):
                if py_file.name.startswith(pattern[:-1]):
                    skip = True
                    break
            elif py_file.name == pattern:
                skip = True
                break
        
        if skip:
            if verbose:
                print(f"⏭️  跳过文件：{py_file.name}")
            continue
        
        try:
            # 动态导入模块
            module_name = py_file.stem
            module = importlib.import_module(f"src.tools.{module_name}")
            
            # 查找模块中所有工具
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                
                # 检查是否是有效的工具
                if not (isinstance(attr, BaseTool) or (hasattr(attr, 'name') and callable(attr))):
                    continue
                
                # 跳过私有成员
                if attr_name.startswith('_'):
                    continue
                
                # 获取工具名称并去重
                tool_name = attr.name if hasattr(attr, 'name') else attr_name
                
                if tool_name not in tools_dict:
                    tools_dict[tool_name] = attr
                    if verbose:
                        print(f"✅ 发现新工具：{tool_name} (来自 {py_file.name})")
                elif verbose:
                    print(f"⚠️  工具已存在，跳过：{tool_name}")
                    
        except Exception as e:
            if verbose:
                print(f"❌ 加载工具失败 {py_file.name}: {e}")
            # 静默失败，不影响其他工具
    
    # 转换为列表返回
    tools_list = list(tools_dict.values())
    
    if verbose:
        new_count = len(tools_dict) - initial_count
        print(f"\n📦 共加载 {len(tools_list)} 个工具 (新增 {new_count} 个):")
        for tool in tools_list:
            tool_name = tool.name if hasattr(tool, 'name') else str(tool)
            print(f"   • {tool_name}")
    
    return tools_list
