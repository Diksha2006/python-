class A:
    def getdata (self):
        self.a=int(input("ENTER THE VALUE OF A="))
        self.b=int(input("ENTER THE VALUE OF B="))
    
class B(A):
       
    def putdata(self):
        
        print("ADDITION=",self.a+self.b)
        print("SUBSTRACTION=",self.a-self.b)
        print("DIVISION=",self.a/self.b)
        print("MULTIPLICATION=",self.a*self.b)
obj=B()
obj.getdata()
obj.putdata()              