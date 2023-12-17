def greeting_function(name):
    print("Weclome,",name)
greeting_function("Joe")

def sum (num1, num2):
    print(f"Sum of {num1} & {num2} is  : ",num1+num2)
sum(10,20)


def sub (num1,num2):
    print(f"subtraction of {num1} & {num2} is " ,num1-num2)
sub(100,10)

def Mul (Num1 , Num2 ):
    print(f"Mutlipliaction of {Num1} & {Num2} is " , Num1*Num2)
Mul(6,7)

def Div(Num1 , Num2):
    print(f"Division of {Num1} & {Num2} is : ", Num1/Num2)
Div(2,5)

def my_Function():
    return 5+4
print(my_Function())

def add_Numbers(num1, num2):
    return num1+num2

print(add_Numbers(5,10))


def add_Numbers(Num1 ,Num2):
    return Num1+Num2

Num1=int(input("Enter Number 1 : "))
Num2=int(input("Enter Number 2: "))
print(add_Numbers(Num1,Num2))