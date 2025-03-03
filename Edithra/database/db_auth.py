# Authentication Database Setup
import os
from Edithra.database.db_connection import get_db_connection

def create_auth_table():
    """Creates the users table if it doesn't exist"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_auth_table()




