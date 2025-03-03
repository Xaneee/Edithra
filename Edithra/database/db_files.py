# File Storage Database
from Edithra.database.db_connection import get_db_connection

def create_file_table():
    """Creates the files table if it doesn't exist"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id SERIAL PRIMARY KEY,
            filename TEXT UNIQUE NOT NULL,
            storage_url TEXT NOT NULL
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_file_table()




