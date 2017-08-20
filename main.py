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
        # input more details about user.
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_salutation = input("What should we call you :")
        spy_age = input("Enter your age. ?")
        print(type(spy_age))
        spy_age = int(spy_age)
        print(spy_age)
        spy_name = (spy_salutation + " " + spy_name)
        print('Welcome' + spy_name + "Glad to have you back with us.")
        print("Alright" + spy_name + "I would like to know little bit about you before we proceed.")
    else:
        print(" Invalid name. Try again.")
else:
    print("Wrong choice. Try again.")
