# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    ins=[]
    for j in range(len(x)-1):
        if x[j] != x[j+1]:
            ins.append(j)
            ins.append(j+1)
    s=set(ins)
    print(len(s))
    
    
