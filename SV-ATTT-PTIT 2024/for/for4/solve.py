
s = b'haind1nSn0rl4x'
text = [0x70, 0x0AE,  0x8A,  0x4D  ,  0x8C,  0x73  ,  0x15,  0x5A  , 0x0EC, 0x0CC, 0x54  ,  0x28  ,  0x32  ,  0x45  , 0x0F0,  0x39  ,  0x27  ,  0x25  , 0x0E6,    4,  0x6A  ,  0x38  ,  0x4F  , 0x0F9,  0x5B  ,  0x95,  0x24  ,  0x9D,  0x9D, 0x0D1,  0x9C,  0x37  , 0x0E9, 0x0AB,  0x98, 0x0A4, 0x0A4,  0x7B  , 0x0C1]
def RC4(key, encrypt):
    S = list(range(256))
    j = 0

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    ciphertext = []
    for char in encrypt:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append((char ^ k))

    return bytes(ciphertext)

flag = print(RC4(s,text))   