'''
The program must accept an integer P which represents the price of an item in a supermarket as
the input. The program must print the discount amount for P up to 2 decimal places based on the
following conditions,
- If the price is less than or equal to Rs. 1000 then 10 percentage discount is applied.
- Else if the price is greater than Rs. 1000 then 10 percentage discount is applied up to Rs. 1000
and 5 percentage discount is applied for the remaining price amount.
Boundary Condition(s):
1 <= P <= 99999999
Input Format:
The first line contains the value of P.
Output Format:
The first line contains the discount price up to 2 decimal places.

Example Input/Output 1:
Input:
852
Output:
85.20

Example Input/Output 2:
Input:
1543
Output:
127.15
'''

'''Program:'''
#Your code below
n=int(input())
if n<1000:
    d=n*0.1
else:
    d=1000*0.1+(n-1000)*0.05
print("{:.2f}".format(d))
