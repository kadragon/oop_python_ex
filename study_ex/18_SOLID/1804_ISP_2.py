from abc import *


class Animal:
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Person:
    @abstractmethod
    def buy(self):
        pass


class Bird:
    @abstractmethod
    def fly(self):
        pass


class Korean(Animal, Person):
    def walk(self):
        print("한국인이 걷고 있습니다.")

    def eat(self):
        print("한국인이 먹고 있습니다.")

    def buy(self):
        print("한국인이 물건을 구입하고 있습니다.")


class Pigeon(Animal, Bird):
    def walk(self):
        print("비둘기가 걷고 있습니다.")

    def eat(self):
        print("비둘기가 먹고 있습니다.")

    def fly(self):
        print("비둘기가 날고 있습니다.")
