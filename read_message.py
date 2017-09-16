from select_friend import select_friend
from steganography.steganography import Steganography
from termcolor import colored
from globals import friends
import re

def read_message():
    # choose friend from the list
    sender=select_friend()
    # Checking if Friend List is not empty
    if friend_choice != (-1):
        pattern = '^[A-Za-z][0-9A-Za-z\s]*\.jpg$'
        a = True  # temporary variable
        # Average Words
        friends[friend_choice].calcAverageWords()
        # prepare the  message
        while a:
            output_image = input("Provide the name of the image to be decrypted: ")
            if (re.match(pattern, output_image) != None):
                a = False
            else:
                print(colored("Wrong choice.Enter Again!", 'red'))
        try:    # Exception Handling
            # Decrypt the message
            text = Steganography.decode(output_image)
            print("Message:", text)
        except TypeError:
            print(colored("Image does not have any message!", 'red'))
        except IOError:
            print(colored("Image Does Not Exists!!!!", 'red'))
    else:
        print(colored("Empty Friend's List is there!", 'red'))

