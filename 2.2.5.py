class MyClass:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print("Объект создан")

    def __del__(self):
        print("Объект удалён")

obj1 = MyClass(5, 7)
obj2 = MyClass()
del obj1
