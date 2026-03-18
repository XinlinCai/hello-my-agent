"""
RAG 检索工具

将知识库检索功能封装为 Agent 可调用的工具
"""
from langchain.tools import BaseTool
from .knowledge_base import KnowledgeBase
from config.settings import KNOWLEDGE_DIR


class KnowledgeRetrievalTool(BaseTool):
    """
    知识检索工具 - 供 Agent 调用
    
    名称：knowledge_retrieval
    功能：从本地知识库检索相关信息
    """
    
    name: str = "knowledge_retrieval"
    description: str = (
        "从本地知识库中检索相关信息。"
        "当用户询问特定领域的知识、技术细节、概念解释或事实性问题时使用此工具。"
        "输入应该是用户的查询问题，可以是中文或英文。"
        "示例问题："
        "- Python 装饰器如何使用？"
        "- 什么是列表推导式？"
        "- 面向对象编程的特点是什么？"
    )
    
    def _run(self, query: str) -> str:
        """
        执行知识检索
        
        Args:
            query: 用户查询的问题
            
        Returns:
            str: 检索到的知识内容
        """
        # 使用配置文件中的知识库目录
        kb = KnowledgeBase(knowledge_dir=str(KNOWLEDGE_DIR))
        return kb.search(query, k=3)
    
    async def _arun(self, query: str) -> str:
        """
        异步执行（暂不支持）
        
        Raises:
            NotImplementedError: 异步检索暂不支持
        """
        raise NotImplementedError("异步检索暂不支持")


# 创建工具实例（方便直接导入使用）
knowledge_retrieval_tool = KnowledgeRetrievalTool()


def search_knowledge(query: str) -> str:
    """
    便捷函数：从知识库检索信息
    
    Args:
        query: 查询问题
        
    Returns:
        str: 检索结果
    """
    return knowledge_retrieval_tool.run(query)
