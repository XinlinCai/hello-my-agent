"""短期记忆模块 - 维护对话历史"""
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from collections import deque
from config.settings import SHORT_TERM_MAX_TURNS


class ShortTermMemory:
    """短期记忆 - 维护对话历史"""
    
    def __init__(self, max_turns: int = None):
        """
        初始化短期记忆
        
        Args:
            max_turns: 最大保留对话轮数（默认使用配置文件中的 SHORT_TERM_MAX_TURNS）
        """
        self.max_turns = max_turns if max_turns is not None else SHORT_TERM_MAX_TURNS
        self.history = deque(maxlen=self.max_turns * 2)
    
    def add_message(self, role: str, content: str):
        """
        添加消息到历史记录
        
        Args:
            role: 角色类型 ("human" 或 "ai")
            content: 消息内容
        """
        if role == "human":
            self.history.append(HumanMessage(content=content))
        elif role == "ai":
            self.history.append(AIMessage(content=content))
    
    def get_history(self) -> List[BaseMessage]:
        """获取完整的对话历史"""
        return list(self.history)
    
    def get_recent_turns(self, k: int = 5) -> List[BaseMessage]:
        """
        获取最近 k 轮对话
        
        Args:
            k: 轮数
            
        Returns:
            最近 k 轮的对话历史
        """
        recent = list(self.history)[-k * 2:]
        return recent
    
    def clear(self):
        """清空记忆"""
        self.history.clear()
    
    def size(self) -> int:
        """获取当前对话轮数"""
        return len(self.history) // 2
