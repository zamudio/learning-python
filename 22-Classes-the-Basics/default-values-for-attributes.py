class Book():
    def __init__(self, title, author, price=14.99):
        self.title = title
        self.author = author
        self.price = price


gatsby = Book('The Great Gatsby', 'F. Scott Fitzgerald')
animal_farm = Book('Animal Farm', 'George Orwell', 19.84)

print(f'{animal_farm.title} by {animal_farm.author}, available for only ${animal_farm.price}!')
print(f'{gatsby.title} by {gatsby.author}, available for only ${gatsby.price}!')
