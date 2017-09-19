from globals import friends
#from termcolor import colored
# function defintion
def select_friend():
    counter = 1
    for friend in friends:   # friend is working as a temporary variable..
        print str(counter) + ". " + friend['name'] + "Age : " + str(friend['age']
        counter  = counter + 1

    result=int(raw_input("Select a friend from the list:"))
    return result-1



