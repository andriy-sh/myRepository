
animals = ('cat', 'dog')
print (animals)



f = "I don't no about Python anithing"

with open('new_file', 'w') as fl:
    for i in f.split():
        fl.write(i + '\n')
    fl.close()

x = open('new_file')

print(x.readlines())

x.read(5)

q = open('new_file', 'a')
print(q)
