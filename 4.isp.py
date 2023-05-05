"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
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
from abc import ABC

class IJanela(ABC):
    def minimizar(self):
        raise NotImplementedError

    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    def maximizar(self):
        raise NotImplementedError



