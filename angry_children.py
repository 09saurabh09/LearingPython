n=int(raw_input())
k=int(raw_input())

data=[]
diff=[]
ans=[]

for i in range(n):
    data.append(int(raw_input()))

data.sort()

for i in range(n-k+1):
    di=data[k+i-1]-data[i]
    ans.append(di)

#for i in range(n-1):
#    diff.append(data[i+1]-data[i])

#for i in range(n-k+1):
#    sm=0
#    for j in range(k-1):
#        sm=sm+diff[i+j]
#
#    ans.append(sm)

#cumsum=diff[0:k]
#len_diff=len(diff)

#for i in range(len_diff-k):
#    cumsum.append(cumsum[i+k-1]+diff[i+k])

#mn=min(ans)
#final=ans.index(mn)
#print data[final+k-1]-data[final]
#print cumsum                  
