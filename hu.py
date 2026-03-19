from abc import ABC, abstractmethod

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def produit(self):
        return self.__produit

    @property
    def quantite(self):
        return self.__quantite

    @quantite.setter
    def quantite(self, value):
        self.__quantite = value


class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom

    @property
    def code(self):
        return self.__code

    @abstractmethod
    def getPrixHT(self):
        pass
