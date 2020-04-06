class Sushi():
    def __init__(self):
        self = self

    @classmethod
    def lunch(cls):
        return cls()


lunch = Sushi.lunch()
