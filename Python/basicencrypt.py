alphabet = 'abcdefghijklmnopqrstuvwxyz'


plaintext = 'helloworld'

ciphertext = 'helloworld'

for i in range( len( plaintext ) ):
    ciphertext[i+2] = plaintext[i]

print(ciphertext)

