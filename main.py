print("Let's get started!")
spy_name=input("Provide your name here :")
# check whether spy has input something or not
if len(spy_name) > 0:
    #code block if the condition is true.
    # concatenation of salutation and name
    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_salutation = input("What should we call you :")
    spy_age=input("Enter your age. ?")
    print (type(spy_age))
    spy_age=int(spy_age)
    print(spy_age)
    spy_name = (spy_salutation + " " + spy_name)
    print('Welcome'  + spy_name  +  "Glad to have you back with us.")
    print("Alright"  + spy_name  +  "I would like to know little bit about you before we proceed.")
else:
    print(" Invalid name. Try again.")