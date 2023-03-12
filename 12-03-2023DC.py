'''
The program must accept an alphabet CH as the input. The program must print all the consonants
from CH circularly as the output.
Note: CH is always in lowercase.
Boundary Condition(s):
'a' <= CH <= 'z'
Input Format:
The first line contains CH.
Output Format:
The first line contains all the consonants in lowercase from CH circularly.

Example Input/Output 1:
Input:
w
Output:
wxyzbcdfghjklmnpqrstv
Explanation:
All the lowercase consonants are printed circularly starting from the given alphabet w

Example Input/Output 2:
Input:
e
Output:
fghjklmnpqrstvwxyzbcd
'''

'''Program:'''
#Your code below
p=input().strip()
o="aeiou"
l=[]
for i in range(ord(p),ord("z")+1):
    if chr(i) not in o:
        l.append(chr(i))
for i in range(ord("a"),ord(p)):
    if chr(i) not in o:
        l.append(chr(i))
print(*l,sep="")