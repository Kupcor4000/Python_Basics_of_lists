def display_list(display_name,wishes):
    print(display_name +":")
    for ob in wishes:
        print(" * " + ob)
    print("\n Suggested wish: ")
    suggested_wish = wishes[0]                 # Należy pamiętać -  .pop() usuwa to element z listy!
    print("=======> " + suggested_wish + " <=========")
        


books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

#the last element of every list, independent of their lenght
print("Last element in list: {}".format(books[len(books)-1]))
books.insert(0,"Portret Doriana Graya by Oscar Wild")
books.insert(2,"Człowiek w poszukiwaniu sensu by Frankl")
recomendation = []
recomendation.append(books[0])
recomendation.append(books[1])

print("")
display_list("books",books)
print("")
display_list("video games",video_games)

    