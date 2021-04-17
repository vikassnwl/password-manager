
import string
import random


def decrypt(key, encrypted_password):
    encrypted_password = list(encrypted_password)

    keyBase = string.ascii_letters+string.punctuation

    keyBaseArray = list(keyBase)

    for i, p in enumerate(encrypted_password):
        key = int(key) + i
        random.seed(key)
        random.shuffle(keyBaseArray)
        for j, c in enumerate(keyBaseArray):
            if p == c:
                encrypted_password[i] = keyBase[j]
    decrypted_password = ''.join(encrypted_password)
    return decrypted_password
