from abc import ABC, abstractmethod


class Tailor:

    def __init__(self, size):
        self.size = size
    def __add__(self, other):
        return round(self.tissue_consumption() + other.tissue_consumption())

    @abstractmethod
    def tissue_consumption(self):
        pass


class Suite(Tailor):

    def tissue_consumption(self):
        return (2 * self.size + 0.3)


class Coat(Tailor):

    def tissue_consumption(self):
        return (2 * self.size + 0.3)

suite = Suite(10)
coat = Coat(20)
print(suite.tissue_consumption())
print(coat.tissue_consumption())
print(suite + coat)