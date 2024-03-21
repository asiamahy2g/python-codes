"""f= open("test.txt",'w') #"w" "a" , "r"
f.write("#this is my first line\n")
f.write("this is the second line")
f.close"""
try:
    with open("test.txt", "a") as f:
        f.read()

except Exception as e:
    print(e)