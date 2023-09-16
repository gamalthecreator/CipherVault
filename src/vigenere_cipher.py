import random
import string

def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    i = 0
    for c in plaintext:
        if c.isalpha():
            # Shift the letter forward by the corresponding letter in the keyword
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            if c.isupper():
                ciphertext += chr((ord(c) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(c) + shift - 97) % 26 + 97)
            i += 1
        else:
            ciphertext += c
    return ciphertext


def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    i = 0
    for c in ciphertext:
        if c.isalpha():
            # Shift the letter backwards by the corresponding letter in the keyword
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            if c.isupper():
                plaintext += chr((ord(c) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(c) - shift - 97) % 26 + 97)
            i += 1
        else:
            plaintext += c
    return plaintext



def generate_random_key(min_length, max_length):
    length = random.randint(min_length, max_length)
    word = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return word

