import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP
from markdownify import markdownify as md

mcp = FastMCP("Crawler")


@mcp.tool(description="A tool to crawl the website")
async def crawl(url: str) -> str:
    """
    Crawls a website
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Optional: remove script/style elements
    for tag in soup(["script", "style"]):
        tag.decompose()

    html_content = str(soup)
    markdown_content = md(html_content, heading_style="ATX")
    return markdown_content.strip() if markdown_content else "No content found."


if __name__ == "__main__":
    mcp.run("streamable-http")
