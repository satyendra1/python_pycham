#Character count from given string
string=input("Enter the string:")
i=0
temp_var=""
while i<len(string):
    if string[i] not in temp_var:
     print(f"{string[i]}:{string.count(string[i])}")
     temp_var+=string[i]
    i+=1
print(temp_var)
