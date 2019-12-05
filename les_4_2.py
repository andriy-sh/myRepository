def outer():
    x = 'local'

    def inner():
        nonlocal x              # Перевизначає змінну на рівень вище
        x = 'nonlocal'
        print('inner: ', x)

    inner()
    print('outer: ', x)

outer()


# Функція лічільник

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

a = make_counter()

print(a())                      # Так викликати, т.к. а отримала за заначення функцію
print(a())
print(a())
