word = 'dsafuhpqweoihfnvklsdoaxecnvlrf'
letters = 'aeiouy'
counter = 0

for x in letters:
    print(x)
    print(counter)
    print('_ _ ' * 30)
    counter += word.count(x)
