class TwoNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print("a =", self.a, "b =", self.b)

    def change(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def max_value(self):
        if self.a > self.b:
            return self.a
        else:
            return self.b

nums = TwoNumbers(3, 5)
nums.show()
print("Сумма:", nums.sum())
print("Максимум:", nums.max_value())
