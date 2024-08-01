from PIL import Image

def encrypt_image(image_path, key):
    """
    Encrypts the input image using pixel manipulation.

    Args:
        image_path (str): The path to the input image.
        key (int): The encryption key.

    Returns:
        None
    """
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_value = pixels[x, y]
            encrypted_pixel_value = tuple([value ^ key for value in pixel_value])
            pixels[x, y] = encrypted_pixel_value

    image.save("encrypted_image.png")


def decrypt_image(image_path, key):
    """
    Decrypts the input image using pixel manipulation.

    Args:
        image_path (str): The path to the input image.
        key (int): The decryption key.

    Returns:
        None
    """
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_value = pixels[x, y]
            decrypted_pixel_value = tuple([value ^ key for value in pixel_value])
            pixels[x, y] = decrypted_pixel_value

    image.save("decrypted_image.png")


def main():
    while True:
        print("Simple Image Encryption Tool")
        print("----------------------------")
        print("1. Encrypt image")
        print("2. Decrypt image")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            image_path = input("Enter the path to the image: ")
            key = int(input("Enter the encryption key: "))
            encrypt_image(image_path, key)
            print("Encrypted image saved as 'encrypted_image.png'")
        elif choice == "2":
            image_path = input("Enter the path to the encrypted image: ")
            key = int(input("Enter the decryption key: "))
            decrypt_image(image_path, key)
            print("Decrypted image saved as 'decrypted_image.png'")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
