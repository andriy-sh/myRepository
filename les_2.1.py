var1 = 0

print(type(var1))
print(type(True))


# Видає False  в двох випадках, так як порівнює  int з bool, а тип var1 = int
print("var1 is True?", var1 is True)
print("var1 is False?", var1 is False)

var2 = var1

print("var2", var2 is True)
print(type(var2))

print("*"*50)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++

x1 = 23
x2 = 23
y = x1 is x2    #  True т.к. порівнює лише змінні в памяті
print(y)

print(id(x1), id(x2))
print("*"*50)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Зміна значень змінних місцями
a = 24
b = 37
print(a, b)
a, b = b, a

print(a, b)

print("*"*50)

# ++++++++++++++++++++

# *g  передає остаток символів в списку
a = [1, 2, 3, 4, 5, 6]
def ppprint(f, h, t, *g):
    print(f)
    print(h)
    print(t)
    print(g)

ppprint(*a)


print("*"*50)

def ppprint(f, h, t, *g, **jj):
    print(g)
    print(jj)

dict_test = {
    'site1': 'http:\\',
    'site2': 'https:\\',
    }

ppprint(*a, **dict_test)
