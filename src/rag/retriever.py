"""
RAG 检索工具

将知识库检索功能封装为 Agent 可调用的工具
"""
from langchain.tools import BaseTool
from .knowledge_base import KnowledgeBase
from config.settings import KNOWLEDGE_DIR

# ========== 全局单例 KnowledgeBase ==========
# 程序启动时初始化一次，后续所有请求共享此实例
_global_knowledge_base = None


def get_global_knowledge_base(force_init: bool = False) -> KnowledgeBase:
    """
    获取全局 KnowledgeBase 单例实例
    
    Args:
        force_init (bool): 是否强制重新初始化（默认 False）
    
    Returns:
        KnowledgeBase: 全局知识库实例
    """
    global _global_knowledge_base
    
    # 首次调用或强制重置时初始化
    if _global_knowledge_base is None or force_init:
        print("📚 正在初始化全局知识库...")
        _global_knowledge_base = KnowledgeBase(knowledge_dir=str(KNOWLEDGE_DIR))
        
        # 预加载向量库（启动时完成，后续查询无需等待）
        success = _global_knowledge_base.build_vectorstore()
        
        if success:
            doc_count = len(_global_knowledge_base.vectorstore.docstore._dict) if _global_knowledge_base.vectorstore else 0
            print(f"✅ 全局知识库初始化完成（共 {doc_count} 个文档块）")
        else:
            print("⚠️  知识库为空或未找到文档")
    
    return _global_knowledge_base


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
        执行知识检索（使用全局单例实例）
        
        Args:
            query: 用户查询的问题
            
        Returns:
            str: 检索到的知识内容
        """
        # 使用全局单例，避免重复加载
        kb = get_global_knowledge_base()
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


def initialize_rag_at_startup():
    """
    启动时预加载 RAG 知识库
    
    建议在 main.py 启动时调用此函数，提前完成初始化
    
    Returns:
        bool: 是否成功初始化
    """
    try:
        kb = get_global_knowledge_base()
        return kb.vectorstore is not None
    except Exception as e:
        print(f"❌ RAG 预加载失败：{e}")
        return False
