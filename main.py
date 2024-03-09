import string
import random

print(f'digits: {string.digits}')
print(f'ascii_letters: {string.ascii_letters}')
print(f'punctuation: {string.punctuation}')
print(f'printable: {string.printable}')

pw = ''

pw_len = input('how long do u want')

pw_len = int(pw_len)

for i in range (pw_len):
    pw += random.choice(string.printable)

print(f'Here you go: {pw}')









