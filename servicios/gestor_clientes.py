from modelos.cliente import Cliente
from modelos.excepciones import ClienteInvalidoError
from servicios.logger import Logger


class GestorClientes:

    def __init__(self):
        self.clientes = []

    # Registrar un cliente
    def registrar_cliente(self, identificador, nombre, correo, telefono):

        try:

            # Verificar si el cliente ya existe
            if self.buscar_cliente(identificador):
                raise ClienteInvalidoError(
                    "Ya existe un cliente con ese identificador."
                )

            cliente = Cliente(
                identificador,
                nombre,
                correo,
                telefono
            )

            self.clientes.append(cliente)

        except ClienteInvalidoError as e:
            Logger.registrar(f"Error de cliente: {e}")
            raise

        except Exception as e:
            Logger.registrar(f"Error inesperado: {e}")
            raise

        else:
            Logger.registrar(
                f"Cliente registrado correctamente: {nombre}"
            )

    # Buscar cliente
    def buscar_cliente(self, identificador):

        for cliente in self.clientes:
            if cliente.identificador == identificador:
                return cliente

        return None

    # Listar clientes
    def listar_clientes(self):
        return self.clientes

    # Eliminar cliente
    def eliminar_cliente(self, identificador):

        try:

            cliente = self.buscar_cliente(identificador)

            if cliente is None:
                raise ClienteInvalidoError(
                    "El cliente no existe."
                )

            self.clientes.remove(cliente)

        except ClienteInvalidoError as e:
            Logger.registrar(f"Error de cliente: {e}")
            raise

        except Exception as e:
            Logger.registrar(f"Error inesperado: {e}")
            raise

        else:
            Logger.registrar(
                f"Cliente eliminado: {cliente.nombre}"
            )