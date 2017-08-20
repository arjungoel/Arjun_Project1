# import statements
# from globals import current_status_message
from add_status import add_status
from add_friend import add_friend

# start_chat() function definition..
def start_chat(name,age,rating,status):
    from globals import current_status_message
    # validating users details.
    show_menu=True
    while(show_menu):
        menu_choices = ("What do you want to do ? \n 1. Add Status \n 2. Close Application")
        result = int(input(menu_choices))
        # validating users input..
        if (result == 1):
        # action 1
            pass
        elif (result == 2):
            show_menu=False
        else:
            print("Wrong choice. Try again.")
