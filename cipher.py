task = input('Do you want to encrypt or decrypt a message? ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

message = input('Please enter a message: ')

if task == 'e':
    key = input('Please enter a key: ')
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print('Your message is now: ' + newMessage)
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
