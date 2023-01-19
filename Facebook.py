'''A post on facebook is said to be more popular if the number of likes on the post is strictly greater than the number of likes on some other post.
In case the number of likes is same, the post having more comments is more popular.
Given arrays 
�
A and 
�
B, each having size 
�
N, such that the number of likes and comments on the 
�
�
ℎ
i 
th
  post are 
�
�
A 
i
​
  and 
�
�
B 
i
​
  respectively, find out which post is most popular.

It is guaranteed that the number of comments on all the posts is distinct.
'''

#piyushgopal

# cook your dish here
t=int(input())
for i in range(t):
    a= int(input())
    l=list(map(int, input().split()))
    c=list(map(int, input().split()))
    z=[]
    ml=max(l)
    mc=0
    if((l.count(ml)>1)):
        for j in range(len(l)):
            if(l[j]==ml):
                z.append(j)
        for x in range(len(z)):
            if(c[z[x]] > mc):
                mc=c[z[x]]
        print((c.index(mc))+1)    
    else:
        print((l.index(ml))+1)
            
