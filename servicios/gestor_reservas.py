# Autor: Yubeli Carabalí
# Proyecto: Software FJ
# Gestor de reservas

from modelos.reserva import Reserva
from modelos.excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError
)
from servicios.logger import Logger


class GestorReservas:

    def __init__(self):
        self.reservas = []

    # Registrar una nueva reserva
    def crear_reserva(self, identificador, cliente, servicio, duracion):

        try:

            # Verificar si la reserva ya existe
            if self.buscar_reserva(identificador):
                raise ReservaInvalidaError(
                    "Ya existe una reserva con ese identificador."
                )

            if cliente is None:
                raise ReservaInvalidaError(
                    "Debe seleccionar un cliente."
                )

            if servicio is None:
                raise ServicioNoDisponibleError(
                    "Debe seleccionar un servicio."
                )

            try:
                reserva = Reserva(
                    identificador,
                    cliente,
                    servicio,
                    duracion
                )

            # Encadenamiento de excepciones
            except Exception as e:
                raise ReservaInvalidaError(
                    "No fue posible crear la reserva."
                ) from e

            self.reservas.append(reserva)

        except Exception as e:
            Logger.registrar(f"Error al crear reserva: {e}")
            raise

        else:
            Logger.registrar(
                f"Reserva {identificador} creada correctamente."
            )

        finally:
            Logger.registrar(
                "Proceso de creación de reserva finalizado."
            )

    # Buscar una reserva por ID
    def buscar_reserva(self, identificador):

        for reserva in self.reservas:
            if reserva.identificador == identificador:
                return reserva

        return None

    # Confirmar reserva
    def confirmar_reserva(self, identificador):

        try:

            reserva = self.buscar_reserva(identificador)

            if reserva is None:
                raise ReservaInvalidaError(
                    "La reserva no existe."
                )

            reserva.confirmar()

        except Exception as e:
            Logger.registrar(f"Error al confirmar reserva: {e}")
            raise

        else:
            Logger.registrar(
                f"Reserva {identificador} confirmada."
            )

    # Cancelar reserva
    def cancelar_reserva(self, identificador):

        try:

            reserva = self.buscar_reserva(identificador)

            if reserva is None:
                raise ReservaInvalidaError(
                    "La reserva no existe."
                )

            reserva.cancelar()

        except Exception as e:
            Logger.registrar(f"Error al cancelar reserva: {e}")
            raise

        else:
            Logger.registrar(
                f"Reserva {identificador} cancelada."
            )

    # Procesar reserva
    def procesar_reserva(self, identificador, descuento=0):

        try:

            reserva = self.buscar_reserva(identificador)

            if reserva is None:
                raise ReservaInvalidaError(
                    "La reserva no existe."
                )

            total = reserva.procesar(descuento)

        except Exception as e:
            Logger.registrar(
                f"Error al procesar reserva: {e}"
            )
            raise

        else:
            Logger.registrar(
                f"Reserva {identificador} procesada. Total: ${total}"
            )
            return total

    # Listar reservas
    def listar_reservas(self):
        return self.reservas