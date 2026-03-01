import random
import string
import time

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list (chars)
key = chars.copy ()
random.shuffle (key)

#ENCRYPTION:
plain_text= input ("Orignal Message: ")
cipher_text = ""

for letters in plain_text:
    index = chars.index (letters)
    cipher_text += key[index]

time.sleep (1)
print (f"Encrypted Message: {cipher_text}")

print ("***********************************")
time.sleep (2)
# DECRYPTION:
cipher_text = input("Encrypted Message: ")
plain_text = ""

for letters in cipher_text:
    index = key.index(letters)
    plain_text += chars[index]

time.sleep (1)
print(f"Orignal Message   : {plain_text}")


#Another way to write this code (By implementing OOP):
import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
chars = list (chars)
key = chars.copy()
random.shuffle(key)

class Encryption:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        cipher_text = ""
        for letter in plain_text:
            index = chars.index (letter)
            cipher_text += key [index]
        print (f"Cipher text: {cipher_text}")
encrypt = Encryption(input ("Plain text: "))

class Decryption:
    def __init__(self, cipher_text):
        self.cipher_text = cipher_text
        plain_text = ""
        for letter in cipher_text:
            index = key.index (letter)
            plain_text += chars [index]
        print (f"Plain text: {plain_text}")
decrypt = Decryption(input ("Cipher text: "))