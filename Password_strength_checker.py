print("="*40)
print("    PASSWORD_STRENGTH_CHECKER")
print("="*40)
password = input("Enter your password:")
score = 0
print ("Total password length:",len(password))
if len(password) <= 8 :
    print (" ✘ Password length : Weak")
else:
    score = score + 1
    print (" ✔ Password length : Strong")
has_uppercase = False
for character in password:
    if character.isupper():
        has_uppercase = True
if has_uppercase:
    score = score + 1
    print(" ✔ Uppercase letter : Found")
else:
    print(" ✘ Uppercase letter : Not Found")
has_number = False
for character in password:
    if character.isdigit():
        has_number = True
if has_number:
    score = score + 1
    print(" ✔ Number : Found")
else:
    print(" ✘ Number : Not Found")
has_special = False
for character in password:
    if not character.isalnum():
        has_special = True
if has_special:
    score = score + 1
    print(" ✔ special character : Found")
else:
    print(" ✘ special character : Not Found")
has_lowercase = False
for character in password:
    if character.islower():
        has_lowercase = True
if has_lowercase:
    score = score + 1
    print(" ✔ Lowercase letter : Found")
else:
    print(" ✘ Lowercase letter : Not Found")
print ("Your score is:",score,"/5")
if score == 5:
    print("VERY STRONG PASSWORD")
elif score == 4:
    print("STRONG PASSWORD")
elif score == 3:
    print("MEDIUM PASSWORD")
else:
    print("WEAK PASSWORD")
print("-"*40)
print("SUGGESTIONS:")
if score == 5:
    print("No suggestions needed. Your password is strong!")
else:
    if len(password) <= 8 :
        print("-Use a longer password")
    if not has_uppercase:
        print("-Add an uppercase letter")
    if not has_lowercase:
        print("-Add a lowercase letter")
    if not has_number:
        print("-Add a number")
    if not has_special:
        print("-Add a special character")
        
    

    
