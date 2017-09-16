# import statements.
from globals import friends
from globals import Spy
from spy_details import spy
from termcolor import colored

# add new friends.
import re      # for regular expression
def add_friend():
    new_friend=Spy('','.',0,0.0,False)
    temp = True # it can be used as Temporary variable
    # Defining use of RE
    patternsalutation = '^Mr|Ms$'
    patternname = '^[A-Za-z][A-Za-z\s]+$'
    patternage = '^[0-9]+$'
    patternrating = '^[0-9]+\.[0-9]$'

   # new_friend  = {
    #    'name': '',
     #   'salutation': '.',
      #  'age': 0,
       # 'rating': 0.0,
        #'is_online': False
    #}
    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation']= input("Are they Mr. or Ms.?: ")

    # concatenation of name and salutation.
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(input("Age? "))

    new_friend['rating'] = float(input("Spy rating? "))

    # users input validations
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
        friends.append(new_friend)
        print ('Friend Added!','green')    # Success msg
    else:
        print ('Sorry! Invalid entry. We can\'t add spy with the details you provided','red') # Error msg

    # returning total no of friends.
    return len(friends)
