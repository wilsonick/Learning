text = 'sup'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
dvalphabet = 'axje.uidchtnmbrl\'poygk,qf';

newtext = 'abc'


for i in range( len( text ) ):
    for j in range( len( alphabet ) ):
        if text[i] == alphabet[i]:
            newtext[i] = dvalphabet[alphabet[i]]

print(newtext)
