import tkinter as tk
from tkinter import messagebox, ttk

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Horario: {self.dia}, {self.hora_inicio}-{self.hora_fin}"

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def mostrar_info(self):
        asignaturas_info = ', '.join([asig.nombre for asig in self.asignaturas])
        return f"Profesor: {self.nombre} {self.apellido}, Asignaturas: {asignaturas_info}"

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        cursos_info = ', '.join([curso.nombre for curso in self.cursos])
        return f"Estudiante: {self.nombre} {self.apellido}, ID: {self.id_estudiante}, Cursos: {cursos_info}"

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        return f"Asignatura: {self.nombre}, Profesor: {self.profesor.nombre} {self.profesor.apellido}"

class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        return f"Evaluacion: Curso: {self.curso.nombre}, Estudiante: {self.estudiante.nombre} {self.estudiante.apellido}, Nota: {self.nota}"

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.agregar_curso(self)

    def mostrar_info(self):
        estudiantes_info = ', '.join([f"{est.nombre} {est.apellido}" for est in self.estudiantes])
        return (f"Curso: {self.nombre}, Profesor: {self.profesor.nombre} {self.profesor.apellido}, "
                f"Estudiantes: {estudiantes_info}, {self.horario.mostrar_info()}")

class SistemaCursos:
    def __init__(self):
        self.profesores = []
        self.estudiantes = []
        self.cursos = []
        self.asignaturas = []
        self.evaluaciones = []

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)

    def mostrar_profesores(self):
        return [profesor.mostrar_info() for profesor in self.profesores]

    def mostrar_estudiantes(self):
        return [estudiante.mostrar_info() for estudiante in self.estudiantes]

    def mostrar_cursos(self):
        return [curso.mostrar_info() for curso in self.cursos]

    def mostrar_asignaturas(self):
        return [asignatura.mostrar_info() for asignatura in self.asignaturas]

    def mostrar_evaluaciones(self):
        return [evaluacion.mostrar_info() for evaluacion in self.evaluaciones]

class SistemaCursosGUI:
    def __init__(self, root):
        self.sistema = SistemaCursos()
        self.root = root
        self.root.title("Sistema de Gestión de Cursos")
        self.root.configure(bg="#f0f0f0")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Button(frame, text="Registrar Profesor", command=self.registrar_profesor, width=30).pack(pady=10)
        ttk.Button(frame, text="Registrar Estudiante", command=self.registrar_estudiante, width=30).pack(pady=10)
        ttk.Button(frame, text="Crear Curso", command=self.crear_curso, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Profesores", command=self.mostrar_profesores, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Estudiantes", command=self.mostrar_estudiantes, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Cursos", command=self.mostrar_cursos, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Asignaturas", command=self.mostrar_asignaturas, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Evaluaciones", command=self.mostrar_evaluaciones, width=30).pack(pady=10)

    def registrar_profesor(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Registrar Profesor", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        ttk.Label(frame, text="Apellido").pack(pady=5)
        apellido_entry = ttk.Entry(frame, width=50)
        apellido_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()

            profesor = Profesor(nombre, apellido)
            self.sistema.agregar_profesor(profesor)
            messagebox.showinfo("Éxito", "Profesor registrado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Registrar", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def registrar_estudiante(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Registrar Estudiante", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        ttk.Label(frame, text="Apellido").pack(pady=5)
        apellido_entry = ttk.Entry(frame, width=50)
        apellido_entry.pack(pady=5)

        ttk.Label(frame, text="ID Estudiante").pack(pady=5)
        id_estudiante_entry = ttk.Entry(frame, width=50)
        id_estudiante_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            id_estudiante = id_estudiante_entry.get()

            estudiante = Estudiante(nombre, apellido, id_estudiante)
            self.sistema.agregar_estudiante(estudiante)
            messagebox.showinfo("Éxito", "Estudiante registrado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Registrar", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def crear_curso(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Crear Curso", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        ttk.Label(frame, text="Profesor").pack(pady=5)
        profesor_entry = ttk.Entry(frame, width=50)
        profesor_entry.pack(pady=5)

        ttk.Label(frame, text="Día").pack(pady=5)
        dia_entry = ttk.Entry(frame, width=50)
        dia_entry.pack(pady=5)

        ttk.Label(frame, text="Hora Inicio").pack(pady=5)
        hora_inicio_entry = ttk.Entry(frame, width=50)
        hora_inicio_entry.pack(pady=5)

        ttk.Label(frame, text="Hora Fin").pack(pady=5)
        hora_fin_entry = ttk.Entry(frame, width=50)
        hora_fin_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            nombre_profesor = profesor_entry.get()
            dia = dia_entry.get()
            hora_inicio = hora_inicio_entry.get()
            hora_fin = hora_fin_entry.get()

            # Buscar el profesor por nombre
            profesor = next((prof for prof in self.sistema.profesores if prof.nombre == nombre_profesor), None)
            if profesor is None:
                messagebox.showerror("Error", f"No se encontró al profesor '{nombre_profesor}'.")
                return

            horario = Horario(dia, hora_inicio, hora_fin)
            curso = Curso(nombre, profesor, horario)
            self.sistema.agregar_curso(curso)
            messagebox.showinfo("Éxito", "Curso creado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Crear Curso", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def mostrar_profesores(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Profesores Registrados", font=("Helvetica", 16)).pack(pady=10)
        profesores = self.sistema.mostrar_profesores()
        for profesor in profesores:
            ttk.Label(frame, text=profesor).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_estudiantes(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Estudiantes Registrados", font=("Helvetica", 16)).pack(pady=10)
        estudiantes = self.sistema.mostrar_estudiantes()
        for estudiante in estudiantes:
            ttk.Label(frame, text=estudiante).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_cursos(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Cursos Registrados", font=("Helvetica", 16)).pack(pady=10)
        cursos = self.sistema.mostrar_cursos()
        for curso in cursos:
            ttk.Label(frame, text=curso).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_asignaturas(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Asignaturas Registradas", font=("Helvetica", 16)).pack(pady=10)
        asignaturas = self.sistema.mostrar_asignaturas()
        for asignatura in asignaturas:
            ttk.Label(frame, text=asignatura).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_evaluaciones(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Evaluaciones Registradas", font=("Helvetica", 16)).pack(pady=10)
        evaluaciones = self.sistema.mostrar_evaluaciones()
        for evaluacion in evaluaciones:
            ttk.Label(frame, text=evaluacion).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaCursosGUI(root)
    root.mainloop()
