from src.agents.general_agent import run_agent as run_general_agent
from src.agents.travel_agent import run_travel_agent


def main():
    print("=" * 60)
    print("欢迎使用我的 Agent 系统 (基于千问模型)")
    print("=" * 60)
    print("\n📋 可用的 Agent:")
    print("  1 - 通用问答 Agent（聊天、知识问答、计算等）")
    print("  2 - 旅行规划 Agent（行程规划、预算计算、天气查询等）")
    print("\n💡 使用提示:")
    print("  • 输入数字 '1' 或 '2' 切换 Agent")
    print("  • 输入 'q' 退出程序")
    print("=" * 60)

    # 默认使用通用问答 Agent
    current_agent = "general"

    while True:
        # 根据当前 Agent 显示提示符
        if current_agent == "general":
            prefix = "[通用问答]"
            agent_name = "通用问答 Agent"
        else:
            prefix = "[旅行规划]"
            agent_name = "旅行规划 Agent"

        user_input = input(f"\n{prefix} 请输入你的问题 (输入 'h' 查看帮助): ")

        # 处理特殊命令
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("\n👋 感谢使用，再见！")
            break

        if user_input.lower() == 'h':
            print("\n📖 使用帮助:")
            print("  1         - 切换到通用问答 Agent")
            print("  2         - 切换到旅行规划 Agent")
            print("  h         - 显示此帮助信息")
            print("  q         - 退出程序")
            continue

        # 切换 Agent
        if user_input == '1':
            current_agent = "general"
            print("✅ 已切换到通用问答 Agent")
            continue
        elif user_input == '2':
            current_agent = "travel"
            print("✅ 已切换到旅行规划 Agent")
            continue

        # 处理用户问题
        try:
            if current_agent == "general":
                response = run_general_agent(user_input)
            else:
                response = run_travel_agent(user_input)

            print(f"\n💬 {agent_name} 回答：{response}")
        except Exception as e:
            print(f"❌ 发生错误：{e}")
            print("💡 提示：请检查输入是否正确，或尝试切换到其他 Agent")


if __name__ == "__main__":
    main()
