info = {
    'name': 'BBQ Chicken',
    'price': 19.99,
    'size': 'XL',
    'ingredients': ['chicken', 'bbq sauce']
}


class Pizza():
    def __init__(self, info):
        for k, v in info.items():
            setattr(self, k, v)


bbq = Pizza(info)
print(bbq.name)
print(bbq.size)
