def caesar_encrypt(text, shift):
    """
    Encrypts the input text using the Caesar Cipher algorithm.

    Args:
        text (str): The input text to be encrypted.
        shift (int): The shift value for the Caesar Cipher.

    Returns:
        str: The encrypted text.
    """
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    """
    Decrypts the input text using the Caesar Cipher algorithm.

    Args:
        text (str): The input text to be decrypted.
        shift (int): The shift value for the Caesar Cipher.

    Returns:
        str: The decrypted text.
    """
    return caesar_encrypt(text, -shift)


def main():
    while True:
        print("Caesar Cipher Program")
        print("---------------------")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter the text to be encrypted: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_encrypt(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == "2":
            text = input("Enter the text to be decrypted: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_decrypt(text, shift)
            print(f"Decrypted text: {decrypted_text}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
