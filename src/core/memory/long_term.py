"""长期记忆模块 - 持久化存储用户画像"""
import json
from pathlib import Path
from typing import Any, Dict
from config.settings import USER_PROFILES_PATH


class LongTermMemory:
    """长期记忆 - 持久化存储用户画像"""
    
    def __init__(self, user_id: str = "default", storage_path: str = None):
        """
        初始化长期记忆
        
        Args:
            user_id: 用户 ID
            storage_path: 存储文件路径（默认使用配置文件中的 USER_PROFILES_PATH）
        """
        self.user_id = user_id
        
        # 使用配置文件中的路径，如果传入了自定义路径则使用自定义路径
        if storage_path is None:
            self.storage_path = USER_PROFILES_PATH
        else:
            self.storage_path = Path(storage_path)
        
        self.profile: Dict[str, Any] = {}
        self._load()
    
    def _load(self):
        """从文件加载用户画像"""
        if self.storage_path.exists():
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.profile = data.get(self.user_id, {})
    
    def _save(self):
        """保存用户画像到文件"""
        try:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            
            data = {}
            if self.storage_path.exists():
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            
            data[self.user_id] = self.profile
            
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 保存用户画像失败：{e}")
            print(f"   文件路径：{self.storage_path.absolute()}")
    
    def set_preference(self, key: str, value: Any):
        """
        设置用户偏好
        
        Args:
            key: 偏好键名
            value: 偏好值
        """
        self.profile[key] = value
        self._save()
    
    def get_preference(self, key: str, default: Any = None) -> Any:
        """
        获取用户偏好
        
        Args:
            key: 偏好键名
            default: 默认值
            
        Returns:
            用户偏好值
        """
        return self.profile.get(key, default)
    
    def get_all_preferences(self) -> Dict[str, Any]:
        """获取所有用户偏好"""
        return self.profile.copy()
    
    def extract_fact(self, text: str) -> bool:
        """
        从文本中提取值得记忆的事实（增强规则）
        
        Args:
            text: 输入文本
            
        Returns:
            是否提取到事实
        """
        extracted_facts = {}
        
        # 1. 偏好提取
        if any(kw in text for kw in ["喜欢", "偏好", "倾向于", "更爱"]):
            extracted_facts["preference"] = text
        
        # 2. 身份/职业提取
        if any(kw in text for kw in ["我是", "我做", "从事", "工作", "职业", "程序员", "工程师", "设计师"]):
            if "程序" in text or "开发" in text or "设计" in text or "工程" in text or "工作" in text:
                extracted_facts["occupation"] = text
        
        # 3. 位置信息
        if any(kw in text for kw in ["住在", "家在", "位于", "在哪个城市", "北京", "上海", "广州", "深圳"]):
            extracted_facts["location"] = text
        
        # 4. 消费水平/预算
        if any(kw in text for kw in ["预算", "价格", "贵", "便宜", "经济型", "豪华", "性价比"]):
            extracted_facts["budget_level"] = text
        
        # 5. 行为模式/习惯
        if any(kw in text for kw in ["经常", "总是", "从不", "一般", "通常", "习惯"]):
            extracted_facts["habit"] = text
        
        # 6. 旅行相关偏好
        if any(kw in text for kw in ["旅行", "旅游", "景点", "酒店", "住宿", "美食", "交通"]):
            if any(kw in text for kw in ["喜欢", "想要", "希望", "需要"]):
                extracted_facts["travel_preference"] = text
        
        # 批量保存
        if extracted_facts:
            for key, value in extracted_facts.items():
                self.set_preference(key, value)
            return True
        
        return False
    
    def clear(self):
        """清空当前用户的画像数据"""
        self.profile.clear()
        self._save()
    
    def get_storage_info(self) -> Dict[str, Any]:
        """
        获取存储信息（用于调试）
        
        Returns:
            包含存储路径和状态的字典
        """
        return {
            "storage_path": str(self.storage_path.absolute()),
            "file_exists": self.storage_path.exists(),
            "user_id": self.user_id,
            "preferences_count": len(self.profile)
        }
