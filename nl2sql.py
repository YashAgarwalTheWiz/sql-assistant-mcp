from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def convert(question,schema):
    client=Groq(api_key=os.environ.get('GROQ_API_KEY'))

    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role':'system','content':f'''You are a SQL expert. Given a database schema and a question, return ONLY a valid SQL query.explanation, no markdown, just raw SQL.
            Schema: {schema}'''},{'role':'user','content':f'{question}'}
            ]
        )
    return response.choices[0].message.content

def validate_query(sql:str):
    client=Groq(api_key=os.environ.get('GROQ_API_KEY'))

    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role':'system','content':f'''You are a SQL expert. validate the query given to you and only return valid if the query is correct otherwise return the issue found'''},{'role':'user','content':f'{sql}'}
            ]
        )
    return response.choices[0].message.content

def explain_query(sql):
    client=Groq(api_key=os.environ.get('GROQ_API_KEY'))

    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role':'system','content':f'''You are a SQL expert. Explain what the query is trying to do in plain english do not overcomplicate it and try to keep it as simple as possible.'''},{'role':'user','content':f'{sql}'}
            ]
        )
    return response.choices[0].message.content

def summarize_db(db):
    client=Groq(api_key=os.environ.get('GROQ_API_KEY'))

    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role':'system','content':f'''You are a SQL expert. summarize what this database is about, what table exists and what kind of data it holds in plain english and structured format if needed.'''},{'role':'user','content':f'{db}'}
            ]
        )
    return response.choices[0].message.content

def generate_report(table_name,data,schema):
    client=Groq(api_key=os.environ.get('GROQ_API_KEY'))

    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role':'system','content':f'''You are a data analyst. Given a table's schema and sample data, generate a detailed markdown report including:
            - Table overview (what kind of data it holds)
            - Number of rows provided
            - Column breakdown (each column, its type, and what it likely represents)
            - Key observations about the data
            - Any anomalies or interesting patterns noticed

            Keep it clear and structured. Use markdown headings and bullet points.'''},{'role':'user','content':f"Table: {table_name}\nSchema: {schema}\nData: {data}"}
            ]
        )
    return response.choices[0].message.content