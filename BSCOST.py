t=int(input())
for i in range(t):
    n,x,y=map(int, input().split())
    a=input()
    if(a.count('0')==n):
        print('0')
    elif(a.count('1')==n):
        print('0')
    else:
        print(min(x,y))
