
class Restaurant:
    name = ''
    type = ''
    rating = 0.0
    delivery = False


bob_burgers = Restaurant()
bob_burgers.name='Bob\'s Burgers'
bob_burgers.type='American Diner'
bob_burgers.rating=4.7
bob_burgers.delivery=False

print(vars(bob_burgers))