a=int(input("A: "))
b=int(input("B: "))
operator=input("add/sub/muti/divid: ")
if(operator=="add"):
    print(a+b)
elif(operator=="sub"):
    print(a-b)
elif(operator=="muti"):
    print(a*b)
elif(operator=="divid"):
    print(a/b)
else:
    print("invalid number")