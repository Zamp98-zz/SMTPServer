import user

def loadUsers(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        out =[]
        for line in lines:
            t = line.replace('<', '')
            t = t.replace('>', '')
            out.append(t)
        users = []
        for line in out:
            u = user.User(line.replace('\n', ''))
            users.append(u)
        f.close()
        return users
    except:
        print("Arquivo ",filename," não encontrado")
        return []