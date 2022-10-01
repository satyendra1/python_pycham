#User Input
Name=input("Enter your Name:")#input function will always take value as string
print(Name)
age=input("Enter ur age:")
print("print type of variable age",type(age))
print(age)
name,age=input("Enter ur name and age:").split(" ")#by default split take as space

name,age=input("Enter ur name and age:").split(",")#Here split will take as aargument comma(,)

print("Name is",name,"and age is",age)
age=int(input("Enere ur age:"))#Here age will store value as integer
print("print type of variable age",type(age))
print(age)
