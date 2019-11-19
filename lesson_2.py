# Визначення функції та виклик її

def func(a, b, c):
    x = (a + b) ** c
    return x

z = 2.17
for i in range(10):
    x = func(i, z, 10)
    print(x)
