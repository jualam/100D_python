import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the password generator!")
num_letters=int(input("How many letters do you want in your password?\n"))
num_symbols=int(input("Ho mnay symbols would you like in your password?\n"))
num_numbers=int(input("How many numbers would you like in your password?\n"))

#Easy lev
password1=""

for i in range(0,num_letters):
    password1+=random.choice(letters)
for i in range(0,num_symbols):
    password1+=random.choice(symbols)
for i in range(0,num_numbers):
    password1+=random.choice(digits)
print (f"Easy password: {password1}")
print(len(password1))

#Hard level
password2=""
password_list=[]
for i in range(0,num_letters):
    password_list+=random.choice(letters)
for i in range(0,num_symbols):
    password_list+=random.choice(symbols)
for i in range(0,num_numbers):
    password_list+=random.choice(digits)

random.shuffle(password_list)
for i in password_list:
    password2+=i
print(f"Hard password: {password2}")
print(len(password2))
