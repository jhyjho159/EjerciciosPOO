/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio3;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class Ejercicio3 {

    static class Categoria {
        String nombre;

        Categoria(String nombre) {
            this.nombre = nombre;
        }

        String mostrarInfo() {
            return "Categoría: " + nombre;
        }
    }

    static class Producto {
        String nombre;
        double precio;
        Categoria categoria;

        Producto(String nombre, double precio, Categoria categoria) {
            this.nombre = nombre;
            this.precio = precio;
            this.categoria = categoria;
        }

        String mostrarInfo() {
            return "Producto: " + nombre + ", Precio: " + precio + ", " + categoria.mostrarInfo();
        }
    }

    static class Cliente {
        String nombre;
        String apellido;
        String idCliente;

        Cliente(String nombre, String apellido, String idCliente) {
            this.nombre = nombre;
            this.apellido = apellido;
            this.idCliente = idCliente;
        }

        String mostrarInfo() {
            return "Cliente: " + nombre + " " + apellido + ", ID: " + idCliente;
        }
    }

    static class ItemOrden {
        Producto producto;
        int cantidad;

        ItemOrden(Producto producto, int cantidad) {
            this.producto = producto;
            this.cantidad = cantidad;
        }

        double calcularSubtotal() {
            return producto.precio * cantidad;
        }
    }

    static class Orden {
        Cliente cliente;
        ArrayList<ItemOrden> items;
        double total;

        Orden(Cliente cliente) {
            this.cliente = cliente;
            this.items = new ArrayList<>();
            this.total = 0;
        }

        void agregarItem(ItemOrden item) {
            items.add(item);
            calcularTotal();
        }

        void calcularTotal() {
            total = 0;
            for (ItemOrden item : items) {
                total += item.calcularSubtotal();
            }
        }
    }

    static class Tienda {
        ArrayList<Producto> productos;
        ArrayList<Cliente> clientes;
        ArrayList<Orden> ordenes;
        ArrayList<Categoria> categorias;

        Tienda() {
            productos = new ArrayList<>();
            clientes = new ArrayList<>();
            ordenes = new ArrayList<>();
            categorias = new ArrayList<>();
        }

        void registrarProducto(Producto producto) {
            productos.add(producto);
        }

        void registrarCliente(Cliente cliente) {
            clientes.add(cliente);
        }

        void crearOrden(Orden orden) {
            ordenes.add(orden);
        }

        ArrayList<String> mostrarProductos() {
            ArrayList<String> productosInfo = new ArrayList<>();
            for (Producto producto : productos) {
                productosInfo.add(producto.mostrarInfo());
            }
            return productosInfo;
        }

        ArrayList<String> mostrarClientes() {
            ArrayList<String> clientesInfo = new ArrayList<>();
            for (Cliente cliente : clientes) {
                clientesInfo.add(cliente.mostrarInfo());
            }
            return clientesInfo;
        }

        ArrayList<String> mostrarOrdenes() {
            ArrayList<String> ordenesInfo = new ArrayList<>();
            for (Orden orden : ordenes) {
                StringBuilder itemsInfo = new StringBuilder();
                for (ItemOrden item : orden.items) {
                    itemsInfo.append(item.producto.nombre).append(" x").append(item.cantidad).append(", ");
                }
                ordenesInfo.add("Orden de " + orden.cliente.nombre + " " + orden.cliente.apellido + ": " +
                        itemsInfo.toString() + "Total: " + orden.total);
            }
            return ordenesInfo;
        }
    }

    static class TiendaGUI {
        JFrame frame;
        Tienda tienda;

        TiendaGUI() {
            tienda = new Tienda();
            frame = new JFrame("Sistema de Gestión de Tienda");
            frame.setSize(600, 400);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLayout(new BorderLayout());

            createMainMenu();
        }

        void createMainMenu() {
            JPanel panel = new JPanel(new GridLayout(6, 1));
            panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

            JButton registrarProductoBtn = new JButton("Registrar Producto");
            registrarProductoBtn.addActionListener(e -> registrarProducto());
            panel.add(registrarProductoBtn);

            JButton registrarClienteBtn = new JButton("Registrar Cliente");
            registrarClienteBtn.addActionListener(e -> registrarCliente());
            panel.add(registrarClienteBtn);

            JButton crearOrdenBtn = new JButton("Crear Orden");
            crearOrdenBtn.addActionListener(e -> crearOrden());
            panel.add(crearOrdenBtn);

            JButton mostrarProductosBtn = new JButton("Mostrar Productos");
            mostrarProductosBtn.addActionListener(e -> mostrarProductos());
            panel.add(mostrarProductosBtn);

            JButton mostrarClientesBtn = new JButton("Mostrar Clientes");
            mostrarClientesBtn.addActionListener(e -> mostrarClientes());
            panel.add(mostrarClientesBtn);

            JButton mostrarOrdenesBtn = new JButton("Mostrar Ordenes");
            mostrarOrdenesBtn.addActionListener(e -> mostrarOrdenes());
            panel.add(mostrarOrdenesBtn);

            frame.add(panel, BorderLayout.CENTER);
            frame.setVisible(true);
        }

        void registrarProducto() {
            JTextField nombreField = new JTextField(5);
            JTextField precioField = new JTextField(5);
            JComboBox<String> categoriaBox = new JComboBox<>();
            for (Categoria categoria : tienda.categorias) {
                categoriaBox.addItem(categoria.nombre);
            }

            JPanel myPanel = new JPanel();
            myPanel.add(new JLabel("Nombre:"));
            myPanel.add(nombreField);
            myPanel.add(Box.createHorizontalStrut(15)); // a spacer
            myPanel.add(new JLabel("Precio:"));
            myPanel.add(precioField);
            myPanel.add(new JLabel("Categoría:"));
            myPanel.add(categoriaBox);

            int result = JOptionPane.showConfirmDialog(null, myPanel,
                    "Registrar Producto", JOptionPane.OK_CANCEL_OPTION);
            if (result == JOptionPane.OK_OPTION) {
                String nombre = nombreField.getText();
                double precio = Double.parseDouble(precioField.getText());
                String categoriaNombre = (String) categoriaBox.getSelectedItem();
                Categoria categoria = tienda.categorias.stream()
                        .filter(c -> c.nombre.equals(categoriaNombre))
                        .findFirst()
                        .orElse(null);
                if (categoria != null) {
                    Producto producto = new Producto(nombre, precio, categoria);
                    tienda.registrarProducto(producto);
                    JOptionPane.showMessageDialog(frame, "Producto registrado con éxito");
                } else {
                    JOptionPane.showMessageDialog(frame, "Categoría no encontrada");
                }
            }
        }

        void registrarCliente() {
            JTextField nombreField = new JTextField(5);
            JTextField apellidoField = new JTextField(5);
            JTextField idClienteField = new JTextField(5);

            JPanel myPanel = new JPanel();
            myPanel.add(new JLabel("Nombre:"));
            myPanel.add(nombreField);
            myPanel.add(Box.createHorizontalStrut(15)); // a spacer
            myPanel.add(new JLabel("Apellido:"));
            myPanel.add(apellidoField);
            myPanel.add(new JLabel("ID Cliente:"));
            myPanel.add(idClienteField);

            int result = JOptionPane.showConfirmDialog(null, myPanel,
                    "Registrar Cliente", JOptionPane.OK_CANCEL_OPTION);
            if (result == JOptionPane.OK_OPTION) {
                String nombre = nombreField.getText();
                String apellido = apellidoField.getText();
                String idCliente = idClienteField.getText();
                Cliente cliente = new Cliente(nombre, apellido, idCliente);
                tienda.registrarCliente(cliente);
                JOptionPane.showMessageDialog(frame, "Cliente registrado con éxito");
            }
        }

        void crearOrden() {
            JComboBox<String> clienteBox = new JComboBox<>();
            for (Cliente cliente : tienda.clientes) {
                clienteBox.addItem(cliente.nombre + " " + cliente.apellido);
            }

            JComboBox<String> productoBox = new JComboBox<>();
            for (Producto producto : tienda.productos) {
                productoBox.addItem(producto.nombre);
            }

            JTextField cantidadField = new JTextField(5);

            JPanel myPanel = new JPanel();
            myPanel.add(new JLabel("Cliente:"));
            myPanel.add(clienteBox);
            myPanel.add(new JLabel("Producto:"));
            myPanel.add(productoBox);
            myPanel.add(Box.createHorizontalStrut(15)); // a spacer
            myPanel.add(new JLabel("Cantidad:"));
            myPanel.add(cantidadField);

            int result = JOptionPane.showConfirmDialog(null, myPanel,
                    "Crear Orden", JOptionPane.OK_CANCEL_OPTION);
            if (result == JOptionPane.OK_OPTION) {
                String clienteNombre = (String) clienteBox.getSelectedItem();
                String[] nombreApellido = clienteNombre.split(" ");
                Cliente cliente = tienda.clientes.stream()
                        .filter(c -> c.nombre.equals(nombreApellido[0]) && c.apellido.equals(nombreApellido[1]))
                        .findFirst()
                        .orElse(null);

                String productoNombre = (String) productoBox.getSelectedItem();
                Producto producto = tienda.productos.stream()
                        .filter(p -> p.nombre.equals(productoNombre))
                        .findFirst()
                        .orElse(null);

                int cantidad = Integer.parseInt(cantidadField.getText());

                if (cliente != null && producto != null) {
                    Orden orden = new Orden(cliente);
                    ItemOrden itemOrden = new ItemOrden(producto, cantidad);
                    orden.agregarItem(itemOrden);
                    tienda.crearOrden(orden);
                    JOptionPane.showMessageDialog(frame, "Orden creada con éxito");
                } else {
                    JOptionPane.showMessageDialog(frame, "Cliente o Producto no encontrados");
                }
            }
        }

        void mostrarProductos() {
            ArrayList<String> productosInfo = tienda.mostrarProductos();
            JOptionPane.showMessageDialog(frame, String.join("\n", productosInfo), "Productos", JOptionPane.INFORMATION_MESSAGE);
        }

        void mostrarClientes() {
            ArrayList<String> clientesInfo = tienda.mostrarClientes();
            JOptionPane.showMessageDialog(frame, String.join("\n", clientesInfo), "Clientes", JOptionPane.INFORMATION_MESSAGE);
        }

        void mostrarOrdenes() {
            ArrayList<String> ordenesInfo = tienda.mostrarOrdenes();
            JOptionPane.showMessageDialog(frame, String.join("\n", ordenesInfo), "Órdenes", JOptionPane.INFORMATION_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TiendaGUI::new);
    }
}
