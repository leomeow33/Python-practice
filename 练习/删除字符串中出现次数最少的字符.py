while True:
    try:
        new = ''
        ss = input()
        tmp = []
        for s in ss:
            tmp.append(int(ss.count(s)))
        min_ = min(tmp)
        for i in range(len(ss)):
            if ss.count(ss[i]) > min_:
                new += ss[i]
        print(new)
    except:
        break