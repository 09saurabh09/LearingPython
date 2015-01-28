X= map(int,raw_input().split())
l = len(X)
count=0
i=0
cond=False
last=l-1
k=0
while(k==0):
    if(X[last]>X[last-1]):
        k=1
    else:
        last=last-1

while((i<l-1)&(cond==False)):
    while((X[i])<(X[i+1])&(i+1<l)&(i!=last)):
        i=i+1
    k=(X[i])
    
    while((X[i]<=k)&(i+1<l)&(i!=last)):
        count=count-X[i]+k
        i=i+1
    
    if(i==last):
        cond=True
        
print count
