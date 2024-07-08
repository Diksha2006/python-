class gradfather:
    def fun1(self):
       print("HII GRADFATHER")
class father(gradfather):
     def fun2(self):       
         print("HII FATHER")
class son(father):
    def fun3 (self):
        print("HII SON") 
obj=son()
obj.fun1()
obj.fun2()
obj.fun3()              