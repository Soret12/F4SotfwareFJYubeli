# Registro de eventos y errores

from datetime import datetime


class Logger:

    @staticmethod
    def registrar(mensaje):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}\n"
            )