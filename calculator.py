a=float(input("enter your first number: "))
b=input("enter your operator: ")
c=float(input("enter your second number: "))
if(b=="+"):
    print("the sum of",a,"and",c,"is",a+c)
elif(b=="-"):
    print("the subtraction of",a,"and",c,"is",a-c)
elif(b=="*"):
    print("the product of",a,"and",c,"is",a*c)
elif(b=="/"):
    print("the division of",a,"and",c,"is",a/c)
else:
    print("inavlid operator")