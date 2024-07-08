


roll=[]
name=[]
marks=[]
def addstud():
    
    r=input("ENTER THE STUDENT ROLLNO=")
    roll.append(r)
    n=input("ENTER THE NAME=")
    name.append(n)
    m=input("ENTER THE STUDENT MARKS=")
    marks.append(m)
    
def viewdetails():
      print("roll \t name  \t marks")
      for i in range(len(roll)):
         print(roll[i],"\t",name[i],"\t",marks[i])

def upadateit(): 
     froll=input("ENTER THE FIND ROLL=")
     for i in range (len(roll)):
        if(roll[i]==froll): 
            ur=input("ENTER THE STUDENT ROLLNO=")
            un =input("ENTER THE NAME=")
            um=input("ENTER THE STUDENT MARKS=")
            roll[i]=ur
            name[i]=un
            marks[i]=um

def deletstud():
    droll=input("ENTER THE ROLLOF DELETE=")
    for i in range(len(roll)):
       if(roll[i]==droll): 
           roll.remove(roll[i])
           name.remove(name[i]) 
           marks.remove(marks[i])      
           break

count=3
while(count!=0):
    uname=input("ENTER THE UNAME=")
    upass=input("ENTER THE PASS=")
    if(uname=="admin" and upass=="1234"):
        print("LOGIN SUCCESSFULLY")
        print("...............WELCOME TO STUDENT MANAGEMENT SYSSTEM........................")
        cnt=1
        while(cnt!=0):
            print("1.ADD STUDENT")
            print("2.VEIW LIST")
            print("3.UPDATE")
            print("4.DELETE")
            print("5.EXIT")
            ch=int(input("ENTER THE CHOICE=")) 
            if(ch==1):
                 print("........ADD STUDENT.......")
                 addstud()
            if(ch==2):
                 print("................VEIW LIST.........") 
                 viewdetails()
            if(ch==3):
                 print("......................UPDATE...........")
                 upadateit()

            if(ch==4):
                 print("............................DELETE...........")

                 deletstud()
            if(ch==5):
                cnt=0 
                print("YOU ARE LOGGED OUT")                         
        
            count=1
    elif(uname!="admin" and upass!="1234"):
        print("LOGIN UNSUCCESSFULLY") 
    elif(uname!= "admin"):
        print(" USER NAME INCORRECT")
    elif(upass!="1234"):
        print("USER PASSWORD INCORRECT")
    count-=1
    if(count!=0):
        print("REMAINING ATTEMPTS=",count)
        print("YOU CAN TRY AGAIN...")


         

            
 
