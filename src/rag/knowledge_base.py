"""
RAG 知识库核心模块

提供基础的文档加载、向量化和检索功能
支持格式：TXT, Markdown, PDF
"""
import os
from typing import List, Optional
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from config.settings import KNOWLEDGE_DIR


class KnowledgeBase:
    """
    知识库类 - 负责文档加载、向量化和检索
    
    Attributes:
        knowledge_dir: 知识库目录路径
        chunk_size: 文本块大小
        chunk_overlap: 文本块重叠量
        vectorstore: FAISS 向量存储
        embeddings: 嵌入模型
    """
    
    def __init__(
        self, 
        knowledge_dir: str = None,
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ):
        # 如果传入了自定义路径则使用自定义路径，否则使用配置文件中的默认路径
        self.knowledge_dir = knowledge_dir if knowledge_dir else str(KNOWLEDGE_DIR)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # 初始化嵌入模型
        self.embeddings = DashScopeEmbeddings(
            model="text-embedding-v2",
            dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
        )
        
        # 初始化文本分割器
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", "。", "！", "？", "；", ".", "!", "?", ";", " ", ""]
        )
        
        self.vectorstore = None
    
    def load_documents(self) -> List[Document]:
        """
        加载知识库目录下的所有文档（支持 TXT, MD, PDF）
        
        Returns:
            List[Document]: 文档列表
        """
        documents = []
        
        if not os.path.exists(self.knowledge_dir):
            print(f"⚠️  知识库目录不存在：{self.knowledge_dir}")
            return documents
        
        # 遍历目录下所有文件
        for root, dirs, files in os.walk(self.knowledge_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                relative_path = os.path.relpath(filepath, self.knowledge_dir)
                
                try:
                    # 根据文件扩展名选择不同的加载器
                    if filename.endswith('.pdf'):
                        # PDF 文件使用 PyPDFLoader
                        loader = PyPDFLoader(filepath)
                        docs = loader.load()
                        print(f"✅ 加载 PDF: {relative_path} ({len(docs)} 页)")
                    elif filename.endswith('.md') or filename.endswith('.markdown'):
                        # Markdown 文件使用 TextLoader（简单有效）
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if content.strip():
                                docs = self.text_splitter.create_documents([content])
                                print(f"✅ 加载 Markdown: {relative_path}")
                            else:
                                print(f"⚠️  文件为空：{relative_path}")
                                continue
                    elif filename.endswith('.txt'):
                        # TXT 文件使用 TextLoader
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if content.strip():
                                docs = self.text_splitter.create_documents([content])
                                print(f"✅ 加载 TXT: {relative_path}")
                            else:
                                print(f"⚠️  文件为空：{relative_path}")
                                continue
                    else:
                        # 跳过不支持的文件类型
                        continue
                    
                    # 为所有文档添加元数据
                    for doc in docs:
                        doc.metadata["source"] = relative_path
                    documents.extend(docs)
                    
                except Exception as e:
                    print(f"❌ 读取文件失败 {filename}: {e}")
        
        if not documents:
            print(f"⚠️  未在知识库目录中找到支持的文档 (.txt, .md, .pdf)")
        
        return documents
    
    def build_vectorstore(self, force_rebuild: bool = False) -> bool:
        """
        构建或重建向量库
        
        Args:
            force_rebuild: 是否强制重建
            
        Returns:
            bool: 是否成功构建
        """
        # 如果已有向量库且不强制重建，直接返回成功
        if self.vectorstore and not force_rebuild:
            return True
        
        docs = self.load_documents()
        
        if not docs:
            return False
        
        self.vectorstore = FAISS.from_documents(docs, self.embeddings)
        return True
    
    def clear_cache(self):
        """
        清除缓存的向量库（用于手动刷新）
        """
        self.vectorstore = None
        print("🔄 知识库缓存已清除，下次查询将重新加载")
    
    def search(self, query: str, k: int = 3) -> str:
        """
        检索相关知识
        
        Args:
            query: 查询问题
            k: 返回最相关的 k 个结果
            
        Returns:
            str: 检索到的知识内容（格式化后）
        """
        if not self.vectorstore:
            success = self.build_vectorstore()
            if not success:
                return "⚠️  知识库为空"
        
        results = self.vectorstore.similarity_search(query, k=k)
        
        if not results:
            return "未在知识库中找到相关信息。"
        
        # 格式化输出
        formatted_results = []
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get("source", "未知来源")
            formatted_results.append(f"[来源：{source}]\n{doc.page_content}")
        
        return "\n\n---\n\n".join(formatted_results)
    
    def search_with_docs(self, query: str, k: int = 3) -> List[Document]:
        """
        检索并返回文档对象（不格式化）
        
        Args:
            query: 查询问题
            k: 返回数量
            
        Returns:
            List[Document]: 相关文档列表
        """
        if not self.vectorstore:
            self.build_vectorstore()
        
        return self.vectorstore.similarity_search(query, k=k)
