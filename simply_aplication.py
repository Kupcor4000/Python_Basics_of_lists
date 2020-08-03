#Shooping list
import time
import os

#funkcja polegajaca na dodawaniu obiektów
def add_to_list(list1):
    user_item = input("Please type a name of product which do you want to add to your list: ")
    list1.append(user_item)
    
#funkcja pokazujaca aktualna zawartosc listy
def show_list(list2):
    for i in range(len(list2)):
            print("{} : {}".format(i+1,list2[i]))
    

CONDITION = "DONE"
ADD = "ADD"
SHOW = "SHOW"
HELP = "HELP"

shopping_list = []
help_sequence = "The sequence which explain to user how aplication works"
user_input = "NOT DONE"

while user_input != CONDITION:
    #TODO User should now a total lenght of his list
    print("_________________________________________________________________________________")
    print("Actualy length of your shopping list is: {} positions!".format(len(shopping_list)))
    #TODO user should be contunually prompted so that he can add a grocery item or view list when he need to
    print("")
    print("What do you want to do? Type 'show' and press enter to see a list or type 'add' and press enter to add a product to your list")
    print("You can also type 'help' so that we write to you how this app works")
    user_input = input()
    user_input = user_input.upper()
    os.system("clear")
    #TODO User should be able to ask for help so that he can understand how to use the application
    if user_input == HELP:
        print(help_sequence)
        
    #TODO User shoudl be able to add an item to the list
    elif user_input == ADD:
        add_to_list(shopping_list)
        os.system("clear")
        
    #TODO User should see a actual list at any time so that he can veryfy order
    elif user_input == SHOW:
        print("Actual shopping list: ")
        show_list(shopping_list)
        
            
    #TODO User should be able to state DONE when it finish, so that he can print a list
    elif user_input == CONDITION:
        print("Your final shopping list: ")
        show_list(shopping_list)
        print("Thanks for using our app!")
    else:
        print("Przykro mi nie ma takiej komendy, proszę wybrać cos ponownie!")