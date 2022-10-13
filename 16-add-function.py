#Sum of two numbers
#diffrent types of function define
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
print (id(num1))#id function use to identify position in memory
print (id(num2))
def add(a,b):#define function with parameter
    print (id(a))
    print (id(b))
    return a+b
print(add(num1,num2))#called function

def hello():# Define function without parameter
    return "Hi Friends"
print(hello())
