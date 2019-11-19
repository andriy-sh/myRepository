
def car():
    def wheels():
        return 4
    return wheels

bmw = car()
bmw.color = 'black'
bmw.dors = 3
bmw.engine = '4x4'


print(bmw.__dict__)





print("*"*50)

#+++++++++++++++++++++++++++++++++++++++++++++++

import random

a = random.sample(range(0, 100), 5)
print(a)


