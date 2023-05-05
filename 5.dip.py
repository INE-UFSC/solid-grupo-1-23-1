"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
'''
class Player:
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: Player):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
'''
class Entidade:
    def __init__(self, name, hp, speed):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = hp
        self.__speed = speed

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

    def speed(self):
        return self.__speed

class Player(Entidade):
    def __init__(self, name):
        super().__init__(name, 100, 1)

class StatsReporter:
    def __init__(self, char: Entidade):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')

p1 = Player("p1")
p1.stats.report()