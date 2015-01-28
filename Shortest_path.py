n= int(raw_input("Enter matrix size:"));

data=[]
d=[9999]
Matrix=[]
l=[0,0]
l1=[0,0]
nabor=[]
s=0
Dist=[]

for i in range(n):
    Dist.append(d*n)
    data.append(raw_input())
    Matrix.append(data[i].split(" "))

    
nabor.append(l)
Dist[0][0]=0

for nab in nabor:
    if(s<n*n):
        
        l1=[nab[0],nab[1]]
        l=[nab[0],nab[1]+1]
        if(l[1]<n):
            
            if((Dist[l[0]][l[1]]==9999)&(Matrix[l[0]][l[1]]=='1')):
                nabor.append(l)
                Dist[l[0]][l[1]]=Dist[l1[0]][l1[1]]+1

        l=[nab[0],nab[1]-1]
        if((Dist[l[0]][l[1]]==9999)&(Matrix[l[0]][l[1]]=='1')&(l[1]>=0)):
            nabor.append(l)
            Dist[l[0]][l[1]]=Dist[l1[0]][l1[1]]+1

        l=[nab[0]-1,nab[1]]
        if((Dist[l[0]][l[1]]==9999)&(Matrix[l[0]][l[1]]=='1')&(l[0]>=0)):
            nabor.append(l)
            Dist[l[0]][l[1]]=Dist[l1[0]][l1[1]]+1

        l=[nab[0]+1,nab[1]]
        if(l[0]<n):
            
            if((Dist[l[0]][l[1]]==9999)&(Matrix[l[0]][l[1]]=='1')):
                nabor.append(l)
                Dist[l[0]][l[1]]=Dist[l1[0]][l1[1]]+1
        

        s=s+1
        
