'''
The program must accept a string S as the input. The program must reverse the characters
between the first occuring consonant and the last occuring consonant (inclusive of both the
consonants) in the string. Then the program must print the modified string as the output.
Note: At least two consonants will be present in the string S.
Boundary Condition(s):
2 <= Length of S <= 1000
Input Format:
The first line contains the string S.
Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
aroma
Output:
amora
Explanation:
The first occurring consonant is r.
The last occurring consonant is m.
So "rom" is reversed as "mor".
Hence the output is amora

Example Input/Output 2:
Input:
aEilkjOpqrstuAe
Output:
aEitsrqpOjkluAe
'''

'''Program:'''
#Your code below
def rev(p):
    v=set('aeiouAEIOU')
    s, e= None, None
    for i,c in enumerate(p):
        if c.isalpha() and c not in v:
            if s is None:
                s=i
            e=i
    return p[:s]+p[s:e+1][::-1]+p[e+1:]
p=input()
print(rev(p))