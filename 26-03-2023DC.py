'''
The program must accept a string S as the input. The program must print the alphabets in S
which have both uppercase and lowercase alphabets in S as the output. The alphabets must be
printed in the same order as given in the input. 
Note: There will be at least one alphabet with both uppercase and lowercase letters in S.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains alphabets as per the condition.
Example Input/Output 1:
Input:
aeroRadeOnoWe
Output:
roROo
Explanation:
The alphabets r and o are present in both uppercase and lowercase so they are printed.
Example Input/Output 2:
Input:
ImpeccAbleCitrus
Output:
IccCi
'''

'''Program:'''
#Your code below
n=input().strip()
for i in n:
    if i.isupper() and i.lower() in n:
        print(i,end="")
    elif i.islower() and i.upper() in n:
        print(i,end="")