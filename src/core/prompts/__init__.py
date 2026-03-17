"""
提示词模板管理模块
统一管理所有 Agent 的系统提示词
"""

from .templates import (
    GENERAL_AGENT_SYSTEM_PROMPT, 
    TRAVEL_AGENT_SYSTEM_PROMPT,
    LIN_DAIYU_AGENT_PROMPT,
    PROGRAMMING_EXPERT_AGENT_PROMPT
)


# 预定义的 Agent 类型映射（保持向后兼容）
PREDEFINED_AGENTS = {
    "general": GENERAL_AGENT_SYSTEM_PROMPT,
    "travel": TRAVEL_AGENT_SYSTEM_PROMPT,
    "lin_daiyu": LIN_DAIYU_AGENT_PROMPT,
    "programming_expert": PROGRAMMING_EXPERT_AGENT_PROMPT
}


def get_system_prompt(agent_type: str = "general") -> str:
    """
    获取指定 Agent 的系统提示词
    
    Args:
        agent_type: Agent 类型 ("general", "travel", "lin_daiyu", "programming_expert")
        
    Returns:
        系统提示词字符串
        
    Raises:
        ValueError: 当指定的 Agent 类型不存在时
    """
    if agent_type not in PREDEFINED_AGENTS:
        available_agents = ", ".join(PREDEFINED_AGENTS.keys())
        raise ValueError(f"未知的 Agent 类型：{agent_type}。可用的 Agent: {available_agents}")
    
    return PREDEFINED_AGENTS[agent_type]


def list_available_agents() -> list:
    """
    列出所有可用的 Agent 类型
    
    Returns:
        包含所有可用 Agent 类型的列表
    """
    return list(PREDEFINED_AGENTS.keys())


def get_agent_info(agent_type: str = None) -> dict:
    """
    获取 Agent 的详细信息
    
    Args:
        agent_type: 可选，指定 Agent 类型。如果不指定，返回所有 Agent 信息
        
    Returns:
        字典，包含 Agent 的描述和信息
    """
    agent_descriptions = {
        "general": "通用问答 Agent（聊天、知识问答、计算等）",
        "travel": "旅行规划 Agent（行程规划、预算计算、天气查询等）",
        "lin_daiyu": "林黛玉风格 Agent（古典文学风格，诗词歌赋）",
        "programming_expert": "编程专家 Agent（全栈开发，架构设计，代码优化）"
    }
    
    if agent_type:
        if agent_type not in PREDEFINED_AGENTS:
            return {"error": f"未知的 Agent 类型：{agent_type}"}
        return {
            "type": agent_type,
            "description": agent_descriptions.get(agent_type, "未知描述"),
            "prompt_length": len(PREDEFINED_AGENTS[agent_type])
        }
    
    return {
        agent_type: {
            "description": desc,
            "prompt_length": len(PREDEFINED_AGENTS[agent_type])
        }
        for agent_type, desc in agent_descriptions.items()
    }


# 导出所有模板，方便外部直接使用
__all__ = [
    'get_system_prompt',
    'list_available_agents',
    'get_agent_info',
    'GENERAL_AGENT_SYSTEM_PROMPT',
    'TRAVEL_AGENT_SYSTEM_PROMPT',
    'LIN_DAIYU_AGENT_PROMPT',
    'PROGRAMMING_EXPERT_AGENT_PROMPT'
]
