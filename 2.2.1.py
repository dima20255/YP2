class Student:
    def __init__(self, lastname, birthdate, group, grades):
        self.lastname = lastname
        self.birthdate = birthdate
        self.group = group
        self.grades = grades

    def change_lastname(self, new_lastname):
        self.lastname = new_lastname

    def change_birthdate(self, new_birthdate):
        self.birthdate = new_birthdate

    def change_group(self, new_group):
        self.group = new_group

    def show_info_if_match(self, lastname, birthdate):
        if self.lastname == lastname and self.birthdate == birthdate:
            print("Фамилия:", self.lastname)
            print("Дата рождения:", self.birthdate)
            print("Группа:", self.group)
            print("Оценки:", self.grades)

students = [Student("Иванов", "2000-01-01", "101", [4,3,5,5,4])]
lastname = input("Введите фамилию: ")
birthdate = input("Введите дату рождения: ")
for s in students:
    s.show_info_if_match(lastname, birthdate
