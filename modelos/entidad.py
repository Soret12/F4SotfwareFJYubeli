#Clase abstracta que representa una entidad del sistema.


from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        self._identificador = valor

    @abstractmethod
    def mostrar_informacion(self):
        #Debe ser implementado por las clases hijas.
        pass