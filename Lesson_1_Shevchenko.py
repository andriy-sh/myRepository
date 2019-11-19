# TASK 1  -

str1 = "ecnalubma"
print(str1)
len_str1 = len(str1)

# Metod 1
str1_revers1 = str1[::-1 ]                              # читаем символы с конца
print(str1_revers1)

# Metod 2
str1_revers2 = str1[len_str1 : - len_str1 - 1 : -1]     # перебираем символы с конца, но указываем начало и конец слайса.
print(str1_revers2)                                     # При обратном проходе они меняются местами


# Metod 3
my_list = list(str1)                                     # Преобразовуем строку в список. Применяем к списку реверс
print(my_list)
my_list.reverse()
str1_revers3 = ''.join(my_list)                         # обратное преобразовуем в строку
print(str1_revers3)

# Metod 4
str1_revers4 = str1[8] + str1[7] + str1[6] + str1[5] + str1[4] + str1[3] + str1[2] + str1[1] + str1[0]
print(str1_revers4)                                     # фантазия закончилась =))))

print('_' * 100)
