import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Definición de las clases necesarias

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"Autor: {self.nombre} {self.apellido}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        return (f"Libro: {self.titulo}, ISBN: {self.isbn}, "
                f"{self.autor.mostrar_info()}, {self.categoria.mostrar_info()}")

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido}, ID: {self.id_usuario}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Préstamo: {self.libro.titulo} a {self.usuario.nombre} {self.usuario.apellido}, "
                f"Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, libro, usuario):
        if libro in self.libros:
            prestamo = Prestamo(libro, usuario, datetime.now().strftime("%Y-%m-%d"))
            self.prestamos.append(prestamo)
            return f"Préstamo realizado: {libro.titulo} a {usuario.nombre} {usuario.apellido}"
        else:
            return "El libro no está disponible en la biblioteca"

    def devolver_libro(self, prestamo):
        if prestamo in self.prestamos:
            prestamo.fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
            return f"Libro devuelto: {prestamo.libro.titulo} por {prestamo.usuario.nombre} {prestamo.usuario.apellido}"
        else:
            return "Préstamo no encontrado"

    def mostrar_libros(self):
        return [libro.mostrar_info() for libro in self.libros]

# Definición de la clase para la interfaz gráfica

class BibliotecaGUI:
    def __init__(self, root):
        self.biblioteca = Biblioteca()  # Inicializar correctamente la biblioteca
        self.root = root
        self.root.title("Biblioteca")
        self.create_main_menu()

    def create_main_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        libro_menu = tk.Menu(menu)
        menu.add_cascade(label="Libros", menu=libro_menu)
        libro_menu.add_command(label="Registrar", command=self.registrar_libro)
        libro_menu.add_command(label="Mostrar", command=self.mostrar_libros)

        usuario_menu = tk.Menu(menu)
        menu.add_cascade(label="Usuarios", menu=usuario_menu)
        usuario_menu.add_command(label="Registrar", command=self.registrar_usuario)

        prestamo_menu = tk.Menu(menu)
        menu.add_cascade(label="Préstamos", menu=prestamo_menu)
        prestamo_menu.add_command(label="Realizar", command=self.realizar_prestamo)
        prestamo_menu.add_command(label="Devolver", command=self.devolver_libro)

    def registrar_libro(self):
        self.clear_frame()
        tk.Label(self.root, text="Registrar Libro").pack()

        tk.Label(self.root, text="Título").pack()
        titulo_entry = tk.Entry(self.root)
        titulo_entry.pack()

        tk.Label(self.root, text="ISBN").pack()
        isbn_entry = tk.Entry(self.root)
        isbn_entry.pack()

        tk.Label(self.root, text="Nombre del Autor").pack()
        nombre_autor_entry = tk.Entry(self.root)
        nombre_autor_entry.pack()

        tk.Label(self.root, text="Apellido del Autor").pack()
        apellido_autor_entry = tk.Entry(self.root)
        apellido_autor_entry.pack()

        tk.Label(self.root, text="Categoría").pack()
        categoria_entry = tk.Entry(self.root)
        categoria_entry.pack()

        def submit():
            titulo = titulo_entry.get()
            isbn = isbn_entry.get()
            nombre_autor = nombre_autor_entry.get()
            apellido_autor = apellido_autor_entry.get()
            nombre_categoria = categoria_entry.get()

            autor = Autor(nombre_autor, apellido_autor)
            categoria = Categoria(nombre_categoria)
            libro = Libro(titulo, isbn, autor, categoria)
            self.biblioteca.registrar_libro(libro)
            messagebox.showinfo("Éxito", "Libro registrado correctamente.")
            self.clear_frame()
            self.create_main_menu()

        tk.Button(self.root, text="Registrar", command=submit).pack()

    def registrar_usuario(self):
        self.clear_frame()
        tk.Label(self.root, text="Registrar Usuario").pack()

        tk.Label(self.root, text="Nombre").pack()
        nombre_entry = tk.Entry(self.root)
        nombre_entry.pack()

        tk.Label(self.root, text="Apellido").pack()
        apellido_entry = tk.Entry(self.root)
        apellido_entry.pack()

        tk.Label(self.root, text="ID Usuario").pack()
        id_usuario_entry = tk.Entry(self.root)
        id_usuario_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            id_usuario = id_usuario_entry.get()

            usuario = Usuario(nombre, apellido, id_usuario)
            self.biblioteca.registrar_usuario(usuario)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.clear_frame()
            self.create_main_menu()

        tk.Button(self.root, text="Registrar", command=submit).pack()

    def realizar_prestamo(self):
        self.clear_frame()
        tk.Label(self.root, text="Realizar Préstamo").pack()

        tk.Label(self.root, text="ISBN del Libro").pack()
        isbn_entry = tk.Entry(self.root)
        isbn_entry.pack()

        tk.Label(self.root, text="ID Usuario").pack()
        id_usuario_entry = tk.Entry(self.root)
        id_usuario_entry.pack()

        def submit():
            isbn = isbn_entry.get()
            id_usuario = id_usuario_entry.get()

            libro = next((lib for lib in self.biblioteca.libros if lib.isbn == isbn), None)
            usuario = next((usr for usr in self.biblioteca.usuarios if usr.id_usuario == id_usuario), None)

            if libro and usuario:
                message = self.biblioteca.realizar_prestamo(libro, usuario)
                messagebox.showinfo("Resultado", message)
            else:
                messagebox.showerror("Error", "Libro o usuario no encontrado.")
            self.clear_frame()
            self.create_main_menu()

        tk.Button(self.root, text="Realizar", command=submit).pack()

    def devolver_libro(self):
        self.clear_frame()
        tk.Label(self.root, text="Devolver Libro").pack()

        tk.Label(self.root, text="ISBN del Libro").pack()
        isbn_entry = tk.Entry(self.root)
        isbn_entry.pack()

        tk.Label(self.root, text="ID Usuario").pack()
        id_usuario_entry = tk.Entry(self.root)
        id_usuario_entry.pack()

        def submit():
            isbn = isbn_entry.get()
            id_usuario = id_usuario_entry.get()

            prestamo = next((pre for pre in self.biblioteca.prestamos if pre.libro.isbn == isbn and pre.usuario.id_usuario == id_usuario), None)

            if prestamo:
                message = self.biblioteca.devolver_libro(prestamo)
                messagebox.showinfo("Resultado", message)
            else:
                messagebox.showerror("Error", "Préstamo no encontrado.")
            self.clear_frame()
            self.create_main_menu()

        tk.Button(self.root, text="Devolver", command=submit).pack()

    def mostrar_libros(self):
        self.clear_frame()
        tk.Label(self.root, text="Libros Registrados").pack()

        libros = self.biblioteca.mostrar_libros()
        for libro in libros:
            tk.Label(self.root, text=libro).pack()

        tk.Button(self.root, text="Volver", command=self.create_main_menu).pack()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()  # Inicializa la ventana principal de tkinter
    app = BibliotecaGUI(root)  # Crea una instancia de la clase BibliotecaGUI
    root.mainloop()  # Ejecuta el bucle principal de tkinter
