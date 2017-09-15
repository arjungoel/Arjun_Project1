# import statements
from spy_details import spy
from start_chat import start_chat
print("Let's get started!")
question=("Do you want to continue as" + spy['salutation'] + " " + spy['name'] + "(Y/N) : ")
existing=input(question)

# validating user's input
if (existing == 'Y') :
    # user want to continue as default user.

    # concatenation of salutation and name of spy
    spy_name = spy['salutation'] + " " + spy['name']
    # starting chat application.
    start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online'])
elif (existing == 'N') :
    # user wants to continue as a new user.
    spy['name']=input("Provide your name here :")

    # check whether spy has input something or not
    if len(spy['name']) > 0:

        spy['salutation'] = input("What should we call you :")
        while True:
            try:
                spy['age'] = int(input("Enter your age. ?")) # typecasting of users input is done.
                break
            except ValueError:
                print("Invalid age.Try again")
        # concatenation of salutation and name of spy
        spy_name = spy['salutation'] + " " + spy['name']

        spy['rating']=float(input("What is your spy rating :")) # typecasting is done here.
        spy['is_online']=True

        # starting chat application
        start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online'])
    else:
        print(" Invalid name. Try again.")
else:
    print("Wrong choice. Try again.")
