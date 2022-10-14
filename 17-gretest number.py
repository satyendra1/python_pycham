#greater among two numbers
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
def greater(a,b):
    if a>b:
        return a
    return b
print(f"greater number among {num1} and {num2} is : {greater(num1,num2)}")

#greatest among three mumbers
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
print(f"greatest number among {num1} {num2} and {num3} is : {greatest(num1,num2,num3)}")
#another method to find greatest by calling one fnction i.e greater inside another function i.e greatest
def new_greatest(a,b,c):
    bigger=greater(num1,num2)
    return greater(bigger, c)
print(f"greatest number among {num1} {num2} and {num3} is : {new_greatest(num1,num2,num3)}")



