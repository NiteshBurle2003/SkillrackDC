'''
The program must accept two string values S1, S2 and an integer X as the input. The program
must print first X characters in the string S1 and then the program must print last X characters in
the string S2 as the output.
Boundary Condition(s):
1 <= Length of S1, S2 <= 100
1 <= X <= Length of S1, S2
Input Format:
The first line contains the string S1.
The second line contains the string S2.
The third line contains the integer X.
Output Format:
The first line contains 2*X characters.
Example Input/Output 1:
Input:
coconutTree
banana
4
Output:
coconana
Explanation:
The first 4 characters in the string coconutTree are coco.
The last 4 characters in the string banana are nana.
Hence the output is coconana
Example Input/Output 2:
Input:
encourage
victory
3
Output:
encory
'''

'''Program:'''
f1 = input().strip()
f2 = input().strip()
x = int(input().strip())
f = f1[:x]
l = s2[-x:]
r = f + l
print(result)