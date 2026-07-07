from modelos.servicio import Servicio
from modelos.excepciones import ServicioInvalidoError


class Equipo(Servicio):

    def __init__(self, identificador, nombre, precio_base, cantidad_disponible):
        super().__init__(identificador, nombre, precio_base)
        self.cantidad_disponible = cantidad_disponible

    # Propiedad cantidad disponible
    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, valor):
        if valor < 0:
            raise ServicioInvalidoError(
                "La cantidad disponible no puede ser negativa."
            )
        self.__cantidad_disponible = valor

    # Implementación del cálculo del costo
    def calcular_costo(self, duracion, descuento=0,impuesto=0):
        costo = self.precio_base * duracion
        costo += costo * impuesto
        costo -= costo * (descuento / 100)      
        return costo

    # Descripción del servicio
    def describir(self):
        return (
            f"Equipo disponible para alquiler. "
            f"Cantidad disponible: {self.cantidad_disponible}"
        )

    # Información completa
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio Base: ${self.precio_base}\n"
            f"Cantidad Disponible: {self.cantidad_disponible}"
        )

    def __str__(self):
        return f"{self.nombre} - Equipo"