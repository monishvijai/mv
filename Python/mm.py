str1=str(input("enter the number"))
str2=' '
index=len(str1)
for i in str1:
    str2=str1[0:index]
    index-=1
    print(str2)
