a= float(input("first number:"))
b= float(input("second number:"))
operator=(input("+ , *, - , /:"))


if operator=="+":
    print(a+b) 
elif operator=="*":
    print(a*b)
elif operator=="-":
    print(a-b)    
else:
    if b==0:
        print("not true")
    else:    
        print(a/b)    
    