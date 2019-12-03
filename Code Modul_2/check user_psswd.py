import string

specLit = list(string.punctuation)
print(specLit)

credent = {'user': 'qwerty', 'admin': '123456', 'guest' : 'test'}


while True:
    try:
        user_name = input("Username: ")

        if not user_name.strip():                   # Убирає пробіли по бокам
            raise RuntimeError

        pwd = credent[user_name]

        passwd = input("Password: ")
        if not passwd.strip() == pwd:
            if input('Do you want change password (y/[n])?').strip().lower() == 'y':
                new_passwd = input("Input new password: ").strip()

                for x in new_passwd:
                    if x in specLit:
                        (credent[user_name]) = new_passwd
                        print("Password saved")
                        break
                else:
                    print("The password is weak! Please setup strong password")
                    continue
            else:
                print("Incorrect password")
                continue
        else:
            continue


    except RuntimeError:
        print("Username is empty!")
    except KeyError:
        print("Invalid username!")






