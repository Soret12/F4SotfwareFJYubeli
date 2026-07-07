# Autor: Yubeli Carabalí
# Proyecto: Software FJ
# Menú principal

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from servicios.gestor_clientes import GestorClientes
from servicios.gestor_servicios import GestorServicios
from servicios.gestor_reservas import GestorReservas

from interfaz.ventana_clientes import VentanaCliente
from interfaz.ventana_servicios import VentanaServicio
from interfaz.ventana_reservas import VentanaReserva

from modelos.excepciones import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    DuracionInvalidaError
)


class MenuPrincipal:

    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title(
            "Software FJ - Sistema Integral de Gestión"
        )

        self.ventana.geometry("500x450")
        self.ventana.resizable(False, False)

        # ==========================
        # Gestores del sistema
        # ==========================

        self.gestor_clientes = GestorClientes()
        self.gestor_servicios = GestorServicios()
        self.gestor_reservas = GestorReservas()

        # ==========================
        # Título
        # ==========================

        ttk.Label(
            self.ventana,
            text="SOFTWARE FJ",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        ttk.Label(
            self.ventana,
            text="Sistema Integral de Gestión de Clientes, Servicios y Reservas"
        ).pack(pady=5)

        ttk.Label(
            self.ventana,
            text="Autor: Yubeli Carabalí"
        ).pack(pady=5)


        # ==========================
        # Botones
        # ==========================

        ttk.Button(
            self.ventana,
            text="Clientes",
            width=35,
            command=self.abrir_clientes
        ).pack(pady=8)


        ttk.Button(
            self.ventana,
            text="Servicios",
            width=35,
            command=self.abrir_servicios
        ).pack(pady=8)


        ttk.Button(
            self.ventana,
            text="Reservas",
            width=35,
            command=self.abrir_reservas
        ).pack(pady=8)


        ttk.Button(
            self.ventana,
            text="Simulación 12 Operaciones",
            width=35,
            command=self.simulacion
        ).pack(pady=8)


        ttk.Button(
            self.ventana,
            text="Salir",
            width=35,
            command=self.ventana.destroy
        ).pack(pady=20)


    # ==========================
    # Abrir ventanas
    # ==========================

    def abrir_clientes(self):

        VentanaCliente(
            self.ventana,
            self.gestor_clientes
        )


    def abrir_servicios(self):

        VentanaServicio(
            self.ventana,
            self.gestor_servicios
        )


    def abrir_reservas(self):

        VentanaReserva(
            self.ventana,
            self.gestor_clientes,
            self.gestor_servicios,
            self.gestor_reservas
        )


    # ==========================
    # Simulación del sistema
    # ==========================

    def simulacion(self):

        errores = 0


        # 1. Cliente válido

        try:

            self.gestor_clientes.registrar_cliente(
                "C001",
                "Ana Torres",
                "ana@gmail.com",
                "3001112233"
            )

        except ClienteInvalidoError:

            errores += 1



        # 2. Segundo cliente válido

        try:

            self.gestor_clientes.registrar_cliente(
                "C002",
                "Carlos Perez",
                "carlos@gmail.com",
                "3004445566"
            )

        except ClienteInvalidoError:

            errores += 1



        # 3. Cliente repetido

        try:

            self.gestor_clientes.registrar_cliente(
                "C001",
                "Cliente repetido",
                "error@gmail.com",
                "000000"
            )

        except ClienteInvalidoError:

            errores += 1



        # 4. Crear sala

        try:

            self.gestor_servicios.registrar_servicio(
                "Sala",
                "S001",
                "Sala reuniones",
                50000,
                20
            )

        except ServicioInvalidoError:

            errores += 1



        # 5. Crear equipo

        try:

            self.gestor_servicios.registrar_servicio(
                "Equipo",
                "E001",
                "Computador portátil",
                30000,
                5
            )

        except ServicioInvalidoError:

            errores += 1



        # 6. Crear asesoría

        try:

            self.gestor_servicios.registrar_servicio(
                "Asesoria",
                "A001",
                "Asesoría programación",
                80000,
                "Desarrollo software"
            )

        except ServicioInvalidoError:

            errores += 1



        # 7. Servicio con error

        try:

            self.gestor_servicios.registrar_servicio(
                "Sala",
                "S002",
                "Sala inválida",
                -500,
                10
            )

        except ServicioInvalidoError:

            errores += 1



        # 8. Reserva válida

        try:

            cliente = self.gestor_clientes.buscar_cliente(
                "C001"
            )

            servicio = self.gestor_servicios.buscar_servicio(
                "S001"
            )


            self.gestor_reservas.crear_reserva(
                "R001",
                cliente,
                servicio,
                3
            )

        except (
            ReservaInvalidaError,
            ServicioNoDisponibleError,
            DuracionInvalidaError
        ):

            errores += 1



        # 9. Confirmar reserva

        try:

            self.gestor_reservas.confirmar_reserva(
                "R001"
            )

        except ReservaInvalidaError:

            errores += 1



        # 10. Procesar reserva

        try:

            self.gestor_reservas.procesar_reserva(
                "R001"
            )

        except ReservaInvalidaError:

            errores += 1



        # 11. Cancelar reserva

        try:

            self.gestor_reservas.cancelar_reserva(
                "R001"
            )

        except ReservaInvalidaError:

            errores += 1



        # 12. Procesar reserva cancelada

        try:

            self.gestor_reservas.procesar_reserva(
                "R001"
            )

        except ReservaInvalidaError:

            errores += 1



        messagebox.showinfo(
            "Simulación finalizada",
            f"Proceso terminado correctamente.\n\n"
            f"Errores controlados: {errores}\n\n"
            f"Revise el archivo logs.txt"
        )