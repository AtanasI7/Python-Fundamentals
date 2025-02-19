class Test:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def sum_numbers(self, val3):
        return (self.val1 * self.val2) + val3


obj = Test(5, 6)

print(obj.sum_numbers(10))