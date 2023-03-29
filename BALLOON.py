# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ans=[1,2,3,4,5,6,7]
    count=0
    for j in range(len(l)):
        if l[j] in ans:
            count+=1
        if count==7:
            print(j+1)
            break
            
