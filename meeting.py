attendees = []
list_created_by_my_friend = ["Lukas","Erich","Magda","Ola","Marlena","August"]
do_you_want_to_end = "NO"
while do_you_want_to_end != "YES":
    attendees.append(input("Please enter the name of the next attendee: "))
    do_you_want_to_end = input("Plese type 'yes' if you finish, otherwise type 'no' and press enter: ")
    do_you_want_to_end = do_you_want_to_end.upper()
print("There are {} attendees on your list!".format(len(attendees)))
attendees.extend(list_created_by_my_friend)
print("When you add your list and your friend's list you will have {} attendees!".format(len(attendees)))
for i in range(len(attendees)):
    print("{} : {}".format(i+1,attendees[i]))
    