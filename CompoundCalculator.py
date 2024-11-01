class CompoundCalculator:
    def __init__(self, value, InOrLo, rate, time):  # InOrLo stands for interest or loss!
        self.__base(value, InOrLo, rate, time)  # InOrLo: 1 or -1

    def __base(self, value, InOrLo, rate, time):
        rate = abs(rate/100 + InOrLo)
        self.__result = value * (rate**time)

    def convert_to_currency(self):
        result1 = str(round(self.__result))
        result2 = ""
        index = 0
        for n in result1[::-1]:
            result2 += n
            index += 1
            if index/3 == int(index/3) and index < len(result1):
                result2 += ","
        return result2[::-1]  # Note: This value is approximate!

    def __str__(self):
        return str(self.__result)


cc = CompoundCalculator(10000, 1, 25, 5)
print(cc)
print(cc.convert_to_currency())
