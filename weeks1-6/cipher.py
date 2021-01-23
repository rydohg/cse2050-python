# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Vigenère Cipher
from sys import stdin, stdout


def make_long_enough_key(key, text):
    if len(key) == len(text):
        return key
    long_key = []
    for i in range(0, len(text)):
        long_key.append(key[i % len(key)])
    return "".join(long_key)


def encrypt(text, key):
    encrypted_text = []
    # this is to ignore other characters
    cipher_count = 0
    for i in range(0, len(text)):
        if ord('a') <= ord(text[i]) <= ord('z'):
            # ord gets ascii code for char
            new_char = (ord(text[i]) - ord('a')) + (ord(key[cipher_count]) - ord('a')) + ord('a')
            if new_char > ord('z'):
                new_char = ord('a') + new_char % ord('{')
            encrypted_text.append(chr(new_char))
            cipher_count += 1
        else:
            encrypted_text.append(text[i])
    return "".join(encrypted_text)


def decrypt(plain_text, key):
    decrypted_text = []
    cipher_count = 0
    for i in range(0, len(plain_text)):
        if ord('a') <= ord(plain_text[i]) <= ord('z'):
            decrypted_char = (((ord(plain_text[i]) - ord('a')) - (ord(key[cipher_count]) - ord('a'))) + 26) % 26 + ord(
                'a')
            decrypted_text.append(chr(decrypted_char))
            cipher_count += 1
        else:
            decrypted_text.append(plain_text[i])
    return "".join(decrypted_text)


input_key = stdin.readline()[:-1]
while True:
    input_line = stdin.readline()
    _, text = input_line.split(maxsplit=1)
    if input_line.startswith("cipher"):
        print(decrypt(text[:-1], make_long_enough_key(input_key, text[:-1])))
    elif input_line.startswith("plain"):
        print(encrypt(text[:-1], make_long_enough_key(input_key, text[:-1])))
