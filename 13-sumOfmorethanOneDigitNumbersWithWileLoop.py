#sum of more than one digit numbers
n=input("please Enter the value of number:")
sum=0
i=0
print(f"lenght of numbers is:{len(n)}")
while i <len(n):
    print(f"index {i} value is: {n[i]}")
    sum=sum+int(n[i])
    i+=1
print(f"sum of {n} digits is:{sum}")

