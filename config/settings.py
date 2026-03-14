import os
from dotenv import load_dotenv

# 指定 UTF-8 编码加载 .env
load_dotenv(encoding='utf-8')

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")