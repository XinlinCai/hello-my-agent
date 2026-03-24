import os
from dotenv import load_dotenv
from pathlib import Path

# 指定 UTF-8 编码加载 .env
load_dotenv(encoding='utf-8')

# ==================== API 配置 ====================
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

# ==================== 项目路径配置 ====================
# 获取项目根目录（当前文件的上两级目录）
PROJECT_ROOT = Path(__file__).parent.parent

# ==================== 知识库配置 ====================
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
# 确保知识库目录存在
KNOWLEDGE_DIR.mkdir(exist_ok=True)

# ==================== 数据存储配置 ====================
# 数据目录（存储用户画像、缓存等持久化数据）
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# 用户画像文件路径（长期记忆存储）
USER_PROFILES_PATH = DATA_DIR / "user_profiles.json"

# ==================== 记忆模块配置 ====================
# 默认用户 ID
DEFAULT_USER_ID = os.getenv("DEFAULT_USER_ID", "default_user")

# 短期记忆最大轮数
SHORT_TERM_MAX_TURNS = int(os.getenv("SHORT_TERM_MAX_TURNS", "10"))

# 上下文工程保留轮数
CONTEXT_MAX_TURNS = int(os.getenv("CONTEXT_MAX_TURNS", "5"))