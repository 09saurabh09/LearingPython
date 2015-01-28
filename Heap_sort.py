import math

data1 = raw_input(" Enter elements for heapsort:")
data1=data1.split(" ")
data=[]
heap=[]
output=[]
a=0
cond=True

for i in range (len(data1)):
    data.append(int(data1[i]))


def heapify(data):
    heap.append(data[0])
    for j in range (1, len(data)):
        heap.append(data[j])
        kk=j
      
        while(kk>0):
            p = int(math.floor(((kk-1)/2)))
            
            if ( heap[kk]<heap[p]):
                heap[kk],heap[p]=heap[p],heap[kk]
                kk=p
            else:
                kk=0

    return heap        


def heap_sort(data):
    
    while(len(data)!=0):
        a= len(data)-1
        data[0],data[a]=data[a],data[0]
        output.append(data.pop())
        cond=True
        k=0
        i=0
        while((cond) & (2*k+2<len(data))):
            
            if (((int(data[k])<int(data[2*k+1]))& (int(data[k]<data[2*k+2])))):
                cond=False

            elif ((int(data[2*k+1])<=int(data[2*k+2]))&(cond==True)):
                data[k],data[2*k+1]=data[2*k+1],data[k]
                k=2*k+1

            elif ((int(data[2*k+1])>int(data[2*k+2]))&(cond==True)):
                data[k],data[2*k+2]=data[2*k+2],data[k]
                k=2*k+2

                
            else:
                cond=True
                
                
heap_data=heapify(data)        
heap_sort(heap_data)
print output
