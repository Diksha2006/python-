v=(input("ENTER THE STRING="))
cnt=0
for i in range (len(v)):
    if(v[i]=='a'or v[i]=='A'or v[i]=='e'or v[i]=='E'or v[i]=='i'or v[i]=='I'or v[i]=='o'or v[i]=='O'or v[i]=='u'or v[i]=='U'):
        cnt+=1
print(v.count('a')+ v.count('A'))
print(v.count('e')+ v.count('E')) 
print(v.count('i')+ v.count('I'))
print(v.count('o')+ v.count('O'))
print(v.count('u')+ v.count('U')) 

print("TOTAL COUNT OF VOWELS=",cnt)
#print("total count of vowels=",v.count('a')+ v.count('A')+v.count('e')+ v.count('E')+v.count('i')+ v.count('I')+v.count('o')+ v.count('O')+count('u')+ v.count('U'))
if(cnt!=0):
    print("ENTERED THE STRING IS VOWEL")
else:
     print("ENTERED THE STRING IS CONSONENT")    