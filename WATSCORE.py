'''You are participating in a contest which has 
11
11 problems (numbered 
1
1 through 
11
11). The first eight problems (i.e. problems 
1
,
2
,
…
,
8
1,2,…,8) are scorable, while the last three problems (
9
9, 
10
10 and 
11
11) are non-scorable ― this means that any submissions you make on any of these problems do not affect your total score. '''

# SOLUTION

# cook your dish here
t=int(input())
for i in range(t):
    d={}
    n=int(input())
    for j in range(n):
        x,y=map(int,input().split())
        if(x in d):
            d[x].append(y)
        else:
            d[x]=[y]
    sum=0
    prob = [1,2,3,4,5,6,7,8]
    for j in d:
        if(j in prob):
            sum+=max(d[j])
    print(sum)
