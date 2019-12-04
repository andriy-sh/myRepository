country = {'Ukraine': 'UA', 'Germany': 'GE', 'Poland': 'PL', 'Bulgary': 'BL', 'Italy': 'IT'}

capital = {'UA': 'Kyiv', 'GE': 'Berlin', 'PL': 'Warshava', 'BL': 'Sofia', 'IT': 'Roma'}

country['USA'] = 'US'
capital['US'] = 'Washington'





for country, domain in country.items():
    print("Domain of {} is {}. The capital is {}.".format(country, domain, capital[domain]))


print ('\n', '*' * 100, '\n')

#
#
#

# HOMEWORK 2.6

setA = set('oafjew8WEWQE')
print(setA)

setB = set('1DFSfdgsdf3go')
print(setB)

tpl1 = tuple(setA & setB)
print(tpl1)

tpl2 = tuple(setA - setB)
print(tpl2)

print(tpl1[:3])
print(tpl2[::-1])

print('All list:', list(tpl1) + list(tpl2))

"""
for x in tpl2  if  type(x) == int:
    print(x)
"""
print ('\n', '*' * 100, '\n')


#
#
#

# HOMEWORK 2.7

f = open('/root/Documents/myfile.txt', 'w')
f.write("Hello Ukraine!")
f.close()

f = open('/root/Documents/myfile.txt', 'w+')
f.write("Slava Ukraine!! I love Ukraine!")
f.close()


f = open('/root/Documents/myfile.txt', 'r')
print(f.read())
f.flush()
