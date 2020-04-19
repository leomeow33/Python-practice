a = [0,1]
count = 0
que = [0]*10
tip = [10,20,30,40,50,60,70,80,90,100]
sum = 0
res = []
for b in a:
    for c in a:
        for d in a:
            for e in a:
                for f in a:
                    for g in a:
                        for h in a:
                            for i in a:
                                for j in a:
                                    for k in a:
                                        que[0] = b
                                        que[1] = c
                                        que[2] = d
                                        que[3] = e
                                        que[4] = f
                                        que[5] = g
                                        que[6] = h
                                        que[7] = i
                                        que[8] = j
                                        que[9] = k
                                        for l in range(10):
                                            if que[l] == 1:
                                                sum += tip[l]
                                                res.append(l+1)
                                        if sum == 100:
                                            print(''.join(str(m) for m in res))
                                        res.clear()
                                        sum = 0
