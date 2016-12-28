from decorators import singleton

AQUARIUM_MAX_SIZE = 100


@singleton
class Aquarium:
    def __init__(self):
            self._citizens = []

    def __len__(self):
        return len(self._citizens)

    def __getitem__(self, item):
        return self._citizens[item]

    def __setitem__(self, key, value):
        self._citizens[key] = value

    def __delitem__(self, key):
        del self._citizens[key]

    def __iter__(self):
        return iter(self._citizens)

    def extend(self, value):
        if len(self) <= AQUARIUM_MAX_SIZE:
            self._citizens.extend(value)
        else:
            raise ValueError('errror! not enough space in the aquarium')

    def remove(self, value):
        self._citizens.remove(value)

    def sort_by_weight(self):
        return self._citizens.sort(key=lambda x: x.weight, reverse=True)


aquarium = Aquarium()
