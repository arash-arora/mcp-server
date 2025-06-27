import os
import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "crawler": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
            "write_better": {
                "command": "python",
                "args": ["servers/write_better_server.py"],
                "transport": "stdio",
            },
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)

    crawl_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Crawl the website: https://arasharora.com",
                }
            ]
        }
    )
    print("Crawler response:", crawl_response["messages"][-1].content)

    write_better_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "I am Leo, working as a data scientist at Google. I love plahying games and a workaholic",
                }
            ]
        }
    )
    print("Write it better response:", write_better_response["messages"][-1].content)


asyncio.run(main())
