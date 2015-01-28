import math
n = int(raw_input())
k = int(raw_input())

maxx=[1]*10
num=9
numbers=[0,9]
ans=[]
for i in range(1,n):
    num=pow(10,i)*9 +num
    numbers.append(num)
    

for i in range(1,k+1):
    maxx[i]=maxx[i-1]*9


while(cond==True):
    
    if(maxx[k]<num):
        ans.append(maxx[k])
    else:
        k=k-1
        num=math.floor(num/2)
    
