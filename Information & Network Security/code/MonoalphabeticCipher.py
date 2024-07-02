def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            index = ord(char) - ord('A')
            ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            index = key.index(char)
            plaintext += chr(index + ord('A'))
        else:
            plaintext += char
    return plaintext

plaintext = input("Enter plaintext: ")
key = "XYZABCDEFGHIJKLMNOPQRSTUVW"

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)