class Bmi:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def get_bmi(self) -> float:
        """
        bmi 를 계산하여 소숫점 2자리로 이루어진 실수로 반환함.
        :return: bmi .2f
        """
        return round(self.__weight / pow(self.__height * 0.01, 2), 2)

    def get_status(self) -> str:
        """
        계산된 bmi 를 기준으로, 판정 문자를 반환함.
        :return: 판정 문자
        """
        bmi = self.get_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self) -> str:
        """
        Peter King(50): 28.41 | Overweight 와 같은 형태로 문자열을 만들어 준다.
        :return: 생성된 문자열 반환
        """
        return "%s (%d): %.2f | %s" % (self.__name, self.__age, self.get_bmi(), self.get_status())

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height


bmi1 = Bmi("John Doe", 18, 90, 165)
print(bmi1)

bmi2 = Bmi("Peter King", 50, 90, 178)
print(bmi2)

# print(bmi2.__name)
# AttributeError: 'Bmi' object has no attribute '__name'
# https://mingrammer.com/underscore-in-python/
