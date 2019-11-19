# LESSON 1
print("Lesson 1")

var1 = 23
print(type(var1), id(var1))

check = var1 is True  # В чому суть перевірки на Правда, Лож? Просто порівняння двох значень?
print(check)

check = var1 is False
print(check)

check = var1 is 23  # Порівнюю, чи є змінна рівною 23
print(check)

var2 = var1 or True  # Навіщо OR?
print(var2, id(var2))  # Можна побачити, що ідентифікатори var1 var2 однакові

check = var2 is True
print(check)

check = var2 is False
print(check)

print(var1 and var2)  # Взагалі не зрозуліло? Чомоу and??? Навіщо воно?

# LESSON 2
print("Lesson 2")
import math
import random

int_seq = random.sample(range(100), 5) # Генерує список з 5 елементів які берутся випадково з діапазону від 0 до 100

rand = random.uniform(2, 1024)  # Генерує випадкове число в діапазоні від а до б

float_random = random.random()  # Генерує випадкове число з плаваючою точкою

int_seq_max = max(int_seq)
floor_div_result = int_seq_max // float_random

print(int_seq)
print(rand)
print(float_random)
print(int_seq_max)
print(floor_div_result)
print(math.factorial(floor_div_result))


# LESSON 3
print("Lesson 3")

import string

text = string.ascii_letters + string.digits
print(text)

print(text[0])	# First symbol

print(text[-1])	  # Last symbol

print(text[2])  # Third from beginning
print(text[-3])    # Third from the end

print(text[:8])		#  Slice of first 8 symbols

print(text[::3]) 	# Print each 3rd symbol

# First solution
print(text[int(len(text)/2):int(len(text)/2)+1])	# Counting first and last boundary
# Another solutuon
print(text[int(len(text) / 2 + 0.5)])			# Counting index

print(text[::-1])		# Reversed text. -1 means the it will print each symbol but will start from the end because of minus



# LESSON 4
print("Lesson 4")

lst = list(string.ascii_letters + string.digits)

print(lst[0])	# First symbol

print(lst[-1])	  # Last symbol

print(lst[2])  # Third from beginning
print(lst[-3])    # Third from the end

print(lst[:10])		#  Slice of first 10 symbols

print(lst[::2]) 	# Print each 2nd symbol

# Print only integer values from list
int_lst = []
for i in lst:
    try:
        int_lst.append(int(i)) # Only integer can be converted here
    except:
        pass

print(int_lst)
print(int_lst[::-1])

print("-".join(lst))  # String from list



# LESSON 5
print("Lesson 5")

 Mapping of coutry to their domain code
countries = {
	'Ukraine': 'UA',
	'Israel': 'IL',
	'Japan': 'JP',
	'United States': 'US',
	'Sweden': 'SE'
	}

capitals = {
	'UA': 'Kiev',
	'IL': 'Jerusalem',
	'JP': 'Tokyo',
	'US': 'Washington',
	'SE': 'Stockholm'
	}

countries['Italy'] = 'IT'
capitals['IT'] = 'Rome'

for key, value in countries.items():
	print ("Domain for {} is {}.".format(key, value))

for key, value in capitals.items():
	print ("The capital of {} is {}".format(key, value))

for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value]))

for key, value in countries.items():
	countries[key] = [value, 'COM', 'GOV']

for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value[0]]))



# LESSON 6
print("Lesson 6")

set1 = set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[3:7] + string.digits[6:])

print(set1)	# First set
print(set2)	# Second set

tpl_intersection = tuple(set1.intersection(set2))
print(tpl_intersection)  # Print intersection

tpl_diff = tuple(set1.difference(set2))
print(tpl_diff)    #  # Print difference between two sets

print(tpl_intersection[:3]) #Slice first 3 symbols from first tuple

print(set(string.digits).intersection(set2)) # Print only numbers from second set

print(tpl_intersection[::-1]) # Reverse tuple

print(list(tpl_intersection), list(tpl_diff))



# LESSON 7
print("Lesson 7")

# Create file object for write only
f = open('myfile.txt','w')
# Write into file
f.write("Hello file world!")
# Close file with saving it's content
f.close()

# Create file object for read and write
f = open('myfile.txt','r+')
# Read and print file content
print(f.read())
f.seek(len("Hello "))
f.write("my " + "file world!") # Try it with "my file" and you will see how work data update in files
f.flush()



