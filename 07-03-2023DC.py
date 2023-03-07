c=int(input())
k=list(map(str,input().split()))
o=int(input())
b=[]
for i in range(c):
    b.append(k[i][-o])
b1=max(b)
b2=b.index(b1)
print(k[b2])