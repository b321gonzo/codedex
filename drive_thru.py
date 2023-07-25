

menu=['🍔 Cheeseburger',
      '🍟 Fries',
      '🥤 Soda',
      '🍦 Ice Cream',
      '🍪 Cookie']

def get_item(x):
    return(menu[x-1])

def welcome():
    print("Welcome to the drive-thru. Here is our menu:")
    for i in (range(1,6)):
        print(i,get_item(i))

welcome()

order=int(input("What number would you like to order?"))

print(get_item(order))