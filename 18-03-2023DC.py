'''
The program must accept the shape and dimensions of N objects as the input. The program must
print the sum of the area of all the objects as the output. The shape can be square or rectangle.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains N.
The next N lines contain the shape followed by dimension(s) side for square and length and
breadth for rectangle separated by a space.
Output Format:
The first line contains the sum of the area of all the objects.

Example Input/Output 1:
Input:
4
square 5
rectangle 4 2
rectangle 3 10
square 11
Output:
184
Explanation:
The first object is square it's area is 5*5 = 25. The total area is 25.
The second object is rectangle it's area is 4*2 = 8. The total area is 33.
The third object is rectangle it's area is 3*10 = 30. The total area is 63.
The fourth object is square it's area is 11*11 = 121. The total area is 184.

Example Input/Output 2:
Input:
6
square 25
rectangle 17 24
square 5
rectangle 40 12
square 34
square 48
Output:
4998
'''

'''Program:'''
#Your code below
m=int(input())
d=[]
u=0
for i in range(m):
    l=list(map(str,input().split()))
    if l[0]=="square":
        c=int(l[1])*int(l[1])
        d.append(c)
    else:
        c=int(l[1])*int(l[2])
        d.append(c)
for i in d:
    u+=i
print(u)