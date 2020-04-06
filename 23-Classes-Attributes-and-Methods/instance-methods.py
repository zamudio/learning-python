class Pokemon():
    def __init__(self, name, speciality, health=100):
        self.name = name
        self.speciality = speciality
        self.health = health

    def roar(self):
        print('Raaaaawwwr!')

    def describe(self):
        print(f'I am {self.name}, I use {self.speciality}')


squirtle = Pokemon('Squirtle', 'Water')
charmander = Pokemon('Charmander', 'Fire')

squirtle.describe()
