# import statements
from spy_details import spy
from start_chat import start_chat
#from globals import Spy
from termcolor import colored
import re
print "Let's get started!"
repeat=True
while repeat:
    question = "Do you want to continue as" + spy['salutation'] + " " + spy['name'] + "(Y/N) ?: "
    existing = raw_input(question)

# validating user's input
    if (existing.upper() == 'Y') :
    # user want to continue as default user.
    # concatenation of salutation and name of spy
        spy_name = spy['salutation'] + " " + spy['name']
    # starting chat application
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])

    elif (existing.upper() == 'N') :
    # user wants to continue as a new user.
    # check whether spy has input something or not
        repeat=False
        wholecheck=True #temporary variable
        while wholecheck:
            tempcheck=True #again temporary variable
    # Validation Using Regex
            patternsalutation = '^Mr|Ms$'
            patternname = '^[A-Za-z][A-Za-z\s]+$'
            patternage = '^[0-9]+$'
            patternrating = '^[0-9]+\.[0-9]$'
    # validation using regular expression
            while tempcheck:
                spy['salutation']=raw_input("What should we call you Mr. or Mrs.:")
                if (re.match(patternsalutation, spy['salutation']) != None):
                    tempcheck = False
                else:
                    print colored("Wrong choice.Enter Again!!!!", 'red')
            tempcheck=True
            while tempcheck:
            spy['name']=raw_input("Provide your name here :")
                if (re.match(patternname, spy['name']) != None):
                    tempcheck = False
                else:
                    print colored("Your name is invalid.Enter Again!!!!", 'red')
     # concatenation of salutation and name of spy
            spy_name = spy['salutation'] + " " + spy['name']
            tempcheck=True
            while tempcheck:
                spy['age'] = raw_input("Enter your age:")
                if (re.match(patternage, spy['age']) != None):
                    tempcheck = False
                else:
                    print colored("Invalid age.Enter Again!!!!", 'red')
            tempcheck = True
            while tempcheck:
                spy['rating'] = float(raw_input("What is your Spy rating ?"))
                 if (re.match(patternrating, spy['rating']) != None):
                    tempcheck = False
                else:
                    print colored("Your rating does not match.Enter Again!!!!", 'red')
            spy['is_online'] = True
            wholecheck = False
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
