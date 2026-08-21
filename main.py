from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("Hello from ai-agent-langraph!")


if __name__ == "__main__":
    print(os.getenv("OPENAI_API_KEY"))
    main()
