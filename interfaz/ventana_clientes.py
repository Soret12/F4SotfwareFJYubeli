# Autor: Yubeli Carabalí
# Proyecto: Software FJ

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class VentanaCliente:

    def __init__(self, padre, gestor_clientes):

        self.gestor = gestor_clientes

        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("600x650")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        # ==========================
        # Identificador
        # ==========================

        ttk.Label(
            self.ventana,
            text="Identificador:"
        ).pack()

        self.txt_id = ttk.Entry(self.ventana)
        self.txt_id.pack()

        # ==========================
        # Nombre
        # ==========================

        ttk.Label(
            self.ventana,
            text="Nombre:"
        ).pack()

        self.txt_nombre = ttk.Entry(self.ventana)
        self.txt_nombre.pack()

        # ==========================
        # Correo
        # ==========================

        ttk.Label(
            self.ventana,
            text="Correo:"
        ).pack()

        self.txt_correo = ttk.Entry(self.ventana)
        self.txt_correo.pack()

        # ==========================
        # Teléfono
        # ==========================

        ttk.Label(
            self.ventana,
            text="Teléfono:"
        ).pack()

        self.txt_telefono = ttk.Entry(self.ventana)
        self.txt_telefono.pack()

        # ==========================
        # Botones
        # ==========================

        ttk.Button(
            self.ventana,
            text="Registrar Cliente",
            command=self.registrar_cliente
        ).pack(pady=10)

        ttk.Button(
            self.ventana,
            text="Actualizar Lista",
            command=self.actualizar_lista
        ).pack()

        # ==========================
        # Lista
        # ==========================

        ttk.Label(
            self.ventana,
            text="Clientes registrados"
        ).pack(pady=10)

        self.lista = tk.Listbox(
            self.ventana,
            width=70,
            height=15
        )

        self.lista.pack()

        self.actualizar_lista()

    # ==========================================
    # Registrar cliente
    # ==========================================

    def registrar_cliente(self):

        try:

            self.gestor.registrar_cliente(
                self.txt_id.get(),
                self.txt_nombre.get(),
                self.txt_correo.get(),
                self.txt_telefono.get()
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado correctamente."
            )

            self.limpiar()
            self.actualizar_lista()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # Actualizar lista
    # ==========================================

    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for cliente in self.gestor.listar_clientes():

            self.lista.insert(
                tk.END,
                str(cliente)
            )

    # ==========================================
    # Limpiar controles
    # ==========================================

    def limpiar(self):

        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_correo.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)