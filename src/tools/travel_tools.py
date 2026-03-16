from langchain_classic.tools import StructuredTool
from datetime import datetime, timedelta


def get_travel_info_func(destination: str, days: int = 3) -> str:
    """获取旅行目的地信息和建议行程的内部函数"""
    travel_tips = {
        "北京": "北京是中国的首都，有故宫、长城、天坛等著名景点。最佳旅游季节是春秋两季。",
        "上海": "上海是现代化国际大都市，有外滩、豫园、迪士尼乐园等景点。美食丰富，购物便利。",
        "杭州": "杭州以西湖闻名，有灵隐寺、龙井茶园等景点。适合休闲度假。",
        "西安": "西安是古都，有兵马俑、大雁塔、古城墙等历史遗迹。历史文化爱好者的天堂。",
        "成都": "成都有大熊猫基地、宽窄巷子、锦里等景点。美食众多，生活节奏悠闲。",
    }

    default_tip = f"{destination}是一个值得一游的地方！建议提前了解当地天气和文化，准备好合适的衣物和装备。"
    tip = travel_tips.get(destination, default_tip)

    itinerary = f"\n\n{days}天行程建议：\n"
    for i in range(1, days + 1):
        itinerary += f"第{i}天：探索{destination}的主要景点，体验当地文化和美食。\n"

    return f"{tip}{itinerary}"


def calculate_budget_func(destination: str, days: int, budget_level: str = "medium") -> str:
    """计算旅行预算的内部函数"""
    daily_budgets = {
        "low": 300,
        "medium": 600,
        "high": 1500
    }

    transport_costs = {
        "北京": 800,
        "上海": 1000,
        "杭州": 700,
        "西安": 600,
        "成都": 750,
    }

    daily_cost = daily_budgets.get(budget_level.lower(), 600)
    transport = transport_costs.get(destination, 500)

    accommodation = daily_cost * 0.4 * days
    food = daily_cost * 0.3 * days
    activities = daily_cost * 0.2 * days
    shopping = daily_cost * 0.1 * days

    total = accommodation + food + activities + shopping + transport

    budget_breakdown = f"""
【{destination} {days}天旅行预算】({'舒适型' if budget_level == 'medium' else '经济型' if budget_level == 'low' else '豪华型'})

💰 总预算：¥{total:.2f}

详细分解:
  🏨 住宿：¥{accommodation:.2f}
  🍜 餐饮：¥{food:.2f}
  🎫 门票：¥{activities:.2f}
  🛍️  购物：¥{shopping:.2f}
  ✈️  交通：¥{transport:.2f}

人均每日花费：¥{total / days:.2f}
"""
    return budget_breakdown


def check_weather_func(destination: str, date: str = None) -> str:
    """查询目的地天气的内部函数"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    weather_conditions = ["晴", "多云", "小雨", "阴天"]
    temperatures = {
        "北京": "15-25°C",
        "上海": "18-28°C",
        "杭州": "16-26°C",
        "西安": "14-24°C",
        "成都": "17-27°C",
    }

    temp = temperatures.get(destination, "15-25°C")
    weather = weather_conditions[hash(date) % len(weather_conditions)]

    return f"{destination} {date} 天气：{weather}，气温：{temp}\n建议：根据天气准备合适的衣物和雨具。"


# 使用 StructuredTool 定义支持多参数的工具
get_travel_info = StructuredTool.from_function(
    func=get_travel_info_func,
    name="get_travel_info",
    description="获取旅行目的地信息和建议行程。输入目的地城市名和可选的天数（默认 3 天）。例如：'北京，5 天'"
)

calculate_budget = StructuredTool.from_function(
    func=calculate_budget_func,
    name="calculate_budget",
    description="计算旅行预算。需要提供目的地、天数和预算级别（low/medium/high）。例如：'上海，5 天，medium'"
)

check_weather = StructuredTool.from_function(
    func=check_weather_func,
    name="check_weather",
    description="查询目的地天气。需要提供城市名和可选的日期（YYYY-MM-DD 格式，默认为今天）"
)
