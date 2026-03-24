"""统一记忆管理器 - 整合短期记忆、长期记忆和上下文工程"""
from typing import Dict
from .short_term import ShortTermMemory
from .long_term import LongTermMemory
from .context_engine import ContextEngine
from config.settings import DEFAULT_USER_ID


class MemoryManager:
    """统一的记忆管理器"""
    
    def __init__(self, user_id: str = None):
        """
        初始化记忆管理器
        
        Args:
            user_id: 用户 ID（默认使用配置文件中的 DEFAULT_USER_ID）
        """
        actual_user_id = user_id if user_id is not None else DEFAULT_USER_ID
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory(user_id=actual_user_id)
        self.context_engine = ContextEngine(self.short_term, self.long_term)
    
    def add_interaction(self, user_input: str, ai_response: str):
        """
        记录交互到记忆
        
        Args:
            user_input: 用户输入
            ai_response: AI 响应
        """
        self.short_term.add_message("human", user_input)
        self.short_term.add_message("ai", ai_response)
        self.long_term.extract_fact(user_input)
    
    def get_context(self, current_query: str, system_prompt: str):
        """
        获取优化后的上下文
        
        Args:
            current_query: 当前查询
            system_prompt: 系统提示词
            
        Returns:
            优化后的消息列表
        """
        return self.context_engine.build_context(current_query, system_prompt)
    
    def clear_short_term(self):
        """清空短期记忆"""
        self.short_term.clear()
    
    def clear_long_term(self):
        """清空长期记忆"""
        self.long_term.clear()
    
    def get_summary(self) -> Dict:
        """
        获取记忆摘要
        
        Returns:
            包含记忆统计信息的字典
        """
        return {
            "short_term_turns": self.short_term.size(),
            "long_term_facts_count": len(self.long_term.get_all_preferences())
        }
    
    def get_storage_info(self) -> Dict:
        """
        获取存储信息（用于调试）
        
        Returns:
            包含存储路径和状态的字典
        """
        return self.long_term.get_storage_info()
    
    def clear_all(self):
        """清空所有记忆（短期 + 长期）"""
        self.clear_short_term()
        self.clear_long_term()
