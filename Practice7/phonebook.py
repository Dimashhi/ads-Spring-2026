import psycopg2
import csv
from config import params

def cn():
    return psycopg2.connect(**params)

def init():
    c = cn()
    cur = c.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pb (
            id SERIAL PRIMARY KEY,
            fn VARCHAR(50),
            pn VARCHAR(20) UNIQUE
        );
    """)
    c.commit()
    cur.close()
    c.close()

def load(f):
    c = cn()
    cur = c.cursor()
    with open(f, 'r', encoding='utf-8') as file:
        r = csv.reader(file)
        next(r)
        for row in r:
            cur.execute("INSERT INTO pb (fn, pn) VALUES (%s, %s) ON CONFLICT DO NOTHING", (row[0], row[1]))
    c.commit()
    cur.close()
    c.close()

def add(a, b):
    c = cn()
    cur = c.cursor()
    try:
        cur.execute("INSERT INTO pb (fn, pn) VALUES (%s, %s)", (a, b))
        c.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        c.close()

def upd(a, b=None, d=None):
    c = cn()
    cur = c.cursor()
    if b:
        cur.execute("UPDATE pb SET fn = %s WHERE fn = %s", (b, a))
    if d:
        cur.execute("UPDATE pb SET pn = %s WHERE fn = %s", (d, a))
    c.commit()
    cur.close()
    c.close()

def get(q):
    c = cn()
    cur = c.cursor()
    cur.execute("SELECT * FROM pb WHERE fn LIKE %s OR pn LIKE %s", (f"%{q}%", f"{q}%"))
    res = cur.fetchall()
    for r in res:
        print(r)
    cur.close()
    c.close()

def rem(x):
    c = cn()
    cur = c.cursor()
    cur.execute("DELETE FROM pb WHERE fn = %s OR pn = %s", (x, x))
    c.commit()
    cur.close()
    c.close()

if __name__ == "__main__":
    try:
        init()
        print("1. Table created successfully!")
        
        add("Dimash", "87071234567")
        print("2. Added Dimash to the phonebook.")
        
        print("3. Searching for Dimash:")
        get("Dimash")
    except Exception as e:
        print(f"Error: {e}")