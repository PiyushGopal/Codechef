from collections import Counter
# cook your dish here
t= int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    leng=len(l)
    c=Counter(l)
    x=c.most_common(1)
    print(leng-x[0][1])
