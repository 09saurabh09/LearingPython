class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        

x1=tree(20)
x2=tree(10)
x3=tree(24)
x4=tree(6)
x5=tree(12)
x6=tree(22)
x7=tree(26)


x1.left=x2
x1.right=x3
x2.left=x4
x2.right=x5
x3.left=x6
x3.right=x7


def binary_tree_search(x1,num):
    p=x1
    Found=False
    while((Found==False)&(p<>None)):
        if(num==p.data):
            print"Number found"
            Found=True
        elif(num<p.data):
            p=p.left
        else:
            
            p=p.right
    if (Found==False):
        print "Number not found"
            
