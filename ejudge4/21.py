import importlib
def s():
    k = int(input())
    for _ in range(k):
        try:
            line = input().split()
            m_path, a_name = line[0], line[1]
            try:
                m = importlib.import_module(m_path)
            except ImportError:
                print("MODULE_NOT_FOUND")
                continue
            if not hasattr(m, a_name):
                print("ATTRIBUTE_NOT_FOUND")
            else:
                attr = getattr(m, a_name)
                if callable(attr):
                    print("CALLABLE")
                else:
                    print("VALUE")
        except EOFError:
            break
s()