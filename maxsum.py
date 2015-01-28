num = int(raw_input("How many number you want to Enter ?: "))
arr=[]
sm=0
maxsum=0
begin=0
end=1
count=0
for i in range(num):
    arr.append(int(raw_input()))

for i in arr:

    if ((begin<end)&(sm==0)&(i>0)):
        begin=count
    sm = max(0,sm+i)
    if (max(sm,maxsum)<>maxsum):
        end =count
    maxsum= max(sm,maxsum)
    count = count + 1
print maxsum
print arr[begin:end+1]
