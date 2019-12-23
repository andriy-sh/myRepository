# Decorators

def my_shiny_new_decorator(function_to_decorate):
# Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
# получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

stand_alone_function()

print('\n', '.' * 50, '\n')

stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()

print('\n', '.' * 50, '\n')

# Слідуючий запис спрощений запис попереднього, т.б.:
'''
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()
'''

@my_shiny_new_decorator                 # Даний запис передає функцію "another_stand_alone_function()"
def another_stand_alone_function():     # в якості аргумента в функцію "my_shiny_new_decorator(function_to_decorate)"
    print("Оставь меня в покое")        # тим сами як би накидує додатковий функціонал поверх - обгортає

another_stand_alone_function()

print('\n', '.' * 50, '\n')
