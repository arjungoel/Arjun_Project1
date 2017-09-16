# global variables and constants here.
from termcolor import colored
from steganography.steganography import Steganography
# current status message is initialized to None.
current_status_message = None
# Color Coding
# Successful msg ==> green
# Error msg ==> red

# list to store status messages.
STATUS_MESSAGES = ['My name is Bla Bla Bla!!!!, Sir']

# lists to store users friends information.
friends = []
# class Spy
class Spy:
    def __init__(self, salutation, name, age, rating, isonline):
        # Assigning Values
        self.Name = salutation + "." + name
        self.Age = age
        self.Rating = rating
        self.SpyOnline = isonline
        self.chat = []
    def displayDetails(self):
        print(self.Name, " ", self.Age)
    def calcAverageWords(self):
        # Average Words Spoken
        avg = 0
        if len(self.chat) != 0:
            for i in self.chat:
                avg = avg + len(Steganography.decode(i.Message))
                avg = avg / (len(self.chat))
        print("Average Words Spoken: ", avg)

    # Chat class
    class Chat:
        def __init__(self, msgImage, timestamp):
            # Assigning Values
            self.Message = msgImage
            self.Timestamp = timestamp

        def displayMessage(self):
            print (colored(self.Timestamp, 'blue'), "\n Message: ", self.Message, "\n")


