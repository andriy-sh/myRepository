
# Errors and Exceptions
'''
a = input("Введи дату: ")

try:
    a = int(a)
except ValueError:
    print("Введи цифру Дебіл!")

print('\n', '*' * 100, '\n')

'''

# Викликаємо самі помилку та відразу ловимо її
try:
    raise NameError
except NameError:
    print("Take NameError")





print('\n', '*' * 100, '\n')



# Сама помилка це є обєктом, тому їй можна передавати якісь значення

try:
    raise IndexError('11111111111')
except IndexError as err:
    print(err)

#
#
#

# Розширюємо кількість існуючих варіантів помилок. Задаємо новий клас, який є обєктом
'''
class NonIntegerError(Exception):
    def __init__(self, string_value):
        super(NonIntegerError, self).__init__(
        "Incorrect input value: %s" % string_value)

def convert_to_int(string):
    try:
        return int(string)
    except ValueError:
        raise NonIntegerError(string)

while True:
    try: print(convert_to_int(input("Some texy: ")))
    except NonIntegerError as err:
        print(err)

'''
print('\n', '*' * 100, '\n')

# Homework

import string

credent = {'user': 'qwerty', 'admin': '123456', 'guest' : 'test'}


while True:
    try:
        user_name = input("Username: ")

        if not user_name.strip():                   # Убирає пробіли по бокам
            raise RuntimeError

        pwd = credent[user_name]

        passwd = input("Password: ")
        if not passwd.strip() == pwd:
            if input('Do you want change password (y/[n])?').strip().lower() == 'y':
                new_passwd = input("Input new password: ").strip()
                if new_passwd:
                    (credent[user_name]) = new_passwd
                    print(new_passwd)

            else:
                print("Incorrect password")
                continue
        else:
            continue


    except RuntimeError:
        print("Username is empty!")
    except KeyError:
        print("Invalid username!")




