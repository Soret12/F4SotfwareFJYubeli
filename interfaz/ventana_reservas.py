# Autor: Yubeli Carabalí
# Proyecto: Software FJ

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from interfaz.utilidades import centrar_ventana


class VentanaReserva:

    def __init__(self, padre,
                 gestor_clientes,
                 gestor_servicios,
                 gestor_reservas):

        self.gestor_clientes = gestor_clientes
        self.gestor_servicios = gestor_servicios
        self.gestor_reservas = gestor_reservas

        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Gestión de Reservas")
        centrar_ventana(self.ventana,600,650)

        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        # ==========================
        # ID Reserva
        # ==========================

        ttk.Label(
            self.ventana,
            text="ID Reserva:"
        ).pack()

        self.txt_id = ttk.Entry(self.ventana)
        self.txt_id.pack()

        # ==========================
        # Cliente
        # ==========================

        ttk.Label(
            self.ventana,
            text="Cliente:"
        ).pack()

        self.cmb_cliente = ttk.Combobox(
            self.ventana,
            state="readonly",
            width=50
        )
        self.cmb_cliente.pack()

        # ==========================
        # Servicio
        # ==========================

        ttk.Label(
            self.ventana,
            text="Servicio:"
        ).pack()

        self.cmb_servicio = ttk.Combobox(
            self.ventana,
            state="readonly",
            width=50
        )
        self.cmb_servicio.pack()

        # ==========================
        # Duración
        # ==========================

        ttk.Label(
            self.ventana,
            text="Duración:"
        ).pack()

        self.txt_duracion = ttk.Entry(self.ventana)
        self.txt_duracion.pack()

        # ==========================
        # Botones
        # ==========================

        ttk.Button(
            self.ventana,
            text="Actualizar listas",
            command=self.actualizar_combobox
        ).pack(pady=5)

        ttk.Button(
            self.ventana,
            text="Crear Reserva",
            command=self.crear_reserva
        ).pack(pady=5)

        ttk.Button(
            self.ventana,
            text="Confirmar Reserva",
            command=self.confirmar_reserva
        ).pack(pady=5)

        ttk.Button(
            self.ventana,
            text="Cancelar Reserva",
            command=self.cancelar_reserva
        ).pack(pady=5)

        ttk.Button(
            self.ventana,
            text="Procesar Reserva",
            command=self.procesar_reserva
        ).pack(pady=5)

        # ==========================
        # Lista de reservas
        # ==========================

        ttk.Label(
            self.ventana,
            text="Reservas registradas"
        ).pack(pady=10)

        self.lista = tk.Listbox(
            self.ventana,
            width=80,
            height=12
        )

        self.lista.pack()

        self.actualizar_combobox()
        self.actualizar_lista()

    # ==========================================
    # Actualizar clientes y servicios
    # ==========================================

    def actualizar_combobox(self):

        clientes = [
            cliente.identificador
            for cliente in self.gestor_clientes.listar_clientes()
        ]

        servicios = [
            servicio.identificador
            for servicio in self.gestor_servicios.listar_servicios()
        ]

        self.cmb_cliente["values"] = clientes
        self.cmb_servicio["values"] = servicios

    # ==========================================
    # Crear reserva
    # ==========================================

    def crear_reserva(self):

        try:

            cliente = self.gestor_clientes.buscar_cliente(
                self.cmb_cliente.get()
            )

            servicio = self.gestor_servicios.buscar_servicio(
                self.cmb_servicio.get()
            )

            self.gestor_reservas.crear_reserva(
                self.txt_id.get(),
                cliente,
                servicio,
                int(self.txt_duracion.get())
            )

            messagebox.showinfo(
                "Éxito",
                "Reserva creada correctamente."
            )

            self.actualizar_lista()
            self.limpiar()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # Confirmar reserva
    # ==========================================

    def confirmar_reserva(self):

        try:

            self.gestor_reservas.confirmar_reserva(
                self.txt_id.get()
            )

            self.actualizar_lista()

            messagebox.showinfo(
                "Éxito",
                "Reserva confirmada."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # Cancelar reserva
    # ==========================================

    def cancelar_reserva(self):

        try:

            self.gestor_reservas.cancelar_reserva(
                self.txt_id.get()
            )

            self.actualizar_lista()

            messagebox.showinfo(
                "Éxito",
                "Reserva cancelada."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # Procesar reserva
    # ==========================================

    def procesar_reserva(self):

        try:

            total = self.gestor_reservas.procesar_reserva(
                self.txt_id.get()
            )

            messagebox.showinfo(
                "Costo Total",
                f"El costo de la reserva es: ${total}"
            )

            self.actualizar_lista()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # Actualizar lista de reservas
    # ==========================================

    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for reserva in self.gestor_reservas.listar_reservas():

            self.lista.insert(
                tk.END,
                str(reserva)
            )

    # ==========================================
    # Limpiar controles
    # ==========================================

    def limpiar(self):

        self.txt_id.delete(0, tk.END)
        self.txt_duracion.delete(0, tk.END)

        self.cmb_cliente.set("")
        self.cmb_servicio.set("")