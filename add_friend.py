# import statements.
from globals import friends
from globals import Spy
from spy_details import spy
from termcolor import colored
import re      # for regular expression
# add new friends.
def add_friend():
    new_friend=Spy('','.',0,0.0,False)
    tempcheck = True # it can be used as Temporary variable
    # Defining use of RE
    patternsalutation = '^Mr|Ms$'
    patternname = '^[A-Za-z][A-Za-z\s]+$'
    patternage = '^[0-9]+$'
    patternrating = '^[0-9]+\.[0-9]$'
        # Validating Each Values Using Regular Expression
        while tempcheck:
            salutation = input(" Are you  Mr. or Ms.? : ")
            if (re.match(patternsalutation, salutation) != None):
                tempcheck = False
            else:
                print(colored("Wrong entry.Enter Again!", 'red'))
        tempcheck = True
        while tempcheck:
            new_friend['name'] = input("Please add your friend's name: ")
            if (re.match(patternname, new_friend['name']) != None):
                tempcheck = False
            else:
                print(colored("Wrong entry.Enter Again!", 'red'))

        # concatenation.
        new_friend['name'] = new_friend['salutation'] + "." + new_friend['name']
        tempcheck = True
        while tempcheck:
            new_friend['age'] = input("What is your Age?:")
            if (re.match(patternage, new_friend['age']) != None):
                tempcheck = False
                new_friend['age'] = int(new_friend['age'])
            else:
                print(colored("Wrong entry.Enter Again!", 'red'))
        tempcheck = True  # temporary variable
        while tempcheck:
            new_friend['rating'] = input("What is your Spy rating?")
            if (re.match(patternrating, new_friend['rating']) != None):
                tempcheck = False
                new_friend['rating'] = float(new_friend['rating'])
            else:
                print(colored("Wrong choice.Enter Again!", 'red'))
   # new_friend  = {
    #    'name': '',
     #   'salutation': '.',
      #  'age': 0,
       # 'rating': 0.0,
        #'is_online': False
    #}


    # users input validations
        if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
            friends.append(new_friend)
            print ('Friend Added!','green')    # Success msg
        else:
            print ('Sorry! Invalid entry. We can\'t add spy with the details you provided','red') # Error msg

    # returning total no of friends.
        return len(friends)
