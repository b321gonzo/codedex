from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

rlist = [
    2440,
    6052,
    6371,
    3390,
    58232
]

random_planet = ch(planets)

r = rlist[planets.index(random_planet)]

sa = round(4*pi*r)

print(random_planet + ' has a surface area of about ' + str(sa) + ' square kilometers.')