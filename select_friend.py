from globals import friends
from termcolor import colored
# function defintion
def select_friend():
    counter = 1
    for friend in friends:   # friend is working as a temporary variable..
        print (str(counter) + ". " + friend['name'] + "Age : " + str(friend['age'])
        counter  = counter + 1

    if(counter > 1):
        temp1 = True
        while temp1:
            result = int(input("Select from the list : "))
            if(result < counter):
                temp1 = False
            else:
                print(colored("Corrected Value:",'red'))
        else:
            return result - 1

