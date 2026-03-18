from src.agents.general_agent import run_general_agent as run_general_agent
from src.agents.travel_agent import run_travel_agent
from src.agents.coding_assistant_agent import run_programming_agent


def main():
    print("\n" + "=" * 60)
    print("🎉 欢迎使用我的 Agent 系统 (基于阿里云千问大模型)")
    print("=" * 60)
    print("\n📋 可用的 Agent:")
    print("  1️⃣  通用问答 Agent - 聊天、知识问答、计算等")
    print("  2️⃣  旅行规划 Agent - 行程规划、预算计算、天气查询等")
    print("  3️⃣  编程专家 Agent - 代码编写、调试、优化、架构设计")
    print("\n💡 快速开始:")
    print("  • 直接输入问题，当前 Agent 会为你解答")
    print("  • 输入数字 1/2/3 切换不同的 Agent")
    print("  • 输入 'h' 查看详细帮助")
    print("  • 输入 'q' 退出程序")
    print("=" * 60)

    # 默认使用通用问答 Agent
    current_agent = "general"

    while True:
        # 根据当前 Agent 显示提示符
        agent_config = {
            "general": {"prefix": "[通用问答]", "name": "通用问答 Agent", "emoji": "🤖"},
            "travel": {"prefix": "[旅行规划]", "name": "旅行规划 Agent", "emoji": "🗺️"},
            "programming": {"prefix": "[编程专家]", "name": "编程专家 Agent", "emoji": "💻"}
        }
        
        config = agent_config.get(current_agent, agent_config["general"])
        prefix = f"{config['emoji']}{config['prefix']}"
        agent_name = config["name"]

        user_input = input(f"\n{prefix} 请输入你的问题：").strip()

        # 处理空输入
        if not user_input:
            print("⚠️  输入为空，请重新输入")
            continue
                
        # 处理特殊命令
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("\n👋 感谢使用，再见！祝你有美好的一天！✨")
            break
                
        if user_input.lower() == 'h':
            print("\n" + "=" * 60)
            print("📖 详细使用帮助:")
            print("=" * 60)
            print("\n【切换 Agent】")
            print("  1         - 切换到通用问答 Agent")
            print("  2         - 切换到旅行规划 Agent")
            print("  3         - 切换到编程专家 Agent")
            print("\n【其他命令】")
            print("  h         - 显示此帮助信息")
            print("  q         - 退出程序")
            print("\n【使用建议】")
            print("  • 通用问答：适合日常聊天、知识查询、简单计算")
            print("  • 旅行规划：制定旅行计划、查询目的地信息、预算规划")
            print("  • 编程专家：代码编写、调试、优化、技术咨询")
            print("=" * 60)
            continue

        # 切换 Agent
        if user_input == '1':
            current_agent = "general"
            print("✅ 已切换到通用问答 Agent 🤖")
            continue
        elif user_input == '2':
            current_agent = "travel"
            print("✅ 已切换到旅行规划 Agent 🗺️")
            continue
        elif user_input == '3':
            current_agent = "programming"
            print("✅ 已切换到编程专家 Agent 💻")
            continue

        # 处理用户问题
        try:
            print(f"\n⏳ {agent_name} 正在思考中...")
                    
            if current_agent == "general":
                response = run_general_agent(user_input)
            elif current_agent == "travel":
                response = run_travel_agent(user_input)
            elif current_agent == "programming":
                response = run_programming_agent(user_input)
                    
            print(f"\n💬 {agent_name} 回答:\n{'-' * 60}")
            print(response)
            print('-' * 60)
        except Exception as e:
            print(f"\n❌ 抱歉，发生错误：{e}")
            print("💡 建议：请检查输入是否正确，或尝试切换到其他 Agent 寻求帮助")


if __name__ == "__main__":
    main()
