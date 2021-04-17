import string
import random


def encrypt(key, raw_password):
    raw_password = list(raw_password)

    keyBase = string.ascii_letters+string.punctuation

    keyBaseArray = list(keyBase)

    for i, p in enumerate(raw_password):
        key = int(key) + i
        random.seed(key)
        random.shuffle(keyBaseArray)
        for j, c in enumerate(keyBase):
            if p == c:
                raw_password[i] = keyBaseArray[j]
    encrypted_password = ''.join(raw_password)
    return encrypted_password
