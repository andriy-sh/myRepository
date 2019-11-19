print('dfdsafdsadsfds'
      'fsdadfadsf')            # Видасть як суцільну строку


'''\b – Backspace

   \n – Newline

   \s -  Space

   \t – Tab

   \v – Vertical tab'''


print('dfdsafdsadsfds\v\v\vfsdadfadsf')            # Вертикальний Tab

print('dfdsafdsadsfds\tfsdadfadsf')

print('dfdsafdsadsfds\nfsdadfadsf')

print('dfdsafdsadsfds\sdadfadsf')

print('dfdsafdsadsfds321\bfsdadfadsf')




import datetime

a = datetime.datetime.now()
print(str(a))
print(repr(a))                   # Виводить всю детальну інформацію про змінні тощо

print('asd' * 2)

# Форматування стрічки

ss = "ID: %s, password: %s"  % (123, 'passw0rd')  # Підставили дані замісць кожного %s відповідно
print(ss)

'''Comments:

There are also several string constants:
string.ascii_letters - ascii_lowercase and ascii_uppercase explained below;
string.ascii_lowercase returns 'abcdefghijklmnopqrstuvwxyz‘;
string.ascii_uppercase returns 'ABCDEFGHIJKLMNOPQRSTUVWXYZ‘;
string.digits returns '0123456789‘;
string.hexdigits returns '0123456789abcdefABCDEF‘;
string.octdigits returns '01234567‘;
string.punctuation returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~‘;
string.printable returs  digits, ascii_letters, punctuation, and whitespace;
string.whitespace returns ' \t\n\r\x0b\x0c‘ – (space, tab, linefeed, return, formfeed, and vertical tab).
'''


S = 'Sring'

print('Всю строку:', S[:], '      ', 'Від 2ого символу до кінця:', S[2:])

R = S[:]

print('Коли ствроюється строку на основі іншої,\nто ідентифікатор'
      ' не змінюється,\nт.к. строка не мутабельна:', 'id(S)=',id(S), 'id(R)=',id(R))

g = 'Test String'
print(g[::-1])     #  Інвертування строки


# Вбудовані методи строк


name = 'Andriy, Sergiy, Vadum, Olga'
print(name.capitalize())
print(name.upper())
print(name.split())
print('Hellllo'.replace('l', 'r', 3))
print(name.split(',', 2))


rty = 'djslvihnkierjdYYjdhsaUJDdjsafIdsfaUUBNB'

print(rty[0], rty[-1], rty[2], rty[-3], rty[:7])

print(rty[::3])

lgs = len(rty)
mid = lgs // 2
print(mid)
print(rty[mid-1])
print(rty[::-1])

print(rty.__hash__())
print(rty)
print(rty.casefold())

a = '0111135'
print(a.isdecimal())

a = '11111'
print(a.isdigit())


