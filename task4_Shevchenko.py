import datetime

class Person():

    def __init__(self, surname, first_name, birth_date, *args):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
        if len(args) > 0:
            self.nickname = args[0]

    def get_fullname(self):
        return str(self.surname) + ' ' + str(self.first_name)

    def get_age(self):
        return str(datetime.datetime.today().year - self.birth_date.year)

A(Shevchenko, Andriy, '1983-05-14') = Person()
