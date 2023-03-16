'''
The program must accept N integers and an integer K as the input. The program must sort those N
integers in ascending order except the integers which are divisible by K. Finally, the program must
print the sorted integers as the output.
Note: The integers which are divisible by K must retain their positions.
Boundary Condition(s):
1 <= N, K <= 1000
1 <= Each integer value <= 10^8
Input Format:
The first line contains the values of N and K separated by a space.
The second line contains N integers separated by space(s).
Output Format:
The first line contains N sorted integers separated by a space.

Example Input/Output 1:
Input:
7 5
65 83 75 92 47 50 19
Output:
65 19 75 47 83 50 92
Explanation:
The integers which are not divisible by 5 are 83, 92, 47 and 19.
The integers which are divisible by 5 are 65, 75 and 50.
So sort the integers which are not divisible by 5 in their positions and also retain the integers which
are divisible by 5 in their same positions.
Hence the output is 65 19 75 47 83 50 92

Example Input/Output 2:
Input:
4 2
90 40 72 46
Output:
90 40 72 46
'''

'''Program:'''
#Your code below
n,m=map(int,input().split())
l=list(map(int,input().split()))
k=[]
j=[]
t=0
for i in range(n):
    if l[i]%m!=0:
        k.append(l[i])
k.sort()
for i in range(n):
    if l[i]%m==0:
        j.append(l[i])
    elif l[i]%m!=0:
        j.append(k[t])
        t+=1
print(*j)