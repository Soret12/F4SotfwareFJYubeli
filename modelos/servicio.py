# Clase abstracta Servicio

from abc import ABC, abstractmethod
from modelos.entidad import Entidad
from modelos.excepciones import ServicioInvalidoError


class Servicio(Entidad, ABC):

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)
        self.nombre = nombre
        self.precio_base = precio_base

    # Propiedad nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ServicioInvalidoError("El nombre del servicio no puede estar vacío.")
        self.__nombre = valor

    # Propiedad precio base
    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if valor <= 0:
            raise ServicioInvalidoError("El precio debe ser mayor que cero.")
        self.__precio_base = valor

    # Método abstracto para calcular el costo
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0,impuesto=0):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def describir(self):
        pass

    # Método abstracto para mostrar información
    @abstractmethod
    def mostrar_informacion(self):
        pass