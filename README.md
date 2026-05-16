# 🗄️ SQL Assistant MCP Server

A powerful MCP (Model Context Protocol) server that connects Claude Desktop to any SQLite database. Ask questions in plain English, run queries, generate reports, export data, and more — all through natural conversation with Claude.

---

## ✨ Features

- **Natural Language to SQL** — Ask questions in plain English, get SQL executed automatically
- **Query Validation** — LLM checks if a query is safe and correct before running it
- **Query Explainer** — Understand what any SQL query does in plain English
- **Database Summarizer** — Auto-explore and summarize any connected database
- **Report Generator** — Generate detailed markdown reports with stats and observations for any table
- **Query History** — Every query is logged and retrievable
- **Export to CSV/JSON** — Save query results to files instantly
- **Multi-Database Support** — Connect to any SQLite file dynamically at runtime
- **Schema-Aware** — LLM reads your full schema before generating SQL, no hallucinated column names

---

## 🛠️ Tools Exposed via MCP

| Tool | Description |
|------|-------------|
| `connect_database` | Connect to any SQLite database by file path |
| `list_tables_mcp` | List all tables in the connected database |
| `describe_table_mcp` | Show schema of a specific table |
| `run_query_mcp` | Execute any SQL query |
| `nl_query` | Convert natural language to SQL and execute it |
| `validate_query_mcp` | Validate if a SQL query is safe and correct |
| `explain_query_mcp` | Explain what a SQL query does in plain English |
| `get_history_mcp` | Retrieve the last 10 executed queries |
| `summarize_database_mcp` | Summarize the entire database structure and purpose |
| `generate_report_mcp` | Generate a detailed markdown report for a table |
| `export_csv` | Export query results to a CSV file |
| `export_json` | Export query results to a JSON file |

---

## 🏗️ Architecture

```
Claude Desktop (MCP Client)
        ↓
MCP Server (server.py)
        ↓
┌───────────────────────────┐
│  database.py              │  → SQLite operations
│  nl2sql.py                │  → Groq LLM (NL2SQL, validate, explain, report)
└───────────────────────────┘
        ↓
SQLite Database (.db file)
```

---

## 📁 Folder Structure

```
sql-assistant-mcp/
├── server.py              # MCP server — all 12 tools defined here
├── database.py            # SQLite operations (connect, query, history)
├── nl2sql.py              # Groq LLM helpers (convert, validate, explain, report)
├── sample_db/
│   ├── create_sample.py   # Script to generate sample database
│   └── sample.db          # Sample SQLite database (employees + projects)
├── .env                   # API keys (not committed)
├── .gitignore
└── requirements.txt
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YashAgarwalTheWiz/sql-assistant-mcp.git
cd sql-assistant-mcp
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Create the sample database (optional)
```bash
cd sample_db
python create_sample.py
```

### 5. Connect to Claude Desktop
Add this to your `claude_desktop_config.json`:

**Windows:** `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`

**Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sql-assistant": {
      "command": "python",
      "args": ["path/to/sql-assistant-mcp/server.py"]
    }
  }
}
```

> **Note:** If using a virtual environment, replace `"python"` with the full path to your venv Python executable.

### 6. Restart Claude Desktop
Fully quit and reopen Claude Desktop. You should see the 🔨 hammer icon indicating tools are connected.

---

## 💬 Example Prompts

Once connected in Claude Desktop:

```
Connect to my database at /path/to/your/database.db
```
```
List all tables in my database
```
```
Show me all employees in the Engineering department
```
```
What is the average salary by department?
```
```
Generate a report for the employees table
```
```
Export all active projects to C:\Users\Desktop\projects.csv
```
```
Explain this query: SELECT * FROM employees WHERE salary > 80000
```
```
Summarize my database
```

---

## 🧠 How Natural Language to SQL Works

1. Claude receives your natural language question
2. MCP server fetches the full database schema (all tables + columns)
3. Schema + question sent to Groq (`llama-3.3-70b-versatile`)
4. LLM returns a raw SQL query
5. Query executed on your SQLite database
6. Results returned to Claude for presentation

Schema-aware by design — the LLM always sees your actual schema first so it never hallucinates column names.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| MCP Framework | `mcp` Python SDK (FastMCP) |
| LLM | Groq (`llama-3.3-70b-versatile`) |
| Database | SQLite |
| Client | Claude Desktop |

---

## 👤 Author

**Yash Agarwal**
Fresher @ TCS | ML/AI Engineer in progress
[GitHub](https://github.com/YashAgarwalTheWiz)
