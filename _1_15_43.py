sum=0

for f in [0,5]:
    for d in [0,2,4,6,8]:
        if d==f:
            continue
        for c in range(0,10):
            if (c==f)or(c==d):
                continue
            for e in range(0,10):
                if (e==f)or(e==d)or(e==c):
                    continue
                if ((c*100+d*10+e)%3)!=0:
                    continue
                for g in range(0,10):
                    if (g==f)or(g==d)or(g==c)or(g==e):
                        continue
                    if ((e*100+f*10+g)%7)!=0:
                        continue
                    for h in range(0,10):
                        if (h==f)or(h==d)or(h==c)or(h==e)or(h==g):
                            continue
                        if ((f*100+g*10+h)%11)!=0:
                            continue
                        for i in range(0,10):
                            if (i==f)or(i==d)or(i==c)or(i==e)or(i==g)or(i==h):
                                continue
                            if ((g*100+h*10+i)%13)!=0:
                                continue
                            for j in range(0,10):
                                if (j==f)or(j==d)or(j==c)or(j==e)or(j==g)or(j==h)or(j==i):
                                    continue
                                if ((h*100+i*10+j)%17)!=0:
                                    continue
                                for a in range(1,10):
                                    if (a==c)or(a==d)or(a==e)or(a==f)or(a==g)or(a==h)or(a==i)or(a==j):
                                        continue
                                    b=45-a-c-d-e-f-g-h-i-j
                                    number=(10**9)*a+(10**8)*b+(10**7)*c+(10**6)*d+(10**5)*e+(10**4)*f+(10**3)*g+(10**2)*h+(10**1)*i+j
                                    print(number)
                                    sum=sum+number

print(sum)