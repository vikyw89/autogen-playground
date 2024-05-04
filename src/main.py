import autogen
from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio

llm_config = {"model": "gpt-4-turbo", "api_key": os.environ["OPENAI_API_KEY"]}


async def main():
    with autogen.coding.DockerCommandLineCodeExecutor(
        work_dir="coding"
    ) as code_executor:
        assistant = AssistantAgent("assistant", llm_config=llm_config)
        user_proxy = UserProxyAgent(
            "user_proxy", code_execution_config={"executor": code_executor}
        )

        # Start the chat
        user_proxy.initiate_chat(
            assistant,
            message="Plot a chart of NVDA and TESLA stock price change YTD. Save the plot to a file called plot.png",
        )


if __name__ == "__main__":
    
    
    asyncio.run(main())
