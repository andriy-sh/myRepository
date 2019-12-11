# Function

def add_values(a, b):
    plus = a + b
    return plus

def main():

    try:
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        qw = add_values(a, b)                        # Обовязково присвоїти, бо повертає None

    except ValueError:
        print('You must input only integer value!')
    else:
        print(qw)

def nod():
    while st != 1:
        st = a % b
        print(st)
    return st


main()
nod()



