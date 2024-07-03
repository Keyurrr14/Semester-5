def encrypt(txt):
    ciphertext = ""
    for char in txt:
        if char.isalpha():
            newchar = (ord(char.upper()) - ord('A') + 3) % 26
            ciphertext += chr(newchar + ord('A')) if char.isupper() else chr(newchar + ord('a'))
        else:
            ciphertext += char 
    return ciphertext


def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            newchar = (ord(char.upper()) - ord('A') - 3) % 26
            plaintext += chr(newchar + ord('A')) if char.isupper() else chr(newchar + ord('a'))
        else:
            plaintext += char
    return plaintext



txt = input("Enter message to encrypt: ")
ciphertext = encrypt(txt)
print(f"Encrypted message: {ciphertext}")

plaintext = decrypt(ciphertext)
print(f"Decrypted message: {plaintext}")
