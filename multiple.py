class A:
    def fun1(self):
        print("I AM FUN1")
class B:
    def fun2(self):
        print("I AM FUN2")  
class C(A,B):
    def fun3(self):
        print("I AM FUN3") 
obj=C()
obj.fun1()
obj.fun2()
obj.fun3()