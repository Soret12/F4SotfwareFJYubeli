from modelos.servicio import Servicio
from modelos.excepciones import ServicioInvalidoError


class Asesoria(Servicio):

    def __init__(self, identificador, nombre, precio_base, especialidad):
        super().__init__(identificador, nombre, precio_base)
        self.especialidad = especialidad

    # Propiedad especialidad
    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not valor.strip():
            raise ServicioInvalidoError( "La especialidad no puede estar vacía.")
        self.__especialidad = valor

    # Implementación del cálculo del costo
    def calcular_costo(self, duracion, descuento=0,impuesto=0):
        costo = self.precio_base * duracion
        costo += costo * impuesto
        costo -= costo * (descuento / 100)      
        return costo

    # Descripción del servicio
    def describir(self):
        return f"Asesoría especializada en {self.especialidad}."

    # Información completa
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio Base: ${self.precio_base}\n"
            f"Especialidad: {self.especialidad}"
        )

    def __str__(self):
        return f"{self.nombre} - Asesoría"