import math
import sys


planet = {"Mercury": {"speed": 47.87,"radius": 58}, "Venus": {"speed": 35.02,"radius": 108}, "Earth": {"speed": 29.78 ,"radius": 150},
          "Mars": {"speed": 24.13,"radius": 228}, "Jupiter" : {"speed": 13.07,"radius": 778}, "Saturn": {"speed": 9.69,"radius": 1429},
          "Uranus": {"speed": 6.81,"radius": 2871}, "Neptune": {"speed": 5.43,"radius": 4504}}

input("Planet 1: ")

def convert_days_in_year(planet):
    radius =

planet_year1 = 2 * math.pi * orbital_radius_1 / orbital_speed_1
planet_year1 = planet_year1 / (60 * 60 * 24) # converting seconds to days


def biggest_planet_year(planet):


orbital_radius_1 = orbital_radius[planet1] * 1000000  # turning millions of kilometres to kilometres
orbital_speed_1 = orbital_speed[planet1]


planet2 = input("Planet 2: ")
orbital_radius_2 = orbital_radius[planet2] * 1000000 # turning millions of kilometres to kilometres
orbital_speed_2 = orbital_speed[planet2]

planet_year2 = 2 * math.pi * orbital_radius_2 / orbital_speed_2
planet_year2 = planet_year2 / (60 * 60 * 24) # converting seconds to days

print("The year is {} days on {}".format(int(planet_year1), planet1))
print("The year is {} days on {}".format(int(planet_year2), planet2))

bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger

print("The {} year is bigger".format(bigger_year))
