from abc import *


class Animal:
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def buy(self):
        pass


class Korean(Animal):
    def walk(self):
        print("한국인이 걷고 있습니다.")

    def eat(self):
        print("한국인이 먹고 있습니다.")

    def fly(self):
        pass

    def buy(self):
        print("한국인이 물건을 구입하고 있습니다.")


class bird(Animal):
    def walk(self):
        print("새가 걷고 있습니다.")

    def eat(self):
        print("새가 먹고 있습니다.")

    def fly(self):
        print("새가 날고 있습니다.")

    def buy(self):
        pass
