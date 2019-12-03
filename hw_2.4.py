# Розбиваємо ІР адресу по частинам. Варіант 1.
str1 = "192.168.11.12"
ip_adr0 = str1.split('.')

print(ip_adr0)
print('_' * 100)

#
# Розбиваємо ІР адресу по частинам. Варіант 2.
ip_adr1 = "22.68.101.212".split('.')

print(ip_adr1)
print('_' * 100)

#
# Навчання списки

L = list(range(-5, 31))  # Якщо застосовувати join до списку, який був згенерований за допомогою  range
# то буде видавати помилку.
print(L)

L1 = list("sodjfkdsmcm")

str2 = ''.join(L1)
print(str2)

Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('\n'.join(map(str, Matrix)))  # Розібратись з функцією MAP

print(Matrix[1][2])
S = Matrix.append([1, 3])
Matrix.extend([4, 3, 78])  # функція .extend не повертає нічого

print(Matrix)

C = Matrix.count(4)
print(Matrix, "скільки 4 в матриці? Відповідь:",
      C)  # Тут інші 4 не рахує, т.к. в інших місцях, де 4 - це списки, а не окремі значення

Matrix.insert(2, 2222)
print("функція insert нічого не повертає")

I = Matrix.index(3)
print(Matrix)
print(I)


l = [5, 7, 3, 1, 2]
l.sort()
print(l)

# Генератори списків
print('Генератори списків')

rew = [x * 4 for x in 'SPAM']
print('rew = ', rew)


res = []
for x in "SPAM":
    res.append(x * 4)

print(res)


ret = list(map(abs, [-1, -2, 3, -6, 7, 8, -9.5]))              #  Виконання функції абс над полсідовністю
print(ret)


# Зрізи та індекси, та інше
mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mx)
print(mx[1][2])

mx[2] = [0, 1, 1]                                              # Не є функцію для додавання нового значення по індесу
print(mx)                                                      # лише робить заміну по існуючому індеску, з індекос 3 видасть помилку


v =  [1, 2, 3]                                                 # такой фокус действует, по факту 2 значения вклинились
v[1:2] = [4, 5]
print(v)

v.pop(2)
print(v)
