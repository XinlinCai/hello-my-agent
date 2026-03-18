import random
from src.agents.general_agent import run_general_agent as run_general_agent
from src.agents.travel_agent import run_travel_agent
from src.agents.coding_assistant_agent import run_programming_agent
from src.rag.retriever import initialize_rag_at_startup


def print_welcome_banner():
    """打印欢迎横幅"""
    print("\n" + "═" * 70)
    print("✨  欢迎使用我的 Agent 系统  ✨")
    print(" " * 23 + "(基于阿里云千问大模型)")
    print("═" * 70)
    print("\n🎯  当前可用 Agent:")
    print("   🤖  [1] 通用问答  - 聊天、知识问答、计算")
    print("   🗺️  [2] 旅行规划  - 行程规划、预算、天气")
    print("   💻  [3] 编程专家  - 代码编写、调试、优化")
    print("\n💡  快速上手:")
    print("   • 直接输入问题即可开始")
    print("   • 输入数字 1/2/3 切换 Agent")
    print("   • 输入 'v' 切换思考过程显示 (开/关)")
    print("   • 输入 'help' 查看帮助 | 'refresh' 刷新知识库 | 'q' 退出")
    print("═" * 70)


def print_help_info(show_verbose: bool):
    """打印详细帮助信息"""
    verbose_status = "✅ 开启" if show_verbose else "❌ 关闭"
    print("\n" + "─" * 70)
    print("📖  使用帮助")
    print("─" * 70)
    print("\n【切换 Agent】")
    print("  1 或 1️⃣    → 切换到通用问答 Agent")
    print("  2 或 2️⃣    → 切换到旅行规划 Agent")
    print("  3 或 3️⃣    → 切换到编程专家 Agent")
    print("\n【常用命令】")
    print("  help       → 📖 显示此帮助信息")
    print("  v          → 👁️ 切换思考过程显示 (当前：{})".format(verbose_status))
    print("  refresh    → 🔄 刷新知识库（更新本地文档后使用）")
    print("  q          → ❌ 退出程序")
    print("\n【使用技巧】")
    print("  ✓ 通用问答适合：日常聊天、百科知识、简单计算")
    print("  ✓ 旅行规划适合：制定计划、查询攻略、预算评估")
    print("  ✓ 编程专家适合：写代码、改 Bug、技术咨询、架构设计")
    print("\n【思考过程显示】")
    print("  • 开启时可查看 AI 的推理过程和工具调用")
    print("  • 关闭时只显示最终回答，界面更简洁")
    print("─" * 70)


def print_agent_switch(agent_name: str, emoji: str):
    """打印 Agent 切换提示"""
    print(f"\n✅ 已切换至 {agent_name} {emoji}")
    print(f"💡 现在可以向{agent_name}提问了！")


def print_error_message(error_msg: str):
    """打印错误提示"""
    print(f"\n❌ 哎呀，出了点问题:")
    print(f"错误信息：{error_msg}")
    print(f"\n💡 建议:")
    print("   • 检查输入是否正确")
    print("   • 尝试简化问题或换个问法")
    print("   • 切换其他 Agent 试试")
    print("   • 如果问题持续，请联系管理员")


def main():
    # 程序启动时预加载 RAG 知识库（只加载一次）
    print("\n🚀 正在启动 Agent 系统...")
    success = initialize_rag_at_startup()

    if success:
        print("✅ 系统就绪！\n")
    else:
        print("⚠️  知识库初始化失败，但基本功能仍可使用\n")

    print_welcome_banner()

    # 默认使用通用问答 Agent
    current_agent = "general"
    # 新增：思考过程显示开关（默认开启）
    show_verbose = True

    while True:
        # 根据当前 Agent 显示提示符
        agent_config = {
            "general": {"prefix": "[通用问答]", "name": "通用问答 Agent", "emoji": "🤖"},
            "travel": {"prefix": "[旅行规划]", "name": "旅行规划 Agent", "emoji": "🗺️"},
            "programming": {"prefix": "[编程专家]", "name": "编程专家 Agent", "emoji": "💻"}
        }

        config = agent_config.get(current_agent, agent_config["general"])
        prefix = f"{config['emoji']} {config['prefix']}"
        agent_name = config["name"]

        # 显示更友好的输入提示
        user_input = input(f"{prefix} 请输入你的问题：").strip()
        # 处理空输入
        if not user_input:
            print("⚠️  输入为空，请输入一些问题或输入 'help' 查看帮助")
            continue

        # 处理特殊命令
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("\n" + "✨" * 35)
            print(" " * 15 + "感谢使用，再见！祝你有美好的一天！🌟")
            print("✨" * 35)
            break

        # 新增：刷新知识库命令
        if user_input.lower() == 'refresh':
            from src.rag.retriever import get_global_knowledge_base
            try:
                kb = get_global_knowledge_base()
                kb.clear_cache()
                get_global_knowledge_base(force_init=True)  # 重新加载
                print("\n🔄 知识库已刷新，最新内容已加载！")
            except Exception as e:
                print(f"\n❌ 刷新失败：{e}")
            continue

        # 支持更多帮助命令别名
        if user_input.lower() in ['h', 'help', '帮助', '?']:
            print_help_info(show_verbose)
            continue
        
        # 切换思考过程显示
        if user_input.lower() == 'v':
            show_verbose = not show_verbose
            status = "✅ 已开启" if show_verbose else "❌ 已关闭"
            print(f"\n👁️ 思考过程显示：{status}")
            print(f"💡 现在使用通用Agent 时会{'显示' if show_verbose else '隐藏'}思考过程")
            continue

        # 切换 Agent
        if user_input in ['1', '1️⃣']:
            current_agent = "general"
            print_agent_switch("通用问答", "🤖")
            continue
        elif user_input in ['2', '2️⃣']:
            current_agent = "travel"
            print_agent_switch("旅行规划", "🗺️")
            continue
        elif user_input in ['3', '3️⃣']:
            current_agent = "programming"
            print_agent_switch("编程专家", "💻")
            continue

        # 处理用户问题
        try:
            # 显示思考状态动画
            loading_messages = [
                f"⏳ {agent_name}正在思考中...",
                f"🧠 {agent_name}分析您的问题...",
                f"💭 {agent_name}准备回答中...",
            ]
            print(f"\n{random.choice(loading_messages)}")
            if current_agent == "general":
                response = run_general_agent(user_input, verbose=show_verbose)
            elif current_agent == "travel":
                response = run_travel_agent(user_input)
            elif current_agent == "programming":
                response = run_programming_agent(user_input)

            # 美化输出格式
            print(f"\n💬 {agent_name}的回答:")
            print(response)
        except Exception as e:
            print_error_message(str(e))


if __name__ == "__main__":
    main()
