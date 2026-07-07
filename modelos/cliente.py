from modelos.entidad import Entidad
from modelos.excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # Propiedad nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío.")
        self.__nombre = valor

    # Propiedad correo
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            raise ClienteInvalidoError("El correo electrónico no es válido.")
        self.__correo = valor

    # Propiedad teléfono
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit():
            raise ClienteInvalidoError("El teléfono solo debe contener números.")
        self.__telefono = valor

    # Implementación del método abstracto
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )

    def __str__(self):
        return f"{self.nombre} ({self.correo})"