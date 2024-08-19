from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
import binascii

# Convert hex to bytes
def hex_to_bytes(hex_str):
    return binascii.unhexlify(hex_str)

# XOR two byte sequences
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Known ciphertext and plaintext
known_ciphertext_hex = "056f2aa2d27007009b3c76bda2dbd232a8b9c40a5c7c8f470154ea5c225c2a5837806a0b3338dcefa5f30ec5303989e096"  # Replace with the known ciphertext in hex
known_plaintext = b'THIS IS A FORM FLAG: PTITCTF{This_is_a_fake_flag}'  # Known plaintext

# Convert known ciphertext from hex to bytes
known_ciphertext = hex_to_bytes(known_ciphertext_hex)

# Recover the keystream by XORing known plaintext with its ciphertext
keystream = xor_bytes(known_ciphertext, known_plaintext)

# Known ciphertext to decrypt
ciphertext_to_decrypt_hex = "01732aa5b16d125b947347ada9f9872baf96ec47236d9e5d0a44d1451c723f"  # Replace with the ciphertext you want to decrypt

# Convert ciphertext to bytes
ciphertext_to_decrypt = hex_to_bytes(ciphertext_to_decrypt_hex)

# Decrypt the ciphertext using the recovered keystream
decrypted_message = xor_bytes(ciphertext_to_decrypt, keystream)

print("Decrypted Message:", decrypted_message.decode())