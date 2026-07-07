# Clase Sala

from modelos.servicio import Servicio
from modelos.excepciones import ServicioInvalidoError


class Sala(Servicio):

    def __init__(self, identificador, nombre, precio_base, capacidad):
        super().__init__(identificador, nombre, precio_base)
        self.capacidad = capacidad

    # Propiedad capacidad
    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if valor <= 0:
            raise ServicioInvalidoError("La capacidad de la sala debe ser mayor que cero.")
        self.__capacidad = valor

    # Implementación del cálculo del costo
    def calcular_costo(self, duracion, descuento=0,impuesto=0):
        costo = self.precio_base * duracion
        costo += costo * impuesto
        costo -= costo * (descuento / 100)      
        return costo

    # Descripción del servicio
    def describir(self):
        return f"Sala con capacidad para {self.capacidad} personas."

    # Información completa
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio Base: ${self.precio_base}\n"
            f"Capacidad: {self.capacidad} personas"
        )

    def __str__(self):
        return f"{self.nombre} - Sala"