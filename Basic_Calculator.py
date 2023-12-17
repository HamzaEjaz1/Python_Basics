# define the function add sub mul div
# print oprtion
# ask values
# call the function
# While loop to continues


def add(a,b):
    result = a +b
    print(a ," + ", b , " = ", result)

def Sub(a,b):
    result = a-b
    print(a ," - ", b , " = ", result)

def MUL(a,b):
    result = a*b
    print(a ," * ", b , " = ", result)

def Div(a,b):
    result = a/b
    print(a ," / ", b , " = ", result)

print("A . ADDITION")
print("B . SUBTRACTION")
print("C . MULTIPLICATION")
print("D . DIVISION")

choice= input("Enter The Option : ")
uC = choice.upper()

if uC=="A":
    print("Additon")
    num = int(input("Enter first Number :  "))
    num_2 = int(input("Enter Second Number : "))
    add(num,num_2)
elif uC=="B":
    print("SUBTRACTION")
    num = int(input("Enter first Number :  "))
    num_2 = int(input("Enter Second Number : "))
    Sub(num,num_2)
elif uC=="C":
    print("MULTIPLICATION")
    num = int(input("Enter first Number :  "))
    num_2 = int(input("Enter Second Number : "))
    MUL(num,num_2)
elif uC=="D":
    print("DIVISON")
    num = int(input("Enter first Number :  "))
    num_2 = int(input("Enter Second Number : "))
    Div(num,num_2)
