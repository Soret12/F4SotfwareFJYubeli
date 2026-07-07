# Función para centrar ventanas Tkinter

def centrar_ventana(ventana, ancho, alto):

    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    posicion_x = int((pantalla_ancho / 2) - (ancho / 2))
    posicion_y = int((pantalla_alto / 2) - (alto / 2))

    ventana.geometry(
        f"{ancho}x{alto}+{posicion_x}+{posicion_y}"
    )