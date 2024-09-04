import tkinter as tk
from tkinter import messagebox, ttk

class Cliente:
    contador_id = 1

    def __init__(self, nombre_completo, direccion, telefono, correo, identificacion):
        self.id_cliente = f"ID_User{Cliente.contador_id}"
        Cliente.contador_id += 1
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.historial_reservas = []

    def obtener_historial(self):
        return self.historial_reservas

class GestionClientes:
    def __init__(self):
        self.clientes = {}

    def registrar_cliente(self, nombre_completo, direccion, telefono, correo, identificacion):
        if identificacion in self.clientes:
            return None

        cliente = Cliente(nombre_completo, direccion, telefono, correo, identificacion)
        self.clientes[identificacion] = cliente
        return cliente.id_cliente

    def buscar_cliente(self, identificacion=None):
        return self.clientes.get(identificacion)

    def buscar_clientes_por_rango(self, id_inicio, id_fin):
        resultados = [cliente for cliente in self.clientes.values() if id_inicio <= cliente.id_cliente <= id_fin]
        return resultados

    def enviar_correo_confirmacion(self, correo_destino, asunto, cuerpo):
        messagebox.showinfo("Correo Enviado", f"Correo enviado a {correo_destino} con el asunto: {asunto}")

    def generar_notificacion(self, cliente, mensaje):
        messagebox.showinfo("Notificación", f"Notificación enviada correctamente a {cliente.nombre_completo}: {mensaje}")

def establecer_estilo():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='white', background='#0078D7', borderwidth=1)
    style.map('TButton',
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    style.configure('TLabel', font=('Helvetica', 12), background='#333333', foreground='white')
    style.configure('TEntry', foreground='black', fieldbackground='white', borderwidth=1)

def registrar_cliente_gui(gestion_clientes, root):
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registrese como Cliente")
    ventana_registro.geometry("400x350")
    ventana_registro.configure(bg='#333333')

    ttk.Label(ventana_registro, text="Nombre Completo:", background='#333333', foreground='white').pack(pady=5)
    entrada_nombre = ttk.Entry(ventana_registro)
    entrada_nombre.pack(pady=5)

    ttk.Label(ventana_registro, text="Identificación:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_registro)
    entrada_identificacion.pack(pady=5)

    ttk.Label(ventana_registro, text="Dirección:", background='#333333', foreground='white').pack(pady=5)
    entrada_direccion = ttk.Entry(ventana_registro)
    entrada_direccion.pack(pady=5)

    ttk.Label(ventana_registro, text="Teléfono:", background='#333333', foreground='white').pack(pady=5)
    entrada_telefono = ttk.Entry(ventana_registro)
    entrada_telefono.pack(pady=5)

    ttk.Label(ventana_registro, text="Correo Electrónico:", background='#333333', foreground='white').pack(pady=5)
    entrada_correo = ttk.Entry(ventana_registro)
    entrada_correo.pack(pady=5)

    def registrar_cliente_y_cerrar():
        nombre = entrada_nombre.get()
        identificacion = entrada_identificacion.get()
        direccion = entrada_direccion.get()
        telefono = entrada_telefono.get()
        correo = entrada_correo.get()
        if nombre and identificacion and direccion and telefono and correo:
            id_cliente = gestion_clientes.registrar_cliente(nombre, direccion, telefono, correo, identificacion)
            if id_cliente:
                messagebox.showinfo("Completo", f"Cliente registrado con éxito. ID: {id_cliente}")
            else:
                messagebox.showwarning("Error", "Ya existe un cliente con esa identificación.")
            ventana_registro.destroy()
        else:
            messagebox.showwarning("Error", "Todos los campos deben estar llenos")

    ttk.Button(ventana_registro, text="Registrese como Cliente", command=registrar_cliente_y_cerrar).pack(pady=20)

def buscar_cliente_gui(gestion_clientes):
    ventana_buscar = tk.Toplevel()
    ventana_buscar.title("Busqueda de Cliente")
    ventana_buscar.geometry("400x200")
    ventana_buscar.configure(bg='#333333')

    ttk.Label(ventana_buscar, text="Identificación del Cliente:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_buscar)
    entrada_identificacion.pack(pady=5)

    def buscar_y_mostrar_cliente():
        identificacion = entrada_identificacion.get()
        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        if cliente:
            mensaje = f"ID: {cliente.id_cliente}\nNombre: {cliente.nombre_completo}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}\nCorreo: {cliente.correo}"
            messagebox.showinfo("Cliente Encontrado", mensaje)
        else:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado")

    ttk.Button(ventana_buscar, text="Busqueda de Cliente", command=buscar_y_mostrar_cliente).pack(pady=20)

def buscar_clientes_por_rango_gui(gestion_clientes):
    ventana_buscar = tk.Toplevel()
    ventana_buscar.title("Busqueda Masiva de Clientes")
    ventana_buscar.geometry("400x200")
    ventana_buscar.configure(bg='#333333')

    ttk.Label(ventana_buscar, text="Rango de ID (Inicio):", background='#333333', foreground='white').pack(pady=5)
    entrada_id_inicio = ttk.Entry(ventana_buscar)
    entrada_id_inicio.pack(pady=5)

    ttk.Label(ventana_buscar, text="Rango de ID (Fin):", background='#333333', foreground='white').pack(pady=5)
    entrada_id_fin = ttk.Entry(ventana_buscar)
    entrada_id_fin.pack(pady=5)

    def buscar_y_mostrar_clientes():
        id_inicio = entrada_id_inicio.get()
        id_fin = entrada_id_fin.get()
        clientes_encontrados = gestion_clientes.buscar_clientes_por_rango(id_inicio, id_fin)
        if clientes_encontrados:
            mensaje = "\n\n".join([f"ID: {cliente.id_cliente}\nNombre: {cliente.nombre_completo}\nIdentificación: {cliente.identificacion}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}\nCorreo: {cliente.correo}" for cliente in clientes_encontrados])
            messagebox.showinfo("Clientes Encontrados", mensaje)
        else:
            messagebox.showinfo("No Encontrado", "No se encontraron clientes en ese rango de IDs.")

    ttk.Button(ventana_buscar, text="Buscar Clientes", command=buscar_y_mostrar_clientes).pack(pady=20)

def enviar_correo_confirmacion_gui(gestion_clientes):
    ventana_correo = tk.Toplevel()
    ventana_correo.title("Enviar Confirmación")
    ventana_correo.geometry("400x300")
    ventana_correo.configure(bg='#333333')

    ttk.Label(ventana_correo, text="Identificación del Cliente:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_correo)
    entrada_identificacion.pack(pady=5)

    ttk.Label(ventana_correo, text="Asunto:", background='#333333', foreground='white').pack(pady=5)
    entrada_asunto = ttk.Entry(ventana_correo)
    entrada_asunto.pack(pady=5)

    ttk.Label(ventana_correo, text="Mensaje:", background='#333333', foreground='white').pack(pady=5)
    entrada_mensaje = ttk.Entry(ventana_correo)
    entrada_mensaje.pack(pady=5)

    def enviar_correo():
        identificacion = entrada_identificacion.get()
        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        if cliente:
            asunto = entrada_asunto.get()
            mensaje = entrada_mensaje.get()
            gestion_clientes.enviar_correo_confirmacion(cliente.correo, asunto, mensaje)
            ventana_correo.destroy()
        else:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado")

    ttk.Button(ventana_correo, text="Enviar Correo", command=enviar_correo).pack(pady=20)

def generar_notificacion_gui(gestion_clientes):
    ventana_notificacion = tk.Toplevel()
    ventana_notificacion.title("Generar Notificación")
    ventana_notificacion.geometry("400x250")
    ventana_notificacion.configure(bg='#333333')

    ttk.Label(ventana_notificacion, text="Identificación del Cliente:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_notificacion)
    entrada_identificacion.pack(pady=5)

    ttk.Label(ventana_notificacion, text="Mensaje:", background='#333333', foreground='white').pack(pady=5)
    entrada_mensaje = ttk.Entry(ventana_notificacion)
    entrada_mensaje.pack(pady=5)

    def generar_notificacion():
        identificacion = entrada_identificacion.get()
        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        if cliente:
            mensaje = entrada_mensaje.get()
            gestion_clientes.generar_notificacion(cliente, mensaje)
            ventana_notificacion.destroy()
        else:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado")

    ttk.Button(ventana_notificacion, text="Generar Notificación", command=generar_notificacion).pack(pady=20)

def iniciar_aplicacion(gestion_clientes):
    root = tk.Tk()
    root.title("Gestión de Clientes")
    root.geometry("600x500")
    root.configure(bg='#333333')
    establecer_estilo()

    ttk.Button(root, text="Registrese como Cliente", command=lambda: registrar_cliente_gui(gestion_clientes, root)).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Busqueda de Cliente", command=lambda: buscar_cliente_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Busqueda Masiva de Clientes", command=lambda: buscar_clientes_por_rango_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Enviar Correo de Confirmación", command=lambda: enviar_correo_confirmacion_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Generar Notificación", command=lambda: generar_notificacion_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)

    root.mainloop()