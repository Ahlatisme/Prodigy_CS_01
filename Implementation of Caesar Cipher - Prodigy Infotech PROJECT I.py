def encrypt(text, shift):
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # If it's neither, just add the character as it is
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Enter Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'D':
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
