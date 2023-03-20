'''Chef usually likes to play cricket, but now, he is bored of playing it too much, so he is trying new games with strings. Chef's friend Dustin gave him binary strings 
�
S and 
�
R, each with length 
�
N, and told him to make them identical. However, unlike Dustin, Chef does not have any superpower and Dustin lets Chef perform only operations of one type: choose any pair of integers 
(
�
,
�
)
(i,j) such that 
1
≤
�
,
�
≤
�
1≤i,j≤N and swap the 
�
i-th and 
�
j-th character of 
�
S. He may perform any number of operations (including zero). '''
#SOLUTION
t=int(input())
for i in range (t):
    n=int(input())
    s=input()
    r=input()
    if(s.count('1')==r.count('1')):
        print("YES")
    else:
        print("NO")
            
