from random import randint, choice
from functools import wraps

CITIZEN_WEIGHTS = {'peacefulfish': randint(1, 9),
                   'predatoryfish': 10,
                   'snail': randint(1, 5),
                   'aquaplant': randint(1, 3)
                   }


def can_eat(citizen_type):
    def decorator_factory(eat):
        @wraps(eat)
        def wrapper(self, citizen):
            if citizen_type == citizen.__class__.__name__.lower():
                print('{0} eat {1}'.format(self.__class__.__name__, citizen.__class__.__name__))
                return eat(self, citizen)
            if self.__class__.__name__.lower() == 'peacefulfish' and citizen.__class__.__name__.lower() == 'predatoryfish':
                print('{0} try eat {1} and was eaten'.format(self.__class__.__name__, citizen.__class__.__name__))
                citizen.eat(self)
        return wrapper
    return decorator_factory


class AquaCitizen:
    """
    Class 'AquaCitizen()' contains description of attributes and methods for citizen-inheritors

    Attributes:

        type (str): Describes citizen type (type = __class__.__name__.lower())
        _weight (int): Citizen weight
        _eaten_citizens_count (int): Eaten citizens counter (for classes who can eat other citizens)

    """
    def __init__(self, class_type):
        self.type = class_type
        self._weight = CITIZEN_WEIGHTS[class_type]
        self._eaten_citizens_count = 0

    """
    Method eat() remove citizen from aquarium citizens list (in class Aquarium(), attribute 'citizens')

    Args:

        citizen (obj): citizen to eat

    """
    def eat(self, сitizen):
        self._weight += сitizen.weight
        self._eaten_citizens_count += 1
        aquarium.citizens.remove(сitizen)

    @property
    def eaten_citizens_count(self):
        return self._eaten_citizens_count

    @property
    def weight(self):
        return self._weight


class PeacefulFish(AquaCitizen):
    def __init__(self):
        super().__init__(self.__class__.__name__.lower())

    @can_eat('aquaplant')
    def eat(self, сitizen):
        return super().eat(сitizen)


class PredatoryFish(AquaCitizen):
    def __init__(self):
        super().__init__(self.__class__.__name__.lower())

    @can_eat('peacefulfish')
    def eat(self, сitizen):
        return super().eat(сitizen)


class Snail(AquaCitizen):
    def __init__(self):
        self._eaten_plants_count = 0
        super().__init__(self.__class__.__name__.lower())

    @can_eat('aquaplant')
    def eat(self, citizen):
        return super().eat(citizen)


class AquaPlant(AquaCitizen):
    def __init__(self):
        super().__init__(self.__class__.__name__.lower())

    @can_eat('type')
    def eat(self, citizen):
        return super().eat(citizen)


class Aquarium:
    """ Class Aquarium() contains descriptions of storage of aquarium citizens (list),
    citizens deployment methods and simulate aquarium life method.

    Attributes:

        citizens (list): List of aquarium citizens

    """
    def __init__(self):
        self.citizens = []

    def deploy_predators(self, count):
        for _ in range(count):
            self.citizens.append(PredatoryFish())

    def deploy_peaceful(self, count):
        for _ in range(count):
            self.citizens.append(PeacefulFish())

    def deploy_snail(self, count):
        for _ in range(count):
            self.citizens.append(Snail())

    def deploy_aquaplant(self, count):
        for _ in range(count):
            self.citizens.append(AquaPlant())

    """ Method simulate() choice random сitizen and try to eat another random сitizen, print scoreboard """
    def simulate(self):
        while len(self.citizens) > count_predators + count_snail:
            eating_citizen = choice(self.citizens)
            citizen_to_eat = choice(self.citizens)
            eating_citizen.eat(citizen_to_eat)

        self.citizens.sort(key=lambda x: x.weight, reverse=True)
        print('SCOREBOARD'.center(36, '*'))
        for n in self.citizens:
            print('{0}(weight={1}) eat {2} feeds'.format(n.__class__.__name__, n.weight, n.eaten_citizens_count))


if __name__ == "__main__":
    aquarium = Aquarium()

    count_peaceful = 20
    count_predators = 3
    count_snail = 4
    count_aquaplant = 40

    aquarium.deploy_peaceful(count_peaceful)
    aquarium.deploy_predators(count_predators)
    aquarium.deploy_snail(count_snail)
    aquarium.deploy_aquaplant(count_aquaplant)

    aquarium.simulate()

