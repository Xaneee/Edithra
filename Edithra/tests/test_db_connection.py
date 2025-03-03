# Database Connection Tests
from Edithra.database.db_connection import get_db_connection

def test_db_connection():
    """Tests database connection"""
    try:
        conn = get_db_connection()
        assert conn is not None
        conn.close()
    except Exception:
        assert False




