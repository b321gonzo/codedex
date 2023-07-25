e_weight = float(input("What is your weight on Earth? "))

print("The following are the different destinations you may go to:")

destinations=['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for i in (range(0,7)):
  print(i+1,destinations[i])

choice = int(input("Choose the number that corresponds with the destination you would like to visit: "))

d_weight=float()

if choice == 1:
  d_weight=e_weight*(0.38)
elif choice == 2:
  d_weight=e_weight*(0.91)
elif choice == 3:
  d_weight=e_weight*(0.38)
elif choice == 4:
  d_weight=e_weight*(2.53)
elif choice == 5:
  d_weight=e_weight*(1.07)
elif choice == 6:
  d_weight=e_weight*(0.89)
else:
  d_weight=e_weight*(1.14)

print("Your weight on",destinations[choice-1],"is",d_weight)