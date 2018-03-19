import select


while 1:
    try:
        conn, addr = s.accept()
    except OSError as e:
        pass
    else:
        print("Получен запрос на соединение от {}".format(str(addr)))
        clients.append(conn)
    finally:
        wait = 0
        r = []
        w = []
        try:
            r, w, e = select.select(cliets, clients, [], wait)
            print(w, r)
        except:
            pass
