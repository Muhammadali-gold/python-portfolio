class OddiyX:
    def __init__(self):
        self.k = 0
        self.gr = 0

    def __init__(self, ko, gra):
        self.k = ko
        self.gr = gra

    def calculateIntegral(self):
        self.Integral_gr = self.gr + 1
        self.Integral_k = self.k / self.Integral_gr

    def numbWhenXGiven(self, x):
        return self.k * (x ** self.gr)

    def integralNumbWhenXGiven(self, x):
        return self.Integral_k * (self.Integral_gr ** x)

    def printIntegral(self):
        print(format("{0} * x**{1}",  [self.Integral_k, self.Integral_gr]))


# Main
obj = OddiyX(1, 1)
obj.calculateIntegral()
assert 5 == obj.numbWhenXGiven(5)
obj.printIntegral()
obj.calculateIntegral()
assert 2 == obj.integralNumbWhenXGiven(2)
