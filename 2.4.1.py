class Student:
    def __init__(self, name, surname, patronymic, group, grades):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"ФИО: {self.surname} {self.name} {self.patronymic}")
        print(f"Группа: {self.group}")
        print(f"Средний балл: {self.average_grade()}")

students = []

def add_student():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")
    group = input("Группа: ")
    grades = []
    for i in range(4):
        grade = int(input(f"Оценка {i+1}: "))
        grades.append(grade)

    student = Student(name, surname, patronymic, group, grades)
    students.append(student)
    print("Студент добавлен!")

def view_all_students():
    if not students:
        print("Список студентов пуст.")
    else:
        for student in students:
            student.display_info()
            print("-" * 20)

def get_student_by_index():
    if not students:
        print("Список студентов пуст.")
        return

    index = int(input("Введите номер студента в списке (начиная с 1): ")) - 1
    if 0 <= index < len(students):
        students[index].display_info()
    else:
        print("Неправильный номер студента.")

while True:
    print("\nМеню:")
    print("1. Добавить студента")
    print("2. Посмотреть всех студентов")
    print("3. Посмотреть студента по номеру")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        get_student_by_index()
    elif choice == "4":
        break
    else:
        print("Неправильный ввод.")
