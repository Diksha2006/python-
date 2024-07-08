class gradfather:
    def fun1(self):
       print("HII GRADFATHER")
class father(gradfather):
     def fun2(self):       
         print("HII FATHER")
class son(gradfather):
    def fun3 (self):
        print("HII SON")
obj1=father()
obj1.fun1()
obj1.fun2()         
obj=son()
obj.fun1()
obj.fun3()             