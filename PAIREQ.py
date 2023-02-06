''' Chef has an array 
�
A of length 
�
N.

In one operation, Chef can choose any two distinct indices 
�
,
�
i,j 
(
1
≤
�
,
�
≤
�
,
�
≠
�
)
(1≤i,j≤N,i=j) and either change 
�
�
A 
i
​
  to 
�
�
A 
j
​
  or change 
�
�
A 
j
​
  to 
�
�
A 
i
​
 .

Find the minimum number of operations required to make all the elements of the array equal.

Input Format
First line will contain 
�
T, number of test cases. Then the test cases follow.
First line of each test case consists of an integer 
�
N - denoting the size of array 
�
A.
Second line of each test case consists of 
�
N space-separated integers 
�
1
,
�
2
,
…
,
�
�
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
  - denoting the array 
�
A.
Output Format
For each test case, output the minimum number of operations required to make all the elements equal. 
'''

from collections import Counter
t=int(input())
for i in range(t):
    r=int(input())
    l=list(map(int, input().split()))
    #this returns distinct elements in a list with thier frequency
    m = Counter(l)
    #and this will return the frequency of the most occuring element.
    k = m.most_common()[0][1]
    answer=len(l)-k
    print(answer)
