from Cryptodome.Cipher import DES
import base64

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text.decode()

# Your base64-encoded ciphertext
cipher_b64 = "Xfw54DbCB6IXKg/a1tdlG40kvNy/0z6CYtdmEvrC+2A="

# Decode the base64 to get the ciphertext
cipher = base64.b64decode(cipher_b64)

# Use the same key used for encryption
key = b'PTITCTF{'

# Decrypt the ciphertext
decrypted_text = decrypt(cipher, key)
print("Decrypted text:", decrypted_text)
