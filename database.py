import sqlite3
from datetime import datetime

def connect(db_path:str):
    connection=sqlite3.connect(db_path)
    cursor=connection.cursor()
    return connection,cursor

def list_tables(db_path):
    connection,cursor=connect(db_path=db_path)
    res=cursor.execute("select name from sqlite_master where type='table'").fetchall()
    connection.close()
    return res

def describe_table(table_name,db_path):
    connection,cursor=connect(db_path=db_path)
    res=cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
    connection.close()
    return res

def save_history(sql,result,db_path):
    connection,cursor=connect(db_path=db_path)
    cursor.execute('''
        create table if not exists query_history (
                id integer primary key AUTOINCREMENT,
                query text,
                result text,
                timestamp date
            )
    ''')
    cursor.execute('''
        Insert into query_history (query,result,timestamp) values (?,?,?)
    ''',(sql,result,datetime.now()))
    connection.commit()
    connection.close()

def run_query(sql,db_path):
    connection,cursor=connect(db_path)
    results=cursor.execute(sql).fetchall()
    save_history(sql,str(results),db_path)
    connection.commit()
    connection.close()
    return results

def get_history(db_path):
    connection,cursor=connect(db_path)
    results=cursor.execute('select * from query_history order by id desc limit 10').fetchall()
    connection.close()
    return results