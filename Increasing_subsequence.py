n=int(raw_input("Enter number of elements:"))
print "Enter Elements"
num=[]
maxi=0
for i in range(n):
    num.append(int(raw_input()))


L=[1]

for i in range(1,n):
    for j in range(i):
        if ((num[j]<num[i])&(L[j]>maxi)):
            maxi=L[j]
            

    L.append(1 + maxi)
    maxi=0

print max(L)    
