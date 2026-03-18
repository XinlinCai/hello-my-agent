"""
RAG 模块 - 检索增强生成（Retrieval-Augmented Generation）

为 Agent 提供外部知识库检索能力

模块结构:
- knowledge_base: 知识库核心类（文档加载、向量化、检索）
- retriever: 检索工具（封装为 Agent 可调用的 Tool）

使用示例:
    # 方式 1：直接使用知识库
    from src.rag import KnowledgeBase
    kb = KnowledgeBase()
    result = kb.search("Python 装饰器")
    
    # 方式 2：使用检索工具
    from src.rag import knowledge_retrieval_tool
    result = knowledge_retrieval_tool.run("Python 装饰器")
    
    # 方式 3：便捷函数
    from src.rag import search_knowledge
    result = search_knowledge("Python 装饰器")
"""

from .knowledge_base import KnowledgeBase
from .retriever import (
    KnowledgeRetrievalTool,
    knowledge_retrieval_tool,
    search_knowledge
)

__all__ = [
    # 核心类
    "KnowledgeBase",
    
    # 工具类
    "KnowledgeRetrievalTool",
    
    # 工具实例
    "knowledge_retrieval_tool",
    
    # 便捷函数
    "search_knowledge"
]
