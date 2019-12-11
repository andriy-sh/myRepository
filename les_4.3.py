spam = print('Hello!')          # Змінна виконує дію, але при цьому не має ніякого значення

print(None == spam)

#
# Передеча аргументів у функцію

def gg(i, o, p):                # Передача функції
    print(i, o, p)              # gg(i, o, p, *args, b = 1, c = 2, **kwargs)

gg(8, 9, 1)


def many(*args, **kwargs):
    print(args, '- Tuple')
    print(kwargs, '- Dict')

many(1, 2, 3, name = 'Mike', job = 'Analyst')


max_value_1 = max([1, 2, 3, 4], [3, 4, 5], key = len)       # В якості ключа можемо передавати різні умови
print(max_value_1)                                          # вибору по МАХ, МІН...

max_value_2 = max([1, 2, 3, 4], [3, 4, 5], key = sum)
print(max_value_2)


# Homework

str1 = 'dasflk;jdsaf;lkjad;lskfn;ladskf;lkjmads;lkcm lkjaenrdfsm'

ids = {'SHA-256': '2ae967fbac361667981cdac2aefdf8ee55f11de1e1a7f3943246b121b8198910', 'SHA-1': '222EF316E98C5A81E61A01D4A66225D55A39D256', 'MD5': '42a00e988e6e7fe39a837413f6bbbf30'}

def my_func(a, b, c = 2, **kwargs):
    print(a)
    print(b)
    print(c)
    print(**kwargs)


my_func(23, 45, ids)

# Next -  Порівняти значення та вивести квадрат значення
'''
lst = list("1327445634209759386427")
more_than = input('Input variable: ')

def art(lst, more_than):
    for i in lst:
        if i >= more_than:
            i = i ** 2
        else:
            print("Error")
    return i

art(lst, more_than)

'''

def multiply_me(n: int):
    '''Повернути результатит обчисленн: n + nn + nnn'''
    rt = n + n**2 + n**3
    return rt

a = multiply_me(4)
print(a)


def copy_me(n: int):
    '''Повернути дублювання значеннь по виду: n + nn + nnn'''
    s = str(n)
    сt = s + '+' + s*2 + '+' + s*3
    return сt

b = copy_me(6)
print(type(b), b)


def copy_sum(n: int):
    '''Повернути дублювання значеннь n  та провести розрахунок: n + nn + nnn'''
    s = str(n)
    ct = s + '+' + s*2 + '+' + s*3
    chart = ct.split('+')
    for el in chart:
        el = int(el)
    return sum(chart)

g = copy_sum(3)
print(type(b), g)
