from modelos.entidad import Entidad
from modelos.excepciones import (
    ReservaInvalidaError,
    DuracionInvalidaError,
    ServicioNoDisponibleError
)


class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Propiedad cliente
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        if valor is None:
            raise ReservaInvalidaError(
                "Debe seleccionar un cliente."
            )
        self.__cliente = valor

    # Propiedad servicio
    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self, valor):
        if valor is None:
            raise ServicioNoDisponibleError(
                "Debe seleccionar un servicio."
            )
        self.__servicio = valor

    # Propiedad duración
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, valor):
        if valor <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )
        self.__duracion = valor

    # Confirmar reserva
    def confirmar(self):
        self.estado = "Confirmada"

    # Cancelar reserva
    def cancelar(self):
        self.estado = "Cancelada"

    # Procesar reserva
    def procesar(self, descuento=0):

        if self.estado == "Cancelada":
            raise ReservaInvalidaError(
                "No se puede procesar una reserva cancelada."
            )

        return self.servicio.calcular_costo(
            self.duracion,
            descuento
        )

    # Implementación del método abstracto
    def mostrar_informacion(self):
        return (
            f"ID Reserva: {self.identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )

    def __str__(self):
        return (
            f"Reserva {self.identificador} - "
            f"{self.cliente.nombre} - "
            f"{self.servicio.nombre} - "
            f"{self.estado}"
        )