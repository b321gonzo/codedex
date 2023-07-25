import random

possibilities = ['🍒','🍇','🍉','7️⃣']

play = True

while play:
    results = random.choices(possibilities,k=3)
    print(results[0] + "  | " + results[1] + "  | " + results[2])
    if results[0] == '7️⃣' and results [1] == '7️⃣' and results[2] == '7️⃣':
        print("Jackpot!")
    else:
        print("Thank you for playing!")
    play_again = input("Do you wish to play again? (Y/N)")
    if play_again != "Y":
        play = False

