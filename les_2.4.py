x = '934jfskvj9854ijrgtnmkvnIFHDPS85INRF'

df = list(x)

f = [i for i in df if type(i) == int]

print(f)

w = ''.join([str(i) for i in x])   # перетворити список в строку

print(type(w))


ds = { (1, 4, 5) : 'sdas', (2, 3, 4) : 'df', (3, 4, 5) : 34}

ds[12] =  '23sd'
ds['qwe'] = 908
print(ds)


year_multi_log = {1 : {'en' : 'Jan', 'ua' : 'Січ'}, 2 : {'en' : 'Feb', 'ua' : 'Лют'}, 3 : {'en' : 'Mar', 'ua' : 'Мар'},
                  4 : {'en' : 'Apr', 'ua' : 'Кві'}, }

print(year_multi_log[1]['ua'])



# РІЗНІ СПОСОБИ ВИВОДУ СЛОВНИКІВ

for t in year_multi_log:
    print(t)

for t in year_multi_log.values():
    print(t)

for t in year_multi_log.keys():
    print(t)

for t in year_multi_log.items():
    print(t)


country = {'Ukraine': 'UA', 'Germany': 'GE', 'Poland': 'PL', 'Bulgary': 'BL', 'Italy': 'IT'}

capital = {'UA': 'Kyiv', 'GE': 'Berlin', 'PL': 'Warshava', 'BL': 'Sofia', 'IT': 'Roma'}

country['USA'] = 'US'
capital['US'] = 'Washington'


print(country)
print(capital)


tmp = 'Domain of %s is %s'


for country, domain in country.items():
    print(tmp % (country, domain))

print(country)

tmp2 = 'Capital of %s is %s'


for capital, domain in capital.items():
    print(tmp2 % (capital, domain))


for country, domain in country.items():
    for capital, domain in capital.items():
    Domain of {} is {}. The Capital of {} is {}.format(country.key(), country.value(), capital.key(), capital.value())

d = {1: 23, 2: 34, 3: 45}
print(d)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)


