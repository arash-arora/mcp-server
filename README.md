# 🤖 MCP Server

This project demonstrates how to build an MCP AI agent
## 🧠 Features

- **Crawl websites** using a local MCP server (BeautifulSoup + markdown conversion).
- **Improve text** via a tool that rewrites bios and personal statements.
- **Combine tools using a single agent**, powered Groq's Qwen model.

---

## 🗂️ Project Structure
|── main.py # Main entrypoint to run the agent
|── servers/
&nbsp;&nbsp;&nbsp; └── crawler_server.py # MCP server to crawl websites and return markdown
&nbsp;&nbsp;&nbsp; └── write_better_server.py # MCP server to improve written text
|── .env # Stores your GROQ_API_KEY
|── README.md


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/arash-arora/mcp-server
cd mcp-server
```

### 2. Install dependencies
```bash 
poetry install
```

### 3. Set your environment variable
- Create an `.env` file with: 
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the MCP Tool Servers
#### Crawl Server
```bash
python servers/crawler_server.py
```
#### Write Better Server
```bash
python servers/write_better_server.py
```

### 5. Run the client
```bash
python client.py
```
The agent will:

Ask the crawler tool to extract content from a website in markdown format.

Ask the write_better tool to improve a short bio.

## 🧩 Tech Stack
🧠 MCP
🌐 BeautifulSoup
✍️ markdownify
⚡ Groq LLM
🔧 LangChain MCP Adapters

