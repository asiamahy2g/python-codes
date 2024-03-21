"""#number 1 and 2
my_string = input("Enter a string: ")
a = len(my_string.strip())

print(f" the string is {a} charaters")

string2 = input("Enter input here:  ")
b = len(string2.strip())

if b > 4:
    print("invalid entry")

else:
    print("valid entry")

##number 3
username = input("username: ")
password = input("password: ")

if username == "admin" and password == "admin":
 print("successfully login")
else:
 print("wrong username or password")


 ##number 4

while True:
    zip_code = input("Please enter a zip code: ")
    z_1 = len(zip_code.strip())
    z_2 = zip_code.isdigit()
    if  z_1 == 5 and z_2 == True:
        print(" your entry is valid")
        break
    else:
        print("invalid entry")
 
 ##number 5
email = input("Enter email address: ")

if "@" in email:
      print("valid email address entered")
else:
    print("enter a valid email address")
"""
 ##number 6
try:
    int1 = int(input("Enter integer 1: "))
    int2 = int(input("Enter integer 2: "))
    sum = int1 + int2
    print(sum)
except ValueError:
    print("please enter a valid integer")



