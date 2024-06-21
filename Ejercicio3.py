import tkinter as tk
from tkinter import messagebox, ttk

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, {self.categoria.mostrar_info()}"

class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente

    def mostrar_info(self):
        return f"Cliente: {self.nombre} {self.apellido}, ID: {self.id_cliente}"

class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0

    def agregar_item(self, item):
        self.items.append(item)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(item.calcular_subtotal() for item in self.items)

class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []
        self.categorias = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_orden(self, orden):
        self.ordenes.append(orden)

    def mostrar_productos(self):
        return [producto.mostrar_info() for producto in self.productos]

    def mostrar_clientes(self):
        return [cliente.mostrar_info() for cliente in self.clientes]

    def mostrar_ordenes(self):
        ordenes_info = []
        for orden in self.ordenes:
            items_info = [f"{item.producto.nombre} x{item.cantidad}" for item in orden.items]
            ordenes_info.append(f"Orden de {orden.cliente.nombre} {orden.cliente.apellido}: {', '.join(items_info)}, Total: {orden.total}")
        return ordenes_info

class TiendaGUI:
    def __init__(self, root):
        self.tienda = Tienda()
        self.root = root
        self.root.title("Sistema de Gestión de Tienda")
        self.root.configure(bg="#f0f0f0")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Button(frame, text="Registrar Producto", command=self.registrar_producto, width=30).pack(pady=10)
        ttk.Button(frame, text="Registrar Cliente", command=self.registrar_cliente, width=30).pack(pady=10)
        ttk.Button(frame, text="Crear Orden", command=self.crear_orden, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Productos", command=self.mostrar_productos, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Clientes", command=self.mostrar_clientes, width=30).pack(pady=10)
        ttk.Button(frame, text="Mostrar Ordenes", command=self.mostrar_ordenes, width=30).pack(pady=10)

    def registrar_producto(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Registrar Producto", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        ttk.Label(frame, text="Precio").pack(pady=5)
        precio_entry = ttk.Entry(frame, width=50)
        precio_entry.pack(pady=5)

        ttk.Label(frame, text="Categoría").pack(pady=5)
        categoria_entry = ttk.Entry(frame, width=50)
        categoria_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            precio = float(precio_entry.get())
            nombre_categoria = categoria_entry.get()

            categoria = next((cat for cat in self.tienda.categorias if cat.nombre == nombre_categoria), None)
            if not categoria:
                categoria = Categoria(nombre_categoria)
                self.tienda.categorias.append(categoria)

            producto = Producto(nombre, precio, categoria)
            self.tienda.registrar_producto(producto)
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Registrar", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def registrar_cliente(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Registrar Cliente", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="Nombre").pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)

        ttk.Label(frame, text="Apellido").pack(pady=5)
        apellido_entry = ttk.Entry(frame, width=50)
        apellido_entry.pack(pady=5)

        ttk.Label(frame, text="ID Cliente").pack(pady=5)
        id_cliente_entry = ttk.Entry(frame, width=50)
        id_cliente_entry.pack(pady=5)

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            id_cliente = id_cliente_entry.get()

            cliente = Cliente(nombre, apellido, id_cliente)
            self.tienda.registrar_cliente(cliente)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            self.create_main_menu()

        ttk.Button(frame, text="Registrar", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def crear_orden(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Crear Orden", font=("Helvetica", 16)).pack(pady=10)
        ttk.Label(frame, text="ID Cliente").pack(pady=5)
        id_cliente_entry = ttk.Entry(frame, width=50)
        id_cliente_entry.pack(pady=5)

        items_frame = ttk.Frame(frame)
        items_frame.pack(pady=5)
        items = []

        def agregar_item():
            producto_nombre = producto_entry.get()
            cantidad = int(cantidad_entry.get())

            producto = next((prod for prod in self.tienda.productos if prod.nombre == producto_nombre), None)
            if producto:
                items.append(ItemOrden(producto, cantidad))
                item_label = ttk.Label(items_frame, text=f"{producto_nombre} x{cantidad}")
                item_label.pack()

        ttk.Label(frame, text="Producto").pack(pady=5)
        producto_entry = ttk.Entry(frame, width=50)
        producto_entry.pack(pady=5)

        ttk.Label(frame, text="Cantidad").pack(pady=5)
        cantidad_entry = ttk.Entry(frame, width=50)
        cantidad_entry.pack(pady=5)

        ttk.Button(frame, text="Agregar Item", command=agregar_item).pack(pady=10)

        def submit():
            id_cliente = id_cliente_entry.get()
            cliente = next((cli for cli in self.tienda.clientes if cli.id_cliente == id_cliente), None)
            if cliente:
                orden = Orden(cliente)
                for item in items:
                    orden.agregar_item(item)
                self.tienda.crear_orden(orden)
                messagebox.showinfo("Éxito", "Orden creada correctamente.")
            else:
                messagebox.showerror("Error", "Cliente no encontrado.")
            self.create_main_menu()

        ttk.Button(frame, text="Crear Orden", command=submit).pack(pady=20)
        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack()

    def mostrar_productos(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Productos Registrados", font=("Helvetica", 16)).pack(pady=10)
        productos = self.tienda.mostrar_productos()
        for producto in productos:
            ttk.Label(frame, text=producto).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_clientes(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Clientes Registrados", font=("Helvetica", 16)).pack(pady=10)
        clientes = self.tienda.mostrar_clientes()
        for cliente in clientes:
            ttk.Label(frame, text=cliente).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def mostrar_ordenes(self):
        self.clear_frame()
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Ordenes Registradas", font=("Helvetica", 16)).pack(pady=10)
        ordenes = self.tienda.mostrar_ordenes()
        for orden in ordenes:
            ttk.Label(frame, text=orden).pack(pady=5)

        ttk.Button(frame, text="Volver", command=self.create_main_menu).pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TiendaGUI(root)
    root.mainloop()
