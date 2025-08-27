alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    output_text = ""
    if direction == "decode":
        shift *= -1

    for i in text:
        if i in alpha:
            output_text += alpha[(alpha.index(i) + shift) % len(alpha)]
        else:
            output_text += i  # leave spaces, punctuation unchanged

    if direction == "encode":
        return f"The encoded text is: {output_text}"
    elif direction == "decode":
        return f"The decoded text is: {output_text}"

def main():
    while True:
        direction = input("\nType 'encode' to encrypt, 'decode' to decrypt, or 'exit' to quit: ").lower()

        if direction == "exit":
            print("Goodbye!")
            break  

        if direction not in ["encode", "decode"]:
            print("Invalid option. Please choose 'encode', 'decode', or 'exit'.")
            continue

        text = input("Enter the text: ").lower()
        shift = int(input("Enter the shift amount: "))

        result = caesar(text, shift, direction)
        print(result)

if __name__=="__main__":
    main()

