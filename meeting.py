attendees = []
do_you_want_to_end = "NO"
while do_you_want_to_end != "YES":
    attendees.append(input("Please enter the name of the next attendee: "))
    do_you_want_to_end = input("Plese type 'yes' or 'no' and press enter: ")
    do_you_want_to_end = do_you_want_to_end.upper()
print("There are {} attendees!".format(len(attendees)))
for i in range(len(attendees)):
    print("{} : {}".format(i+1,attendees[i]))
    