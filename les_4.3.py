spam = print('Hello!')          # Змінна виконує дію, але при цьому не має ніякого значення

print(None == spam)
print('\n', '.' * 50, '\n')
#
# Передеча аргументів у функцію

def gg(i, o, p):                # Передача функції
    print(i, o, p)              # gg(i, o, p, *args, b = 1, c = 2, **kwargs)

gg(8, 9, 1)

print('\n', '.' * 50, '\n')

def many(*args, **kwargs):
    print(args, '- Tuple')
    print(kwargs, '- Dict')

many(1, 2, 3, name = 'Mike', job = 'Analyst')


max_value_1 = max([1, 2, 3, 4], [3, 4, 5], key = len)       # В якості ключа можемо передавати різні умови
print(max_value_1)                                          # вибору по МАХ, МІН...

max_value_2 = max([1, 2, 3, 4], [3, 4, 5], key = sum)
print(max_value_2)

print('\n', '.' * 50, '\n')

# Homework

str1 = 'dasflk;jdsaf;lkjad;lskfn;ladskf;lkjmads;lkcm lkjaenrdfsm'

ids = {'SHA-256': '2ae967fbac361667981cdac2aefdf8ee55f11de1e1a7f3943246b121b8198910', 'SHA-1': '222EF316E98C5A81E61A01D4A66225D55A39D256', 'MD5': '42a00e988e6e7fe39a837413f6bbbf30'}

def my_func(a, b, c = 2, **kwargs):
    print(a)
    print(b)
    print(c)
    print(**kwargs)


my_func(23, 45, ids)

print('\n', '.' * 50, '\n')

# Next -  Порівняти значення та вивести квадрат значення

lst = list("132445634209759386427")
more_than = input('Input variable: ')

def art(lst, more_than):
    ''' Дана функція перебирає список та порівнює кожне значення зі значенням яке ви ввели.
    Кожне значення, що більше заданого возводить до ступеня 2 та друкує '''

    for i in lst:
        if i >= more_than:
            i = int(i) ** 2                 # Змінюємо тип змінної, т.к. до цього це 'str' який не возводиться в ступінь 2
            print(i)
        else:
            pass
art(lst, more_than)

print('\n', '.' * 50, '\n')

def multiply_me(n: int):
    '''Повернути результатит обчислення формули: n + nn + nnn'''
    rt = n + n**2 + n**3
    return rt

a = multiply_me(4)
print(a)

print('\n', '.' * 50, '\n')

def copy_me(n: int):
    '''Повернути дублювання значеннь по виду: n + nn + nnn'''
    s = str(n)
    сt = s + '+' + s*2 + '+' + s*3
    return сt

b = copy_me(6)
print(type(b), b)

print('\n', '.' * 50, '\n')

# Функція дублює значення цифр та отриманні десятичні числа складає

summ = 0
def copy_sum(n: int):
    ''' Повернути дублювання значеннь n  та провести розрахунок: n + nn + nnn'''
    s = str(n)
    ct = s + '+' + s*2 + '+' + s*3
    chart = ct.split('+')
    print(chart)
    for el in chart:                    # Проходить по списку та кожне значення перетворює в int
        global summ                     # Задає глобально змінну, щоб внутрі функції визначити змінну summ
        el = int(el)
        summ = summ + el
    print(summ)
    return summ

copy_sum(7)
