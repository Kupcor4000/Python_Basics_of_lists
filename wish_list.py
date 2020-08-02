books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

#the last element of every list, independent of their lenght
print("Last element in list: {}".format(books[len(books)-1]))
books.insert(0,"Portret Doriana Graya by Oscar Wild")
books.insert(2,"Człowiek w poszukiwaniu sensu by Frankl")
recomendation = []
recomendation.append(books[0])
recomendation.append(books[1])
books.pop(0)
print("List after books changes: {}".format(books))
print("List of recomended books: {}".format(recomendation))