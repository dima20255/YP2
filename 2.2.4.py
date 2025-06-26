class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

c = Counter()
print("Начальное значение:", c.get_value())
c.increment()
print("После увеличения:", c.get_value())
c.decrement()
print("После уменьшения:", c.get_value())
