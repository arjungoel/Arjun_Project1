from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
from globals import friends
import re
def read_message():
    # choose friend from the list
    sender=select_friend()
    patternimage='^[A-Za-z][0-9A-Za-z\s]*\.jpg$'
    temp=True
    while temp:
            encrypted_image = raw_input("Provide the name of the image to be encrypted: ")
            if (re.match(patternimage, encrypted_image) != None):
                temp = False
            else:
                print colored("Wrong choice.Enter Again!",'red')
    try:    # Exception Handling
            # Decrypt the message
        text = secret_message = Steganography.decode(encrypted_image)
        print "message:",text
    except TypeError:
        print colored("Image does not have any message!", 'red')
    except IOError:
        print colored("Image Does Not Exists!!!!", 'red')

        # save the messages
        new_chat = {
            'message':text,
            'time':datetime.now(),
            'sent_by_me':False
        }
        friends[sender]['chats'].append(new_chat)
        print colored("Your secret message has been saved.",'green')