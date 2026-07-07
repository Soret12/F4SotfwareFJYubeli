# Software FJ - Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios y reservas mediante una interfaz gráfica construida con la biblioteca Tkinter. El sistema fue desarrollado aplicando los principios de la Programación Orientada a Objetos (POO), utilizando clases abstractas, herencia, polimorfismo, encapsulamiento y manejo avanzado de excepciones, sin emplear bases de datos.

---

## Funcionalidades

* Registro de clientes con validaciones.
* Registro de servicios.
* Gestión de reservas.
* Confirmación y cancelación de reservas.
* Procesamiento del costo de una reserva.
* Manejo de excepciones personalizadas.
* Registro de eventos y errores en un archivo `logs.txt`.
* Simulación automática de operaciones válidas e inválidas.

---

## Tecnologías utilizadas

* Python 3
* Tkinter
* Programación Orientada a Objetos (POO)

---

## Estructura del proyecto

```text
SoftwareFJ/
│
├── interfaz/
│   ├── menu.py
│   ├── ventana_cliente.py
│   ├── ventana_servicio.py
│   ├── ventana_reserva.py
│
├── modelos/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── sala.py
│   ├── equipo.py
│   ├── asesoria.py
│   ├── reserva.py
│   └── excepciones.py
│
├── servicios/
│   ├── gestor_clientes.py
│   ├── gestor_servicios.py
│   ├── gestor_reservas.py
│   └── logger.py
│
├── logs.txt
├── main.py
└── README.md
```

---

## Cómo ejecutar el proyecto

1. Tener instalado Python 3.
2. Descargar o clonar el repositorio.
3. Abrir el proyecto en Visual Studio Code o cualquier editor compatible.
4. Ejecutar el archivo:

```bash
python main.py
```

---

## Características implementadas

* Programación Orientada a Objetos.
* Clases abstractas.
* Herencia.
* Polimorfismo.
* Encapsulamiento.
* Sobrescritura y métodos con parámetros opcionales.
* Excepciones personalizadas.
* Manejo de excepciones (`try`, `except`, `else` y `finally` donde corresponde).
* Interfaz gráfica desarrollada con Tkinter.
* Registro de eventos mediante archivo de logs.
* Gestión de información sin utilizar bases de datos.

---

## Autor

Yubeli Soret Carabalí Sandoval
