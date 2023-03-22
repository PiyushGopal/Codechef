# cook your dish here

from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())   
    l=list(map(int,input().split()))
    c=Counter(l)

    a=1
    for j in c:
        if(c[j]%2 !=0):
            a=0
    if(a==1):
        print("YES")
    else:
        print("NO")
