from langchain_groq import ChatGroq
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Grammar")


@mcp.tool()
async def write_better(content: str) -> str:
    """
    Provided the content, return the better version of it
    """
    model = ChatGroq(model="qwen-qwq-32b")
    response = model.ainvoke(
        {
            "messages": [
                {"role": "system", "content": "Provided the sentence, write it better"},
                {"role": "user", "content": content},
            ]
        }
    )
    return response


if __name__ == "__main__":
    mcp.run(transport="stdio")
