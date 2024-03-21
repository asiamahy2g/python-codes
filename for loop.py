num_v=0
num_c=0

name = input(" Enter name here: ")
for i in name.strip():
    if i in ['a','e','i','o','u']:
        print(f"{i} is a vowel")
        num_v+=1

    else:
        print(f"{i} is a consonant")
        num_c+=1

print(f"number of vowels is :{num_v}")
print(f"number of consonants is :{num_c}")

