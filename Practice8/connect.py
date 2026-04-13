import psycopg2
from config import x
def k():
    l = None
    try:
        m = x()
        l = psycopg2.connect(**m)
        n = l.cursor()
        n.execute('SELECT version()')
        o = n.fetchone()
        print(o)
        n.close()
    except (Exception, psycopg2.DatabaseError) as p:
        print(p)
    finally:
        if l is not None:
            l.close()
if __name__ == '__main__':
    k()