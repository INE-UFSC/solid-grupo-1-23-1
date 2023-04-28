"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, sound: str, lista: list):
        self.name = name
        self.sound = sound
        self.lista = lista

    @property
    @abstractmethod
    def name(self, name):
        pass
    
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def add(self):
        pass

class Animal:
    def make_sound_lion(self):
        self.name == 'lion'
        return('roar')
        
    def make_sound_mouse(self):
        self.name == 'mice'
        return('squeak')


animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""



class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discountfav(self):
        if self.customer == 'fav':
            return self.price * 0.2
            
    def give_discountvip(self):
        if self.customer == 'vip':
            return self.price * 0.4

