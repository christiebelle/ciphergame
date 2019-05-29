task = input('Do you want to encrypt (e) or decrypt (d) a message? ')
while task == 'e' or task == 'd' or task == 'bf':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newMessage = ''

    message = input('Please enter a message: ')

    if task == 'e':
        key = input('Please enter a key - this will be a number between 1 and 26: ')
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position + key) % 26
                newCharacter = alphabet[newPosition]
                newMessage += newCharacter
            else:
                newMessage += character
        print('Your message is now: ' + newMessage)
        task = input('Do you want to encrypt (e) or decrypt (d) a message? ')
    elif task == 'd':
        key = input('Please enter a key: ')
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position - key) % 26
                newCharacter = alphabet[newPosition]
                newMessage += newCharacter
            else:
                newMessage += character
        print('Your message is now: ' + newMessage)
        task = input('Do you want to encrypt (e) or decrypt (d) a message? ')
    elif task == 'bf':
        for i in range(len(alphabet)):
            newMessage = ''
            for character in message:
                if character in alphabet:
                    position = alphabet.find(character)
                    newPosition = (position - i) % 26
                    newCharacter = alphabet[newPosition]
                    newMessage += newCharacter
                else:
                    newMessage += character
            print('Key #%s: %s'%(i, newMessage))
        task = input('Do you want to encrypt (e) or decrypt (d) a message? ')
    elif task == 'q':
         print("Thank you! Goodbye!")
         break
