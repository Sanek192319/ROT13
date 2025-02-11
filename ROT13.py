import codecs

def rot13(text):
    return codecs.encode(text, 'rot_13')

# Example usage
if __name__ == "__main__":
    text = input("Enter text: ")
    encrypted = rot13(text)
    print(f"ROT13 Output: {encrypted}")

    # Since ROT13 is symmetric, applying it again decrypts the text
    decrypted = rot13(encrypted)
    print(f"Decrypted: {decrypted}")
