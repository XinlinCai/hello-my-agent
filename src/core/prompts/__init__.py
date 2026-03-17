"""
提示词模板管理模块
统一管理所有 Agent 的系统提示词
"""

from .templates import GENERAL_AGENT_SYSTEM_PROMPT, TRAVEL_AGENT_SYSTEM_PROMPT


def get_system_prompt(agent_type: str = "general") -> str:
    """
    获取指定 Agent 的系统提示词
    
    Args:
        agent_type: Agent 类型 ("general" 或 "travel")
        
    Returns:
        系统提示词字符串
    """
    prompts = {
        "general": GENERAL_AGENT_SYSTEM_PROMPT,
        "travel": TRAVEL_AGENT_SYSTEM_PROMPT
    }
    
    return prompts.get(agent_type, GENERAL_AGENT_SYSTEM_PROMPT)


# 导出所有模板，方便外部直接使用
__all__ = [
    'get_system_prompt',
    'GENERAL_AGENT_SYSTEM_PROMPT',
    'TRAVEL_AGENT_SYSTEM_PROMPT'
]
