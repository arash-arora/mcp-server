import os
from bs4 import BeautifulSoup
import requests
from mcp.server.fastmcp import FastMCP
from markdownify import markdownify as md
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(place: str) -> str:
    """
    Get the weather of a place

    Input: place
    Output: weather of that place
    """
    location_response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=1&appid=ddbe99c3933f2c5a54e8af79887bcd64"
    )
    location_response.raise_for_status()
    location = location_response.json()
    lat, long = location[0]["lat"], location[0]["lon"]

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": f"{lat},{long}"}

    api_key = os.getenv("WEATHER_API_KEY")
    headers = {
        "x-rapidapi-key": api_key
        or "fd2e7104f1msh31526e216ca2bf5p1f4d3bjsn7c32e0c0599e",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    return str(response.json())


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
    mcp.run(transport="streamable-http")
