

def func_1(x):
    return x ** 2

x = 2

y = func_1(x)
print(y)

print('\n', '.' * 50, '\n')

def func_2(c):
    return c ** 3

c = 7

y = func_2                        # Можна спочатку оголошувати функцію, а потом передавати значення
z = y(c)
print(z)

print('\n', '.' * 50, '\n')


def func_3(s, f = 0):
    return s + f ** (s + f)

y = func_3(3)
v = func_3(s = 4, f = 4)
b = func_3(5, f = 2)
print(y, v, b)

print('\n', '.' * 50, '\n')

def func_4(x, *args, f = 0, **kwargs):
    print('Видасть початок як список: ',args)
    print('Видасть кінцівку як tuple: ', kwargs)
    return (x + f) ** (x + f)

y = func_4(1, 2, 3, 4, 5, f = 2, r = 5, t = 1)
print(y)
print('\n', '.' * 50, '\n')

empty_list = []
def add_to_list(f):
    empty_list.append(f)     #  Тут модифікується список, тому повертати нічого не треба


add_to_list('ffff')          #  Результатом функціє є модивікаця списку.
add_to_list('0000')          #  Кожен викли - чергова модифікація
add_to_list('aaaa')
print(empty_list)

print('\n', '.' * 50, '\n')

new_list = [
    func_2(2)
    ]

new_list.append(func_2(4))   #  Ще варіант зміни елементу функцією

print(new_list)

g = func_2(func_2(2) + 5)    #  Функція як аргумент
print(g)

print('\n', '.' * 50, '\n')



def func_without_args():             # Функції, які не потребують аргументу, а виконують дію
    print('Hi Andriy!')
hello = func_without_args()
print(hello)

print('\n', '.' * 50, '\n')

'''
import requests
def check_google_liave():
    rs = requests.get("https://8.8.8.8")
    return rs.status_code

check_google_liave()
'''

print('\n', '.' * 50, '\n')


def counter():              #
    x = 0
    def incr():             # Збільшити щось на 1, кожен раз
        nonlocal x
        x += 1
        return x
    return incr

f = counter()
print(f())
