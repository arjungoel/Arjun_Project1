# import statements
from spy_details import spy
from start_chat import start_chat
from globals import Spy
from termcolor import colored
import re
print("Let's get started!")
whole=True
while True:
    question=("Do you want to continue as" + spy['salutation'] + " " + spy['name'] + "(Y/N) ?: ")
    existing=input(question)

# validating user's input
if (existing == 'Y') :
    # user want to continue as default user.
    whole=False
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])


    # starting chat application.

elif (existing == 'N') :
    # user wants to continue as a new user.
    whole=False
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
            spy['salutation']=input("What should we call you Mr. or Mrs.:")
            if (re.match(patternsalutation, salutation) != None):
                tempcheck = False
            else:
                print(colored("Enter Again!!!!", 'red'))
        tempcheck=True
        while tempcheck:
            spy['name']=input("Provide your name here :")
            if (re.match(patternname, spy['name']) != None):
                tempcheck = False
            else:
                print(colored("Enter Again!!!!", 'red'))
     # concatenation of salutation and name of spy
        spy_name = spy['salutation'] + " " + spy['name']
        tempcheck=True
        while tempcheck:
            spy['age'] = input("Enter your age:")
            if (re.match(patternage, spy['age']) != None):
                tempcheck = False
                spy['age'] = int(spy['age'])
            else:
                print(colored("Enter Again!!!!", 'red'))
        tempcheck = True
        while tempcheck:
            spy['rating'] = float(input("What is your Spy rating ?"))
            spy['is_online']=True
            if (re.match(patternrating, spy['rating']) != None):
                tempcheck = False
                spy['rating'] = float(spy['rating'])
            else:
                print(colored("Enter Again!!!!", 'red'))
        # Checking If Spy is eligible
        if spy['rating'] <= 5.0 and spy['age'] > 12 and spy['age'] < 50:
            start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
            wholecheck = False
        else:
            print(colored("Invalid name. Try again!", 'red'))
    else:
        print(colored("Wrong choice. Try again!", 'red'))


    # check whether spy has input something or not
    #if len(spy['name']) > 0:

    #    spy['salutation'] = input("What should we call you :")
     #   while True:
      #      try:
       #         spy['age'] = int(input("Enter your age. ?")) # typecasting of users input is done.
        #        break
         #   except ValueError:
          #      print("Invalid age.Try again",'red')
        # concatenation of salutation and name of spy
        #spy_name = spy['salutation'] + " " + spy['name']

       # spy['rating']=float(input("What is your spy rating :")) # typecasting is done here.
        #spy['is_online']=True

        # starting chat application
   #     start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online'])
  #  else:
 #       print(" Invalid name. Try again.",'red')
#else:
  #  print("Wrong choice. Try again.",'red')
