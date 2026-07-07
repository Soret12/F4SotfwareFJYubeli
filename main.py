from tkinter import Tk
from interfaz.menu import MenuPrincipal
from interfaz.utilidades import centrar_ventana


def main():
    ventana = Tk()
    centrar_ventana(ventana,500,450)
    app = MenuPrincipal(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
    