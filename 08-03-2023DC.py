'''The program must accept N filenames with extension and an extension E as the input. The program
must print the filename which has the largest length with the extension E among the N filenames
as the output. If more than one filename has the same largest length with the extension E then
print the first occurring one as the output. If there is no file with the extension E then the program
must print FILE NOT FOUND as the output.
Note: All the alphabets in each extension are always lower case.
Boundary Condition(s):
1 <= N <= 100
1 <= Length of each filename with the extension <= 100
1 <= Length of the extension E <= 10
Input Format:
The first line contains the value of N.
The next N lines each contain a filename.
The (N+2)th
line contains the extension E.
Output Format:
The first line contains the filename based on the given conditions or FILE NOT FOUND.


Example Input/Output 1:
Input:
5
addTwoNumbers.c
removeVowels.java
stringExpansion.c
arrayRotation.cpp
main.c
.c
Output:
stringExpansion.c
Explanation:
The filenames with the give extension .c are addTwoNumbers, stringExpansion and main.
So the filename with the largest length among those filenames is stringExpansion.
Hence the output is stringExpansion.c


Example Input/Output 2:
Input:
4
markSheet.pdf
myRingTone.mp3
nature.png
myAadhaar.pdf
.xlsx
Output:
FILE NOT FOUND
'''


'''Program:'''
a=int(input())
l=[]
v=[]
v1=[]
for i in range(a):
    l.append(input().strip())
b=input().strip()
for i in range(len(l)):
    c=l[i][-len(b):]
    if c==b:
        v.append(l[i])
        v1.append(len(l[i]))
if len(v1)!=0:
    z=max(v1)
    z1=v1.index(z)
    print(v[z1])
else:
    print("FILE NOT FOUND")