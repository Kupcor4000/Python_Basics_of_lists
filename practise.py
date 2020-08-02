CONDITION = "N"

#TODO Create an empty list to maintain the player names
player_names = []


    #TODO Ask the user if they'd like to add players to the list
user_input_1 = input("Would you like to add player to team 'roaster'? If yes type 'y', if no type 'n' : ")
user_input_1 = user_input_1.upper()
    #If the user answer "Yes", let them type in a name and add it to the list
while user_input_1 != CONDITION :
    new_player = input("Please enter the name of player you want to add to the list: ")
    player_names.append(new_player)
    user_input_1 = input("Would you like to add another player to team 'roaster'? If yes type 'y', if no type 'n' : ")

#If the user answers "No", print out the team 'roster'
if len(player_names) == 0:
    print("Your team 'roaster' has no players!")
else:
#TODO print the number of players on the team
    print("The team has {} members!".format(len(player_names)))
#TODO Print the player number and the player name
    print("The team roaster: ")
    for i in range(len(player_names)):
        print("{} : zawodnik: {}".format(i+1,player_names[i]))
#The player number should start at the number one

#TODO Select a goalkeeper form the above rosaster
    goalkeeper = int(input("Please select the player who will be a goalkeeper of the team roaster (type number of this player): "))
    
#TODO Print the goalkeeper's name
    print("A {} is a goalkeepr!".format(player_names[goalkeeper-1]))