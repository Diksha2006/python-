a=int (input("ENTER THE FIRST NUMBER="))
b=int (input("ENTER THE SECOND NUMBER="))
c=int(input("ENTER THE THIRD NUMBER="))
if(a>b and a>c):
             print("A IS GREATER")
elif(b>a and b>c):
             print("B IS GREATER")
elif(c>a and c>b ): 
             print("C IS GREATER") 
elif(a==b and a==c):
             print("ALL NUMBER EQUAL")
elif(a==b or a<c):
             print("A AND B IS EQUAL AND C IS SMALLER") 
elif(a==c or a<b):
             print("A AND C IS EQUAL AND B IS SMALLER")
elif(b==c or b<a):
              print("B AND C IS EQUAL AND A IS SMALLER")  