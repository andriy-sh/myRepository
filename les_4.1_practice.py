import math

def days_in_year(pl_radius, pl_speed):
    ''' Calculate how match days in year on the planet '''

    planet_year = (2 * math.pi * (pl_radius * (10 ** 6))) / (pl_speed * 8640)
    return planet_year
    #return print("Days in year = ", planet_year)

def bigger_year(first_planet_years, second_planet_years):
    ''' Calculate which planet bigger '''
    bigger_year = 1 if first_planet_years > second_planet_years else 2  # Looking which year is bigger
    print("The {} planet's year is bigger".format(bigger_year))


planet_db = {"Mercury": {"speed": 47.87,"radius": 58}, "Venus": {"speed": 35.02,"radius": 108}, "Earth": {"speed": 29.78 ,"radius": 150},
          "Mars": {"speed": 24.13,"radius": 228}, "Jupiter" : {"speed": 13.07,"radius": 778}, "Saturn": {"speed": 9.69,"radius": 1429},
          "Uranus": {"speed": 6.81,"radius": 2871}, "Neptune": {"speed": 5.43,"radius": 4504}}
#
#
# Calculate for fist planet
planet = input("Input 1st planet name for calculate days in year: ")

pl_radius = planet_db[planet]["radius"]
pl_speed = planet_db[planet]["speed"]

print("The {}'s R = {}, C = {}".format(planet, int(pl_radius), int(pl_speed)))

first_planet_years = days_in_year(pl_radius, pl_speed)
print("The {}'s has {} planet years".format(planet, int(first_planet_years)))

#
#
# Calculate for second planet
planet = input("Input 2nd planet name for calculate days in year: ")

pl_radius = planet_db[planet]["radius"]
pl_speed = planet_db[planet]["speed"]

print("The {}'s R = {}, C = {}".format(planet, int(pl_radius), int(pl_speed)))

second_planet_years = days_in_year(pl_radius, pl_speed)
print("The {}'s has {} planet years".format(planet, int(second_planet_years)))


bigger_year(first_planet_years, second_planet_years)









