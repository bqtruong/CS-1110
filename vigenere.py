def letter_to_index(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter.isalpha():
        return alphabet.index(letter)
    return -1
def index_to_letter(index):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    if index >= 0 and index <= 25:
        return alphabet[index]
    return "?"
def vigenere_encrypt(plain_letter, key_letter):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    if plain_letter.isalpha() and key_letter.isalpha():
        return alphabet[(alphabet.index(plain_letter) + alphabet.index(key_letter)) % 26]
    else:
        return plain_letter
def vigenere_decrypt(cipher_letter, key_letter):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    if cipher_letter.isalpha() and key_letter.isalpha():
        return alphabet[(alphabet.index(cipher_letter) + 26 - alphabet.index(key_letter)) % 26]
    else:
        return cipher_letter
def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    crypt = [None] * len(plaintext)
    for x in range(0, len(plaintext)):
        crypt[x] = vigenere_encrypt(list(plaintext)[x], key[x])
    return "".join(crypt)
def decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    plaintext = [None] * len(ciphertext)
    for x in range(0, len(ciphertext)):
        plaintext[x] = vigenere_decrypt(list(ciphertext)[x], key[x])
    return "".join(plaintext)
