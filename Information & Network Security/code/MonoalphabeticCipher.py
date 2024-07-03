def encrypt(txt, key):
    ciphertext = ""
    for char in txt:
        if char.isalpha():
            newchar = (ord(char.upper()) - ord('A') + key) % 26
            ciphertext += chr(newchar + ord('A')) if char.isupper() else chr(newchar + ord('a'))
        else:
            ciphertext += char 
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            newchar = (ord(char.upper()) - ord('A') - key) % 26
            plaintext += chr(newchar + ord('A')) if char.isupper() else chr(newchar + ord('a'))
        else:
            plaintext += char
    return plaintext


txt = input("Enter message to encrypt: ")
key = int(input("Enter key for encryption: "))
ciphertext = encrypt(txt, key)
print(f"Encrypted message: {ciphertext}")

plaintext = decrypt(ciphertext, key)
print(f"Decrypted message: {plaintext}")
