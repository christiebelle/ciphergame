#The task message is what tells the programme what function to carry out: encrypting or decrypting
task = raw_input('Do you want to encrypt (e) or decrypt (d) a message? ')

#These are the accepted options for input - anything other than an 'e'/'d'/'bf'/'q' will break the application
while task == 'e' or task == 'd' or task == 'bf':

#The 'alphabet' array lists out all 26 letters of the alphabet - I know they are only lowercase for now, but there is a reason for that!
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#The 'newMessage' parameter is currently set to empty, this is where our encrypted/decrypted message will eventually live
    newMessage = ''

#So we have taken in a 'task', now we need an actual message to work on. That is what this parameter is.
    message = raw_input('Please enter a message: ')

#Now we come on to our conditional statements that tell the programme how to behave and what to do with our message.
#So our first condition asks are we 'encrypting' a message?
    if task == 'e':
        key = input('Please enter a key - this will be a number between 1 and 25: ') #Our key will set how much we scramble the message
        for letter in message:
        #'letter' is a new parameter and refers to each individual letter in the message, so this is essentially saying for each letter
        #in our message, do the following...
            if letter in alphabet: #this is making sure that the our 'letter' is in our 'alphabet' array, if it is then it will...
                position = alphabet.find(letter) #This finds where in our array the letter is, and gives it a number value
                newPosition = (position + key) % 26 #this line is where we do the shuffling. We take the number position, add the key to it
                                                    #and then find what that is mod 26 - essentially what is the remainder when we divide (position+key) by 26. The answer
                                                    #then becomes our newPosition
                newletter = alphabet[newPosition] #searching through our 'alphabet' array we look for what letter is at 'newPosition' and this
                                                  #becomes our new letter.
                newMessage += newletter #we add the newletter to the 'newMessage' and go back to the start of the loop
            else: #the condition for what happens if the letter is not in the 'alphabet', we just add it to the newMessage as it is (space)
                newMessage += letter
        print('Your message is now: ' + newMessage) #we then print out the newMessage which should - if we have done our job - be jibberish
        task = raw_input('Do you want to encrypt (e) or decrypt (d) a message? ') #and so we start again
#Now we look at what happens when 'decrypting' a message
    elif task == 'd':
        key = input('Please enter a key - this will be a number between 1 and 25: ') #nothing different so far. We need a message and a key to work with
        for letter in message: #same conditions are being set here, working with each individual letter in the message
            if letter in alphabet:
                position = alphabet.find(letter) #we get the number position for the letter
                newPosition = (position - key) % 26 #this time however we do position minus key before finding what that is mod 26.
                newletter = alphabet[newPosition] #again we use the 'newPosition' to then search the array for the letter at that spot
                newMessage += newletter #and we add it to our 'newMessage'
            else:
                newMessage += letter #or we just add it in as it is if it doesnt appear in the array
        print('Your message is now: ' + newMessage) #display the decreypted message
        task = raw_input('Do you want to encrypt (e) or decrypt (d) a message? ') #and we go again!
#BONUS CONTENT! So 'bf' stands for Brute Force which is a small easter egg.
    elif task == 'bf':
#You will notice the difference in the condition statement here. We are now saying that we are working with every letter in the alphabet array
#These instructions are essentially telling the computer to print out every single combination for keys 1-25
        for i in range(len(alphabet)):
            newMessage = '' #'newMessage' is being set empty here because each time we run through this loop we need a new empty message
            for letter in message: #then we do into the same conditional logic for decrypting a message, because that is what brute force is
                if letter in alphabet:
                    position = alphabet.find(letter)
                    newPosition = (position - i) % 26
                    newletter = alphabet[newPosition]
                    newMessage += newletter
                else:
                    newMessage += letter
            print('Key #%s: %s'%(i, newMessage)) #we are printing it out this way so that we can identify the key used to encrypt the message
        task = raw_input('Do you want to encrypt (e) or decrypt (d) a message? ') #and we go again!
    elif task == 'q': #this just quits the application
         print("Thank you! Goodbye!")
         break
