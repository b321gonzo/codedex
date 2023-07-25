import random
import time

# print("")
# print("Let's play a game.")
# time.sleep(1.5)
# print("")
# print("In this game we have 20 spots.")
# time.sleep(1.5)
# print("")

# #print blank list
# for i in (range(1,21)):
#     print(str(i)+".")
#     time.sleep(0.2)

# print("")
# print("I will generate a random integer between and including 1 and 1000.")
# time.sleep(3)

# print("")
# print("You will decide which of the 20 spots to place that random number.")
# time.sleep(3)

# print("")
# print("The objective of the game is to place all generated numbers in numerical order.")
# time.sleep(3)

# print("")
# print("When you choose a spot, that choice is locked in.")
# time.sleep(3)

# print("")
# print("If you meet the objective, you win; but if you can't place a number in the correct order you lose.")
# time.sleep(3.5)

# print("")
# print("Let's begin.")
# time.sleep(1.5)

#setting up "empty" list. This is to keep track of where the genrated numbers are placed
ordering = ["","","","","","","","","","","","","","","","","","","",""]

generated_number = random.randint(1,1000)
logn = [generated_number] #logn stands for "List of Generated Numbers"
logn_sorted = [generated_number]

print("")
print("Random number:")
print(generated_number)

print("")
position_choice = int(input("Which spot (1-20) do you want to place the random number? "))

ordering[position_choice-1] = generated_number

locp = [position_choice] #locp stands for "List of Chosen Positions"

ordering_stripped = ordering.copy()
for i in range(1,ordering_stripped.count("")+1):
    ordering_stripped.remove("")

print("")

for i in range(1,21):
    print(str(i)+". "+str(ordering[i-1]))

while ordering_stripped==logn_sorted:
    
    generated_number = random.randint(1,1000)
    
    logn.append(generated_number)
    logn_sorted=logn.copy()
    logn_sorted.sort()

    print("")
    print("Random number:")
    print(generated_number)

    print("")
    position_choice = int(input("Which spot (1-20) do you want to place the random number? "))

    ordering[position_choice-1] = generated_number

    locp.append(position_choice)

    ordering_stripped = ordering.copy()
    for i in range(1,ordering_stripped.count("")+1):
        ordering_stripped.remove("")

    print("")

    for i in range(1,21):
        print(str(i)+". "+str(ordering[i-1]))




