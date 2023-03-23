'''
The program must accept N integers and an integer X as the input. The program must add X with
the even integers among N integers and subtract X from the odd integers among N integers.
Finally, the program must print the modified values of N integers as the output.
Boundary Condition(s):
1 <= N, X <= 1000
Input Format:
The first line contains an Integer N.
The second line contains the N integers separated by a space.
The third line contains the integer X.
Output Format:
The first line contains the modified N integers separated by a space(s).

Example Input/Output 1:
Input:
5
12 23 34 55 56
3
Output:
15 20 37 52 59
Explanation:
The even integers are 12 34 and 56. So add 3 with these even integers (15, 37, 59). 
The odd integers are 23 and 55. So subtract 3 with these odd integers (20, 52).
Hence the output is 15 30 37 52 59

Example Input/Output 2:
Input:
7
1 2 3 4 5 6 7
4
Output:
-3 6 -1 8 1 10 3
'''

'''Program:'''
#Your code below
n=int(input())
l=list(map(int,input().split()))
p=int(input())
for i in range(n):
    if l[i]%2==0:
        print(l[i]+p,end=" ")
    else:
        print(l[i]-p,end=" ")