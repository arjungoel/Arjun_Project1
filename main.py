print("Let's get started!")
spy_name=input("Provide your name here :")
spy_salutation=input("What should we call you :")
# check whether spy has input something or not
if len(spy_name) > 0:
    #code block if the condition is true.
# concatenation of salutation and name
spy_name=(spy_salutation  +  " "  +  spy_name)
print('Welcome'  + spy_name +  "Glad to have you back with us.")