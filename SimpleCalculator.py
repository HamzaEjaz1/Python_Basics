Num1 = int(input("Enter First Number"))
Num2 = int(input("Enter Second Number"))
op = input("Enter Operator : ")

if op=="+":
    print("sum is : ",Num1+Num2)
elif op=="-":
    print("sub is : ",Num1-Num2)
elif op=="*":
    print("Mul is : ",Num1*Num2)
elif op=="/":
    print("Div is : ",Num1/Num2)
else:
    print("Invalid Operator")