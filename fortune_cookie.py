def fortune():
    import random
    fortune = ["Don't pursue happiness - create it.",
               'All things are difficult before they are easy.',
               "The early bird gets the worm, but the second mouse gets the cheese",
               'If you eat something and nobody sees you eat it, it has no calories,',
               'Someone in your life needs a letter from you.',
               "Don't just think. Act!",
               "Your heart will skip a beat.",
               "The fortune you search for is in another cookie.",
               "Help! I'm being held prisoner in a Chinese bakery!"]
    print(fortune[random.randint(0,len(fortune)-1)])

fortune()
fortune()
fortune()
fortune()
fortune()
fortune()
fortune()
fortune()