import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class VentanaServicio:

    def __init__(self, padre, gestor_servicios):

        self.gestor = gestor_servicios

        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Gestión de Servicios")
        self.ventana.geometry("600x650")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        # Tipo de servicio
        ttk.Label(
            self.ventana,
            text="Tipo de Servicio:"
        ).pack()

        self.cmb_tipo = ttk.Combobox(
            self.ventana,
            values=["Sala", "Equipo", "Asesoria"],
            state="readonly"
        )
        self.cmb_tipo.current(0)
        self.cmb_tipo.pack()

        # Identificador
        ttk.Label(
            self.ventana,
            text="Identificador:"
        ).pack()

        self.txt_id = ttk.Entry(self.ventana)
        self.txt_id.pack()

        # Nombre
        ttk.Label(
            self.ventana,
            text="Nombre:"
        ).pack()

        self.txt_nombre = ttk.Entry(self.ventana)
        self.txt_nombre.pack()

        # Precio
        ttk.Label(
            self.ventana,
            text="Precio Base:"
        ).pack()

        self.txt_precio = ttk.Entry(self.ventana)
        self.txt_precio.pack()

        # Dato extra
        ttk.Label(
            self.ventana,
            text="Dato adicional\n"
                 "(Capacidad / Cantidad / Especialidad)"
        ).pack()

        self.txt_extra = ttk.Entry(self.ventana)
        self.txt_extra.pack()

        # Botón registrar
        ttk.Button(
            self.ventana,
            text="Registrar Servicio",
            command=self.registrar_servicio
        ).pack(pady=10)

        # Lista
        ttk.Label(
            self.ventana,
            text="Servicios registrados"
        ).pack()

        self.lista = tk.Listbox(
            self.ventana,
            width=70,
            height=12
        )

        self.lista.pack()

        self.actualizar_lista()

    # Registrar servicio
    def registrar_servicio(self):

        try:

            tipo = self.cmb_tipo.get()
            identificador = self.txt_id.get()
            nombre = self.txt_nombre.get()
            precio = float(self.txt_precio.get())

            if tipo == "Asesoria":
                dato_extra = self.txt_extra.get()
            else:
                dato_extra = int(self.txt_extra.get())

            self.gestor.registrar_servicio(
                tipo,
                identificador,
                nombre,
                precio,
                dato_extra
            )

            messagebox.showinfo(
                "Éxito",
                "Servicio registrado correctamente."
            )

            self.limpiar()

            self.actualizar_lista()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # Actualizar lista
    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for servicio in self.gestor.listar_servicios():

            self.lista.insert(
                tk.END,
                str(servicio)
            )

    # Limpiar cajas
    def limpiar(self):

        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_extra.delete(0, tk.END)

        self.cmb_tipo.current(0)