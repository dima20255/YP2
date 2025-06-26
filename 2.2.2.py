class Train:
    def __init__(self, destination, number, time):
        self.destination = destination
        self.number = number
        self.time = time

    def show_info_of_number(self, number):
        if self.number == number:
            print("Пункт назначения:", self.destination)
            print("Номер поезда:", self.number)
            print("Время отправления:", self.time)

trains = [
    Train("Москва", number = 1, time="12:00"),
    Train("Новосибирск", number = 2, time="15:00")
]

num = int(input("Введите номер поезда: "))

for t in trains:
    t.show_info_of_number(num)
