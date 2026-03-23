
alphabet = 'abcdefghijklmnopqrstuvwxyz'
while True:
    choose = input('encode, decode, quit?: ').strip().lower()
    
    if choose == 'encode':
        encode = input('Encode input: ')
        rotate = int(input('Rotation: '))
        cipher = ''
        for i in encode:
            if i.lower() in alphabet:
                index = alphabet.index(i.lower())
                inde = (index + rotate) % 26
                if i.isupper():
                    cipher += alphabet[inde].upper()
                else:
                    cipher += alphabet[inde]
            else:
                cipher += i
        print(cipher)
        
    elif choose == 'decode':
        statement = input('Correct statement: ')
        decode = input('Coded statement: ')
        found = False
        for rotate in range(26):
            word = ''
            for i in decode:
                if i.lower() in alphabet:
                    index = alphabet.index(i.lower())
                    inde = (index - rotate) % 26
                    if i.isupper():
                        word += alphabet[inde].upper()
                    else:
                        word += alphabet[inde]
                else:
                    word += i
                    
            if word == statement:
                print('Rotation:', str(rotate))
                print('Decoded text:', statement)
                found = True
        if not found:
            print('No rotation found')
            
    elif choose == 'quit':
        print('Thank you!')
        break
    else:
        print('Error! Please choose a given option.')

    
