
class Number:

    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2
    def triple(self):
        return self.value * 3
    def quadruple(self):
        return self.value * 4
    def halve(self):
        return self.value / 2
    def evaluate_1(self):
        if self.value % 2 == 0:
            return print("This is an even number")
        else:
            return print("This is an odd number")
    def evaluate_2(self):
        if type(self.value) == int:
            return print("This is an integer number")
        elif type(self.value) == float:
            return print("This is an float number")
        else:
            return print("Don't know what it is")


number_three = Number(3)
number_four = Number(4.5)
string_testing = Number("testing")


print(number_three.value)
print(number_three.value)
print(number_three.double)
print(number_three.double())

print(string_testing.value)
print(string_testing.evaluate_2())

