# LESSON 1
print("Lesson 1")

var1 = 14
print(type(var1), id(var1))

check = var1 is True  # В чому суть перевірки на Правда, Лож? Просто порівняння двох значень?
print(check)

check = var1 is False
print(check)

check = var1 is 14  # Порівнюю, чи є змінна рівною 23
print(check)

var2 = var1 or True  # Навіщо OR?
print(var2, id(var2))  # Можна побачити, що ідентифікатори var1 var2 однакові

check = var2 is True
print(check)

check = var2 is False
print(check)

print(var1 and var2)  # Взагалі не зрозуліло? Чомоу and??? Навіщо воно?

# LESSON 2
print("Lesson 2")
import math
import random

int_seq = random.sample(range(100), 5) # Генерує список з 5 елементів які берутся випадково з діапазону від 0 до 100

rand = random.uniform(2, 1024)  # Генерує випадкове число в діапазоні від а до б

float_random = random.random()  # Генерує випадкове число з плаваючою точкою

int_seq_max = max(int_seq)
floor_div_result = int_seq_max // float_random

print(int_seq)
print(rand)
print(float_random)
print(int_seq_max)
print(floor_div_result)
print(math.factorial(floor_div_result))


# LESSON 3
print("Lesson 3")

import string

text = string.ascii_letters + string.digits


print(text)

print(text[0])	    # Перший символ

print(text[-1])	    # Останній

print(text[2])      # Третій
print(text[-3])     # Третій з кінця

print(text[:8])		# Перші 8 символів

print(text[::3]) 	# Кожний 3

# ???????  Питання


# LESSON 4
print("Lesson 4")

lst = list(string.ascii_letters + string.digits)

print(lst)

print(lst[0])	    # Перший символ

print(lst[-1])	    # Останній символ

print(lst[2])       # 3й
print(lst[-3])      # 3й з кінця

print(lst[:10])		# по 10

print(lst[::2]) 	# кожний 2


print(lst.reverse())   # Метод не возвращает результат - видає 'None'

print(lst)




# LESSON 5
print("Lesson 5")

domain = {"Ukraine" : "UA", "Germany" : "D", "Russia" : "RU", "Britan" : "GB", "Uzbekistan" : "UZ"}

capital = {"Ukraine" : "Kyiv", "Germany" : "Berlin", "Russia" : "Moscow", "Britan" : "London", "Uzbekistan" : "Tashkent"}

print(domain)
print(capital)

print(domain.keys())

for key in domain.keys() :
    print("Domain for {} is {}". format(key, domain[key]))

for key in capital.keys() :
    print("The capital of {} is {}". format(key, capital[key]))

for key in domain.keys() :
    print (domain[key], capital[key])


for key in domain.keys() :
    print ("Domain for {} is {}, and capital {}". format(key, domain[key], capital[key]))

for key in domain.keys() :
    domain[key] = "COM." + domain[key]
print(domain)

# LESSON 6
print("Lesson 6")


set1 = set('ASDFGhjkl12345')  # що він взагалі видає? Випадково перемішує?
set2 = set('ASDFGerkl67890')

print(set1)
print(set2)

tpl_intersection = tuple(set1.intersection(set2)) # Первший відрізняється від другого такими симловами
print("Intersection:", tpl_intersection)

tpl_diff_1 = tuple(set1.difference(set2)) # Первший відрізняється від другого такими симловами
print
print("Difference 1:",tpl_diff_1)

tpl_diff_2 = tuple(set2.difference(set1)) # Другий відрізняється від другого такими симловами
print
print("Difference 2:",tpl_diff_2)

print(tpl_intersection[:3])

print(tpl_intersection[::-1])




# LESSON 7
print("Lesson 7")

# Створюємо файл з правати тільки на запис
f = open('/home/myfile.txt','w')

# Записуємо вираз текстовий в файл

f.write("Hello my world!")

# Закриваємо файл зі збереженням вмісту
f.close()

# Створюємо файловий обєкт для писання та читання
f = open('/home/myfile.txt','r+')

# Читаємо та виводимо вміст файлу
print(f.read())
f.seek(len("Hello "))

f.write("my " + "reaaaal world world!")

print(f.read())
f.flush()


