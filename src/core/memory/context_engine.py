"""上下文工程引擎 - 智能组织输入信息"""
from typing import List
from langchain_core.messages import BaseMessage, SystemMessage
from .short_term import ShortTermMemory
from .long_term import LongTermMemory
from config.settings import CONTEXT_MAX_TURNS


class ContextEngine:
    """上下文工程引擎 - 智能筛选与组织上下文信息"""
    
    def __init__(self, short_term: ShortTermMemory, long_term: LongTermMemory):
        """
        初始化上下文引擎
        
        Args:
            short_term: 短期记忆实例
            long_term: 长期记忆实例
        """
        self.short_term = short_term
        self.long_term = long_term
        self.max_context_turns = CONTEXT_MAX_TURNS
    
    def build_context(self, current_query: str, system_prompt: str) -> List[BaseMessage]:
        """
        构建优化的上下文
        
        Args:
            current_query: 当前查询
            system_prompt: 系统提示词
            
        Returns:
            优化后的消息列表
        """
        messages = [SystemMessage(content=system_prompt)]
        
        user_facts = self.long_term.get_all_preferences()
        if user_facts:
            facts_text = "用户背景：\n" + "\n".join(
                f"- {k}: {v}" for k, v in user_facts.items()
            )
            messages.append(SystemMessage(content=facts_text))
        
        relevant_history = self._select_relevant_history(current_query)
        messages.extend(relevant_history)
        
        return messages
    
    def _select_relevant_history(self, query: str, k: int = None) -> List[BaseMessage]:
        """
        选择相关的历史对话
        
        Args:
            query: 当前查询
            k: 选择的轮数
            
        Returns:
            相关的历史对话列表
        """
        if k is None:
            k = self.max_context_turns
        
        history = self.short_term.get_history()
        
        if len(history) <= k * 2:
            return history
        
        return history[-k * 2:]
    
    def estimate_token_count(self, messages: List[BaseMessage]) -> int:
        """
        估算 token 数量（简化版）
        
        Args:
            messages: 消息列表
            
        Returns:
            估算的 token 数量
        """
        total_chars = sum(
            len(msg.content) 
            for msg in messages 
            if hasattr(msg, 'content') and msg.content
        )
        return total_chars // 4
