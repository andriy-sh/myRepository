# Задание 1: Посчитать количество гласных в каждом слове текста.
# Вывести максимальное количество гласных в одном слове

text = "Proineeeeeee eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

wordList = text.split()
print(wordList)

for word in wordList:
    print(word)
    letters = 'aeiouy'
    counter = 0
    for x in letters:
        counter += word.count(x)
    print(counter)

    check = counter
while check > counter:
   print('max =', check)
   print('_ _ ' * 30)


