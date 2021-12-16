from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return f'Общий объем ткани {self.coat_t + other.costume_t}'

    @abstractmethod
    def tisue(self):
        pass


class Coat(Clothes):
    @property
    def tisue(self):
        self.coat_t = self.param / 6.5 + 0.5
        return f'Нужно ткани на пальто {self.param / 6.5 + 0.5}'


class Costume(Clothes):
    @property
    def tisue(self):
        self.costume_t = self.param * 2 + 0.3
        return f'Нужно ткани на костюм {self.param * 2 + 0.3}'


coat1 = Coat(10)
costume1 = Costume(20)
t = coat1
print(costume1.tisue)
print(coat1.tisue)
print(coat1 + costume1)
