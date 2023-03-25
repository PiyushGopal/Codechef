# cook your dish here
from collections import Counter
from math import *
t=int(input())
for i in range(t):
    s=input()
    if(len(s)%2 !=0):
        sa=s[:floor(len(s)/2)]
        sb=s[floor(len(s)/2)+1:]
    else:
        sa=s[:len(s)//2]
        sb=s[len(s)//2:]

    saa=dict(Counter(sa))
    sbb=dict(Counter(sb))
    flag=0
    for i in saa:
        if i in sbb.keys():
            if(saa[i]==sbb[i]):
                flag=1 
            else:
                flag=0
                break
        else:
            flag=0
            break
    if flag==1:
        print("YES")
    else:
        print("NO")
            
    
