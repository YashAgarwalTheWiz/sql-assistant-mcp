from mcp.server.fastmcp import FastMCP
from database import list_tables,describe_table,run_query,get_history
from nl2sql import convert,explain_query,validate_query,summarize_db,generate_report
import csv
import json

mcp=FastMCP(name='Database Assistant')
current_db = None

@mcp.tool()
def connect_database(db_path:str)->str:
    global current_db
    current_db=db_path
    return f'connected to {db_path}'

@mcp.tool()
def list_tables_mcp():
    """Lists all tables in the currently connected database"""
    res=list_tables(current_db)
    return res

@mcp.tool()
def describe_table_mcp(table_name:str):
    res=describe_table(table_name,current_db)
    return res

@mcp.tool()
def run_query_mcp(sql:str):
    res=run_query(sql,current_db)
    return res

@mcp.tool()
def get_history_mcp():
    res=get_history(current_db)
    return res

@mcp.tool()
def nl_query(question):
    schema=''
    table_names=list_tables(current_db)
    for name in table_names:
        schema+=f'table: {name[0]}\n'
        columns=describe_table(name[0],current_db)
        for col in columns:
            schema+=f'column: {col[1]} ({col[2]})\n'
    
    sql=convert(question,schema)
    return run_query(sql,current_db)

@mcp.tool()
def validate_query_mcp(sql:str)->str:
    """Validates if a SQL query is safe and correct before running it"""
    return validate_query(sql)

@mcp.tool()
def explain_query_mcp(sql: str) -> str:
    """Explains what a SQL query does in plain English"""
    return explain_query(sql)

@mcp.tool()
def export_csv(sql:str,file_path:str)->str:
    """Runs a query and exports results to a CSV file"""
    results=run_query(sql,current_db)
    with open(file_path,'w',newline='') as f:
        writer=csv.writer(f)
        writer.writerows(results)
    return f"Exported to {file_path}"

@mcp.tool()
def export_json(sql,file_path)->str:
    """Runs a query and exports results to a JSON file"""
    results=run_query(sql,current_db)
    with open(file_path,'w') as f:
        json.dump([list(row) for row in results],f)
    return f"Exported to {file_path}"

@mcp.tool()
def summarize_database_mcp():
    schema=''
    table_names=list_tables(current_db)
    for name in table_names:
        schema+=f'table: {name[0]}\n'
        columns=describe_table(name[0],current_db)
        for col in columns:
            schema+=f'column: {col[1]} ({col[2]})\n'

    res=summarize_db(schema)
    return res

@mcp.tool()
def generate_report_mcp(table_name:str):
    results=run_query(f"select * from {table_name} limit 50",current_db)
    schema=describe_table(table_name,current_db)
    return generate_report(table_name,results,schema)

if __name__ == "__main__":
    mcp.run()