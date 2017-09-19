# import statements.
from globals import friends
#from globals import Spy
#from spy_details import spy
from termcolor import colored
import re      # for regular expression
# add new friends.
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '.',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    wholecheck = True # it can be used as Temporary variable
    # Defining use of RE
    tempcheck = True
    patternsalutation = '^Mr|Ms$'
    patternname = '^[A-Za-z][A-Za-z\s]+$'
    patternage = '^[0-9]+$'
    patternrating = '^[0-9]+\.[0-9]$'
        # Validating Each Values Using Regular Expression
        while tempcheck:
            new_friend['salutation'] = raw_input(" Are you  Mr. or Ms.? : ")
            if (re.match(patternsalutation, new_friend['salutation']) != None):
                tempcheck = False
            else:
                print colored("Wrong entry.Enter Again!", 'red')
            new_friend['name'] = new_friend['salutation'] + "." + new_friend['name']   # concatenation.
        tempcheck = True
        while tempcheck:
            new_friend['name'] = raw_input("Please add your friend's name: ")
            if (re.match(patternname, new_friend['name']) != None):
                tempcheck = False
            else:
                print(colored("Wrong entry.Enter Again!", 'red'))
         while tempcheck:
            new_friend['age'] = raw_input("What is your Age?:")
            if (re.match(patternage, new_friend['age']) != None):
                tempcheck = False
            else:
                print(colored("Wrong entry.Enter Again!", 'red'))
        tempcheck = True  # temporary variable
        while tempcheck:
            new_friend['rating'] = raw_input("What is your Spy rating?")
            if (re.match(patternrating, new_friend['rating']) != None):
                tempcheck = False
                wholecheck = False
            else:
                print colored("Wrong choice.Enter Again!", 'red')
             # users input validations
        if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
            friends.append(new_friend)
            print ('Friend Added!','green')    # Success msg
        else:
            print colored ('Sorry! Invalid entry. We can\'t add spy with the details you provided','red') # Error msg

    # returning total no of friends.
        return len(friends)
