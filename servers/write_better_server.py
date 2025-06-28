from langchain_groq import ChatGroq
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Grammar")


@mcp.tool()
async def write_better(content: str) -> str:
    """
    Provided the sentence, make the sentence grammatical correct
    """
    model = ChatGroq(model="qwen-qwq-32b")
    response = model.ainvoke(
        {
            "messages": [
                {"role": "user", "content": content},
            ]
        }
    )
    return response


if __name__ == "__main__":
    mcp.run(transport="stdio")
