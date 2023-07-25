def dog_years(name,age):
  human_age=age*7
  answer=name+" is "+str(human_age)+" years old in human years."
  return(answer)

print(dog_years("Bingo",3))

def dog_years2(name,age):
  human_age=age*7
  print(name,'is',str(human_age),'years old in human years.')

dog_years2("Bingo",3)