#
#
#

# LESSON 3.1


l = [1, 2, 3, 4, 5]
a, *b = l
print(a, b)


print(192, 168, 15, 1, sep = ".", end = "   next >>\t log out\n")


print('\n', '*' * 100, '\n')

#
#
#

# LESSON 3.2
a = 0
if a == 0:
    b = 1
    if b == 1:
        c = 2
        print('c = 2')
    print('b = 1')
print('a = 0')

print('\n', '*' * 100, '\n')

for number in range(10):
    print(number)


print('\n', '*' * 100, '\n')

for i in range(6):
    print(pow(i, i))
else:
    print("Not found")

print('\n', '*' * 100, '\n')

list_asdf = [1, 2, 2, 4, 'e', 4, 5]

for v in list_asdf:
    print(v)
    if type(v) == str:
        break
else:
    print("STR not found")


print('\n', '*' * 100, '\n')


a = -5
while a < 0:
    a += 1              # a = a + 1
    print(a)


print('\n', '*' * 100, '\n')
#
#
#

# HOMEWORK 2.7
