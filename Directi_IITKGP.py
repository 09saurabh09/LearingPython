s= raw_input("Enter the string:")
l= len(s)
stack=[]
count=0
for i in range(l):
    print s[i]
    
    if ((s[i]>='0')&(s[i]<='9')):
        count = count+1
        print count
    elif(s[i]=='('):
        count=count-1
        stack.append(count)
        print count
        count=0
        
        stack.append(s[i-1])
        

    elif(s[i]==')'):
        count=count*int(stack.pop())+ stack.pop()
        print count
