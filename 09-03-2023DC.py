'''
The program must accept an integer N as the input. The program must remove the digits of N  in
odd positions if N is odd. Else the program must remove the digits in even positions of N. Finally,
the program must print the modified N as the output.
Boundary Condition(s):
1 <= N <= 10^18
Input Format:
The first line contains N.
Output Format:
The first line contains the modified N.

Example Input/Output 1:
Input:
245872
Output:
257
Explanation:
245872 is an even integer so all the digits at even positions are removed to get 257.

Example Input/Output 2:
Input:
1009
Output:
9
'''

'''Program:'''
n=input().strip()
m=''
if int(n)%2==0:
    for i in range(0,len(n),2):
        m+=n[i]
    print(m)
else:
    print(int(n[1:len(n):2]))