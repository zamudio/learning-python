class Guitar():
    def __init__(self, name, wood_type, strings, year):
        self.name = name
        self.wood_type = wood_type
        self.strings = strings
        self.year = year
        print(
            f'A new guitar is being created! This object is a {name} made of {wood_type} wood, with {strings} strings, and made in the year {year}')


acoustic = Guitar('Fender', 'Mahogany', 6, 1990)
jazz = Guitar('Gibson', 'Cherry', 6, 1974)

print(acoustic.name)
