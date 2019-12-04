import string

new_passwd = input("Input new password: ").strip()

specLit = list(string.punctuation)

print(specLit)

for x in new_passwd:
    if x in specLit:
        print("Password saved")
        break
else:
    print("The password is weak!")




