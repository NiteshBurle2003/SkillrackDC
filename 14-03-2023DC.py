'''
The program must accept a URL (Uniform Resource Locator) as the input. The program must print
the top-level domain of the URL as the output.
Note: The URL always starts with either http or https.
Boundary Condition(s):
15 <= Length of URL <= 1000
Input Format:
The first line contains the URL.
Output Format:
The first line contains the top-level domain of the URL.

Example Input/Output 1:
Input:
http://www.skillrack.com
Output:
.com
Explanation:
The top-level domain of the URL http://www.skillrack.com is .com
Hence the output is .com

Example Input/Output 2:
Input:
https://www.amazon.co.in
Output:
.in
Example Input/Output 3:
Input:
http://www.skillrack.com/solve/8464
Output:
.com
'''


'''Program:'''
#Your code below
p=input().strip()
d=p.split('//')[-1].split('/')[0]
d1=d.split('.')
print('.'+d1[-1])