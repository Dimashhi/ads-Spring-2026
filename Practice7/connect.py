import psycopg2
from config import params

def get_db():
    try:
        c = psycopg2.connect(**params)
        return c
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    conn = get_db()
    if conn:
        print("Connected!")
        conn.close()