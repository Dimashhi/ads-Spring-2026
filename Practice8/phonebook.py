import psycopg2
from config import x
def s():
    t = x()
    u = None
    try:
        u = psycopg2.connect(**t)
        v = u.cursor()
        v.execute("SELECT * FROM search_contacts(%s)", ('John',))
        w = v.fetchall()
        for r in w:
            print(r)

        v.execute("CALL upsert_contact(%s, %s)", ('Alice Smith', '1234567890'))
        
        f = ['Bob', 'Charlie']
        g = ['9876543210', '5556667777']
        v.execute("CALL bulk_insert_contacts(%s, %s, %s)", (f, g, [None]))
        h = v.fetchone()[0]
        print(h)

        v.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (5, 0))
        
        v.execute("CALL delete_contact(%s)", ('Alice Smith',))

        u.commit()
        v.close()
    except Exception as e:
        print(e)
    finally:
        if u:
            u.close()

if __name__ == "__main__":
    s()