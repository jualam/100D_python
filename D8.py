['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt and 'decode' to decrypt").lower()
text=input("Enter the text you want to encrypt/decrypt:").lower()
shift=int(input("type the number to shift"))

def encrypt(text,shift):
    for i in text:
        