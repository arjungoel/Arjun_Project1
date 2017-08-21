from globals import friends

# function defintion
def select_friend():
    counter = 1
    for friend in friends:   # friend is working as a temporary variable..
        print (str(counter) + ". " + friend['name'] + "Age : " + str(friend['age'])
        counter = counter + 1

    result = int(input("Select from the list : "))
    return result - 1

