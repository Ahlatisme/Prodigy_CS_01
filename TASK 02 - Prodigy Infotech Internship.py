from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    encrypted_pixels = pixels ^ key  # XOR operation with the key
    
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    decrypted_pixels = pixels ^ key  # XOR operation with the key (same as encryption)
    
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? (Enter Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue

        image_path = input("Enter the path to the image: ")
        key = int(input("Enter the key (integer value): "))
        output_path = input("Enter the path for the output image: ")

        if choice == 'E':
            encrypt_image(image_path, key, output_path)
        elif choice == 'D':
            decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
