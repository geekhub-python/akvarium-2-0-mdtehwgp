from random import randint
from abc import ABCMeta, abstractmethod
from aquarium import aquarium
from decorators import can_eat


class AquariumCitizen(metaclass=ABCMeta):
    def __init__(self, weight):
        self.type = __class__.__name__
        self._weight = weight
        self._eaten_citizens_count = 0

    @abstractmethod
    def eat(self, сitizen):
        self._weight += сitizen.weight
        self._eaten_citizens_count += 1
        aquarium.remove(сitizen)

    @property
    def eaten_citizens_count(self):
        return self._eaten_citizens_count

    @property
    def weight(self):
        return self._weight


class PeacefulFish(AquariumCitizen):
    def __init__(self):
        super().__init__(weight=randint(1, 9))

    @can_eat('AquaPlant')
    def eat(self, сitizen):
        return super().eat(сitizen)


class PredatoryFish(AquariumCitizen):
    def __init__(self):
        super().__init__(weight=10)

    @can_eat('PeacefulFish')
    def eat(self, сitizen):
        return super().eat(сitizen)


class Snail(AquariumCitizen):
    def __init__(self):
        self._eaten_plants_count = 0
        super().__init__(weight=randint(1, 5))

    @can_eat('AquaPlant')
    def eat(self, citizen):
        return super().eat(citizen)


class AquaPlant(AquariumCitizen):
    def __init__(self):
        super().__init__(weight=randint(1, 3))

    @can_eat('sunlight')
    def eat(self, citizen):
        return super().eat(citizen)
