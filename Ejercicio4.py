import tkinter as tk
from tkinter import messagebox, ttk

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}"

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_info(self):
        jugadores_info = ', '.join([jugador.mostrar_info() for jugador in self.jugadores])
        return f"Equipo: {self.nombre}, Entrenador: {self.entrenador}, Jugadores: {jugadores_info}"

class Partido:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.resultado = None

    def jugar_partido(self, resultado):
        self.resultado = resultado

    def mostrar_resultado(self):
        return f"Partido: {self.equipo_local.nombre} vs {self.equipo_visitante.nombre}, Resultado: {self.resultado}, Estadio: {self.estadio.nombre}"

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_info(self):
        equipos_info = ', '.join([equipo.nombre for equipo in self.equipos])
        return f"Grupo: {self.nombre}, Equipos: {equipos_info}"

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.nombre}, Ciudad: {self.ciudad}, Capacidad: {self.capacidad}"

class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def generar_fixture(self):
        fixture = []
        for grupo in self.grupos:
            equipos = grupo.equipos
            for i in range(len(equipos)):
                for j in range(i + 1, len(equipos)):
                    estadio = self.estadios[(i + j) % len(self.estadios)]
                    partido = Partido(equipos[i], equipos[j], estadio)
                    fixture.append(partido)
        return fixture

class MundialGUI:
    def __init__(self, root):
        self.mundial = Mundial()
        self.root = root
        self.root.title("Sistema de Gestión de un Mundial de Fútbol")
        self.root.configure(bg="#f0f0f0")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Button(frame, text="Registrar Grupo", command=self.registrar_grupo, width=30).pack(pady=10)
        ttk.Button(frame, text="Registrar Estadio", command=self.registrar_estadio, width=30).pack(pady=10)
        ttk.Button(frame, text="Generar Fixture", command=self.generar_fixture, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Grupos", command=self.mostrar_grupos, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Estadios", command=self.mostrar_estadios, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Partidos", command=self.mostrar_partidos, width=30).pack(pady=10)

    def registrar_grupo(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Registrar Grupo", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre del Grupo").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            grupo = Grupo(nombre)
            self.mundial.registrar_grupo(grupo)
            messagebox.showinfo("Éxito", "Grupo registrado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Registrar", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def registrar_estadio(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Registrar Estadio", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre del Estadio").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        ttk.Label(frame, text="Ciudad").pack(pady=5)
        ciudad_entry = ttk.Entry(frame, width=50)
        ciudad_entry.pack(pady=5)

        ttk.Label(frame, text="Capacidad").pack(pady=5)
        capacidad_entry = ttk.Entry(frame, width=50)
        capacidad_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            ciudad = ciudad_entry.get()
            capacidad = capacidad_entry.get()

            estadio = Estadio(nombre, ciudad, capacidad)
            self.mundial.registrar_estadio(estadio)
            messagebox.showinfo("Éxito", "Estadio registrado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Registrar", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def generar_fixture(self):
        fixture = self.mundial.generar_fixture()
        self.fixture = fixture  # Guardamos el fixture generado
        messagebox.showinfo("Éxito", "Fixture generado correctamente.")
        self.mostrar_partidos()

    def mostrar_grupos(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Grupos Registrados", font=("Helvetica", 16)).pack(pady=10)
        grupos = [grupo.mostrar_info() for grupo in self.mundial.grupos]
        for grupo in grupos:
            ttk.Label(frame, text=grupo).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_estadios(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Estadios Registrados", font=("Helvetica", 16)).pack(pady=10)
        estadios = [estadio.mostrar_info() for estadio in self.mundial.estadios]
        for estadio in estadios:
            ttk.Label(frame, text=estadio).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_partidos(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Partidos", font=("Helvetica", 16)).pack(pady=10)
        if hasattr(self, 'fixture'):
            partidos = [partido.mostrar_resultado() for partido in self.fixture]
            for partido in partidos:
                ttk.Label(frame, text=partido).pack(pady=5)
        else:
            ttk.Label(frame, text="No se ha generado el fixture.").pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MundialGUI(root)
    root.mainloop()
