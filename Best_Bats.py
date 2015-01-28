import math
cases = int(raw_input("Enter number of test cases: "))
ans=0
list = [0] * 11
list1 =[0]*11
list2 = [0]*11
a=0
b=0
for i in range(cases):
    for j in range(11):
        list[j]=int(raw_input(""))

    list.sort()

    k= int(raw_input("Enter value of k:"))
    list1=list[-k:]
    list2=list[-k:]
    for p in range(len(list1)):
        if (p>=len(list1)):
            break
        if(list1.count(list1[p])>1):
            list1.remove(list1[p])

    for q in range(len(list1)):
        a=math.factorial(list.count(list1[q]))
        
        b=(math.factorial(list2.count(list1[q])))
        c=math.factorial((list.count(list1[q]))-list2.count(list1[q]))
        
        #ans += (math.factorial(list.count(list1[q])))/((math.factorial(list2.count(list1[q])))*((math.factorial(list.count(list1[q])))-(math.factorial(list2.count(list1[q]))))
        if(a!=b):
            
            ans += a/(b*c)
            
print "Total possible cases are:", ans


