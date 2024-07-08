class A:
    def fun1(self):
        self.a=int(input("ENTER THE VALUE OF A="))
        self.b=int(input("ENTER THE VALUE OF B="))
class B(A):
    def fun2(self):
        print("ADDTION=",self.a +self.b)   
class C(A):
    def fun3(self):
        print("SUBSTRACTION=",self.a-self.b)
obj=B()
obj.fun1()
obj.fun2()
obj1=C()
obj1.fun1()
obj1.fun3()                     