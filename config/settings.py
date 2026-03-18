import os
from dotenv import load_dotenv
from pathlib import Path

# 指定 UTF-8 编码加载 .env
load_dotenv(encoding='utf-8')

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

# 获取项目根目录（当前文件的上两级目录）
PROJECT_ROOT = Path(__file__).parent.parent

# 知识库目录（使用绝对路径）
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"

# 确保知识库目录存在
KNOWLEDGE_DIR.mkdir(exist_ok=True)