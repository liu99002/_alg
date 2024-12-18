def perm(x):
    p=[]
    re(x,p)

def re(x,p):
    i=len(p)
    if i==x:
        print(p)
        return
    for y in range(x):
        if not y in p:
            p.append(y)
            re(x,p)
            p.pop()
perm(4)