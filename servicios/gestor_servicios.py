from modelos.sala import Sala
from modelos.equipo import Equipo
from modelos.asesoria import Asesoria
from modelos.excepciones import ServicioInvalidoError
from servicios.logger import Logger


class GestorServicios:

    def __init__(self):
        self.servicios = []

    # Registrar servicio
    def registrar_servicio(
        self,
        tipo_servicio,
        identificador,
        nombre,
        precio_base,
        dato_extra
    ):

        try:

            # Verificar si ya existe
            if self.buscar_servicio(identificador):
                raise ServicioInvalidoError(
                    "Ya existe un servicio con ese identificador."
                )

            if tipo_servicio == "Sala":

                servicio = Sala(
                    identificador,
                    nombre,
                    precio_base,
                    dato_extra
                )

            elif tipo_servicio == "Equipo":

                servicio = Equipo(
                    identificador,
                    nombre,
                    precio_base,
                    dato_extra
                )

            elif tipo_servicio == "Asesoria":

                servicio = Asesoria(
                    identificador,
                    nombre,
                    precio_base,
                    dato_extra
                )

            else:
                raise ServicioInvalidoError(
                    "Tipo de servicio no válido."
                )

            self.servicios.append(servicio)

        except ServicioInvalidoError as e:
            Logger.registrar(f"Error de servicio: {e}")
            raise

        except Exception as e:
            Logger.registrar(f"Error inesperado: {e}")
            raise

        else:
            Logger.registrar(
                f"Servicio registrado correctamente: {nombre}"
            )

    # Buscar servicio
    def buscar_servicio(self, identificador):

        for servicio in self.servicios:
            if servicio.identificador == identificador:
                return servicio

        return None

    # Listar servicios
    def listar_servicios(self):
        return self.servicios

    # Eliminar servicio
    def eliminar_servicio(self, identificador):

        try:

            servicio = self.buscar_servicio(identificador)

            if servicio is None:
                raise ServicioInvalidoError(
                    "El servicio no existe."
                )

            self.servicios.remove(servicio)

        except ServicioInvalidoError as e:
            Logger.registrar(f"Error de servicio: {e}")
            raise

        except Exception as e:
            Logger.registrar(f"Error inesperado: {e}")
            raise

        else:
            Logger.registrar(
                f"Servicio eliminado: {servicio.nombre}"
            )