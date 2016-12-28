from functools import wraps


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


def can_eat(citizen_type):
    def decorator_factory(eat):
        @wraps(eat)
        def wrapper(self, citizen):
            if citizen_type == citizen.__class__.__name__:
                return eat(self, citizen)
            if self.__class__.__name__ == 'PeacefulFish' and citizen.__class__.__name__ == 'PredatoryFish':
                citizen.eat(self)

        return wrapper

    return decorator_factory
