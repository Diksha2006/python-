print("PASSWORD MUST BE 8 CHARACTER(INCLUDE UPPERCASE,LOWERCASE,NUMBER,SPECIAL CHARACTER)...")
password=input("ENTER THE PASSWORD=")
lcnt=0
ucnt=0
dnt=0
scnt=0
for i in range(len(password)):
    if(password[i]>='a'and password[i]<='z'):
        lcnt+=1
    elif(password[i]>='A'and password[i]<='Z'):
        ucnt+=1 
    elif(password[i]>='0'and password[i]<='9'):
        dnt+=1
    else:
          scnt+=1           
if(lcnt!=0 and  ucnt!=0 and dnt!=0 and scnt!=0 and len(password)>=8):
    print("VALID PASSWORD")
else:
    print("INVALID PASSWORD")    
