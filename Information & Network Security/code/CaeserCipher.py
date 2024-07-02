def encrypt(plaintext):
    ciphertext = ""
    for char in plaintext.upper():
        newchar = (ord(char) - ord('A') + 3) % 26
        ciphertext += chr(newchar + ord('A'))
    return ciphertext

def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext.upper():
        newchar = (ord(char) - ord('A') - 3) % 26
        plaintext += chr(newchar + ord('A'))
    return plaintext


txt = input("Enter plaintext: ")
ciphertext = encrypt(txt)
plaintext = decrypt(ciphertext)
print(f"Encrypted Text: {ciphertext}")
print(f"Decrypted Text: {plaintext}")