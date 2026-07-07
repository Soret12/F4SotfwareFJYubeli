from tkinter import Tk
from interfaz.menu import MenuPrincipal


def main():
    ventana = Tk()
    app = MenuPrincipal(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
    