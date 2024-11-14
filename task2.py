from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    encrypted_img = img.copy()
    pixels = encrypted_img.load()  # Access pixel data

    # Encrypt by shifting RGB values by the key
    for i in range(encrypted_img.width):
        for j in range(encrypted_img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Save encrypted image
    encrypted_path = image_path.replace(".", "_encrypted.")
    encrypted_img.save(encrypted_path)
    print(f"Encrypted image saved as {encrypted_path}")
    return encrypted_path

def decrypt_image(encrypted_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    decrypted_img = img.copy()
    pixels = decrypted_img.load()  # Access pixel data

    # Decrypt by shifting RGB values back by the key
    for i in range(decrypted_img.width):
        for j in range(decrypted_img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save decrypted image
    decrypted_path = encrypted_path.replace("_encrypted", "_decrypted")
    decrypted_img.save(decrypted_path)
    print(f"Decrypted image saved as {decrypted_path}")
    return decrypted_path

def main():
    print("Image Encryption Tool")
    choice = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")
        return

    image_path = input("Enter the path of the image file: ")
    try:
        key = int(input("Enter an encryption key (integer): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the key.")
        return

    if choice == 'e':
        encrypt_image(image_path, key)
    else:
        decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
