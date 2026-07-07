#Excepciones personalizadas del sistema.


class ClienteInvalidoError(Exception):
    #Se lanza cuando los datos del cliente son inválidos.
    pass


class ServicioInvalidoError(Exception):
    #Se lanza cuando un servicio tiene datos incorrectos.
    pass


class ReservaInvalidaError(Exception):
    #Se lanza cuando no es posible crear una reserva.
    pass


class ServicioNoDisponibleError(Exception):
    #Se lanza cuando un servicio no está disponible.
    pass


class DuracionInvalidaError(Exception):
    #Se lanza cuando la duración ingresada no es válida.
    pass