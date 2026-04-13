import configparser
def x(y='database.ini', z='postgresql'):
    a = configparser.ConfigParser()
    a.read(y)
    b = {}
    if a.has_section(z):
        c = a.items(z)
        for d in c:
            b[d[0]] = d[1]
    else:
        raise Exception(f'Section {z} not found in {y}')
    return b