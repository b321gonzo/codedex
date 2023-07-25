gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("  1) Dawn")
print("  2) Dusk")
print("")
q1 = int(input())
print("")

if q1 == 1:
    gryffindor = gryffindor+1 
    ravenclaw = ravenclaw+1
elif q1 == 2:
    hufflepuff = hufflepuff+1 
    slytherin = slytherin+1
else:
    print("Wrong input.")

print("Q2) When I'm dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")
print("")
q2 = int(input(""))
print("")

if q2 == 1:
    hufflepuff = hufflepuff+2
elif q2 == 2:
    slytherin = slytherin+2
elif q2 == 3:
    ravenclaw = ravenclaw+2
elif q2 == 4:
    gryffindor = gryffindor+2
else:
    print("Wrong input.")

print("Q3) Which kind of instrument most pleases your ear?")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")
print("")
q3 = int(input(""))
print("")

if q3 == 1:
    slytherin = slytherin+4
elif q3 == 2:
    hufflepuff = hufflepuff+4
elif q3 == 3:
    ravenclaw = ravenclaw+4
elif q3 == 4:
    gryffindor = gryffindor+4
else:
    print("Wrong input.")

if gryffindor>slytherin and gryffindor>ravenclaw and gryffindor>hufflepuff:
    print("You are a Gryffindor!")
elif slytherin>ravenclaw and slytherin>hufflepuff:
    print("You are a Slytherin!")
elif ravenclaw>hufflepuff:
    print("You are a Ravenclaw!")
elif hufflepuff>gryffindor:
    print("You are a Hufflepuff!")
else:
    print("ERROR")
