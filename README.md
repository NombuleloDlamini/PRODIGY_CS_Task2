# Task 2: Image Encryption Tool
This task provides a program to encrypt and decrypt images by shifting each pixel's
RGB values.
- encrypt_image(image_path, key): This function encrypts an image by loading it
and adding a `key` to each pixel's RGB values, with modulo 256 to wrap values
within the range. The encrypted image is saved with "_encrypted" added to the
filename.
- decrypt_image(encrypted_path, key): This function decrypts an image by
reversing the encryption: subtracting the `key` from each pixel's RGB values (again
using modulo 256). The decrypted image is saved with "_decrypted" in the filename.
- main(): The main function prompts the user to choose between encrypting or
decrypting an image. It then asks for an image file path and an integer key for
encryption. Based on the choice, it calls either the `encrypt_image` or
`decrypt_image` function.
