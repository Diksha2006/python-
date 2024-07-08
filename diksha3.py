n=int(input("ENTER THE NUMBER="))
rev=0
rem=0
no=n
rem=no%10
print("last number=",rem)
while(no>10):
     r=(no/10)
     no=no/10
     print("first numer=",int(r))
     no+=1
