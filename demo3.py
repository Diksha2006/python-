q=int(input("enter the qty="))
r=int(input("enter the rate="))
total=q*r
print("total=",total)
d=int(input("enter the dis%"))

print("dis value=",total/d)
demo=(d/100)*1000
basic=total-demo
print("basic sal=",basic)
g=int(input("enter the gst%"))
gst=(g/100)*1000
print("net total=",gst+basic)

