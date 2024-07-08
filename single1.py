class parent:
    def fun1(self):
        print("parent fun1")
class child(parent):
    def fun2(self):
        print("parent fun2")
obj=child()
obj.fun1()
obj.fun2()              