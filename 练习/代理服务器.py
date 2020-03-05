while True:
    try:
        p = []
        s = []
        n = int(input())
        for i in range(n):
            p.append(input())
        m = int(input())
        for i in range(m):
            s.append(input())
        if n == 1 and p[0] in s:
            print('-1')
            continue
        used = []
        count = 0
        for item in s:
            if item in used:
                continue
            if item in p:
                used.append(item)
                if set(used) == set(p):
                    used =[]
                    used.append(item)
                    count += 1
        print(count)
    except:
        break
