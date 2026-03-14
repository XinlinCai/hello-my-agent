from src.agents.my_agent import run_agent


def main():
    print("欢迎使用我的第一个 Agent(基于千问模型)")
    while True:
        user_input = input("\n请输入你的问题(输入 'exit' 退出): ")
        if user_input.lower() == 'exit':
            break
        try:
            response = run_agent(user_input)
            print(f"Agent 回答: {response}")
        except Exception as e:
            print(f"发生错误: {e}")


if __name__ == "__main__":
    main()
