plaintext = 'sashaiscool'

convert = 'abcdefghijklmnopqrstuvwxyz'
convert2 = convert[::-1]
shift = 10

numplain = list( range( len( plaintext ) ) )
shiftnumplain = list( range( len( numplain ) ) )

ciphertext = list( range( len( plaintext) ) ) 




# Convert plaintext to numbers in a list using the alphabet
# Find the number of the characters in plaintext in the alphabet

for i in range( len( plaintext ) ):
    for j in range( len( convert ) ):
        if plaintext[i] == convert[j]:
            numplain[i] = j+1   # Convert to numbers

            shiftnumplain[i] = j + shift # Shift the numbers

            # Wrap around all the numbers, modulus 26.
            if (j + shift) >= 26:
                shiftnumplain[i] = shiftnumplain[i] % 26

            # Use the new numbers to convert back to ciphertext, using convert
            ciphertext[i] = convert[shiftnumplain[i]]



print(plaintext)

print(numplain)
print(shiftnumplain)

print(ciphertext)
print(''.join(map(str,ciphertext) ) )








'''
for i in range( len( shiftnumplain ) ):
    for j in range( len( convert ) ):
        if 
'''


