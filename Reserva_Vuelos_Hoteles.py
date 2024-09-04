import tkinter as tk
from tkinter import messagebox, ttk
from Gestion_Clientes import GestionClientes

vuelos_disponibles = [
    {"id": 1, "origen": "Cali", "destino": "Los Angeles", "precio": 3000000, "asientos_disponibles": 5},
    {"id": 2, "origen": "Bogotá", "destino": "Chicago", "precio": 2000000, "asientos_disponibles": 2},
    {"id": 3, "origen": "Rionegro", "destino": "Cali", "precio": 1500000, "asientos_disponibles": 0},
    {"id": 4, "origen": "Pereira", "destino": "Bogotá", "precio": 3500000, "asientos_disponibles": 3}
]

hoteles_disponibles = [
    {"id": 1, "nombre": "Hotel Los Angeles Dream", "ubicacion": "Los Angeles, CA", "precio_noche": 450000, "calificacion": 4},
    {"id": 2, "nombre": "Hotel Chicago Luxury", "ubicacion": "Chicago, IL", "precio_noche": 350000, "calificacion": 5},
    {"id": 3, "nombre": "Hotel Cali Comfort", "ubicacion": "Cali, Valle del Cauca", "precio_noche": 250000, "calificacion": 3},
    {"id": 4, "nombre": "Hotel Bogotá Royal", "ubicacion": "Bogotá, Cundinamarca", "precio_noche": 400000, "calificacion": 5}
]

reservas = []

def establecer_estilo():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='white', background='#0078D7', borderwidth=1)
    style.map('TButton',
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    style.configure('TLabel', font=('Helvetica', 12), background='#333333', foreground='white')
    style.configure('TEntry', foreground='black', fieldbackground='white', borderwidth=1)

def mostrar_vuelos_gui():
    ventana_vuelos = tk.Toplevel()
    ventana_vuelos.title("Vuelos Disponibles")
    ventana_vuelos.geometry("400x300")
    ventana_vuelos.configure(bg='#333333')
    
    for vuelo in vuelos_disponibles:
        vuelo_info = f"ID: {vuelo['id']}, Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Precio: ${vuelo['precio']}, Asientos: {vuelo['asientos_disponibles']}"
        ttk.Label(ventana_vuelos, text=vuelo_info, background='#333333', foreground='white').pack(pady=5)

def reservar_vuelo_gui(gestion_clientes):
    ventana_reserva = tk.Toplevel()
    ventana_reserva.title("Reservar Vuelo")
    ventana_reserva.geometry("400x300")
    ventana_reserva.configure(bg='#333333')

    ttk.Label(ventana_reserva, text="Ingrese su Identificación:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_reserva)
    entrada_identificacion.pack(pady=5)

    ttk.Label(ventana_reserva, text="ID del Vuelo:", background='#333333', foreground='white').pack(pady=5)
    entrada_id_vuelo = ttk.Entry(ventana_reserva)
    entrada_id_vuelo.pack(pady=5)

    def reservar():
        identificacion = entrada_identificacion.get()
        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        
        if not cliente:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado. Debe registrarse en Gestión Clientes.")
            return
        
        id_vuelo = int(entrada_id_vuelo.get())
        vuelo_seleccionado = next((v for v in vuelos_disponibles if v["id"] == id_vuelo), None)
        
        if not vuelo_seleccionado:
            messagebox.showwarning("No Encontrado", "Vuelo no encontrado. Intente nuevamente.")
            return
        
        if vuelo_seleccionado["asientos_disponibles"] == 0:
            messagebox.showwarning("Sin Asientos", "No hay asientos disponibles para este vuelo.")
            return
        
        cliente.historial_reservas.append({"tipo": "vuelo", "detalle": vuelo_seleccionado})
        vuelo_seleccionado["asientos_disponibles"] -= 1
        messagebox.showinfo("Reserva Exitosa", f"Reserva confirmada para el vuelo {vuelo_seleccionado['origen']} a {vuelo_seleccionado['destino']}.")

    ttk.Button(ventana_reserva, text="Confirmar Reserva", command=reservar).pack(pady=20)

def mostrar_hoteles_gui():
    ventana_hoteles = tk.Toplevel()
    ventana_hoteles.title("Hoteles Disponibles")
    ventana_hoteles.geometry("400x300")
    ventana_hoteles.configure(bg='#333333')
    
    for hotel in hoteles_disponibles:
        hotel_info = f"ID: {hotel['id']}, Nombre: {hotel['nombre']}, Ubicación: {hotel['ubicacion']}, Precio por noche: ${hotel['precio_noche']}, Calificación: {hotel['calificacion']}/5"
        ttk.Label(ventana_hoteles, text=hotel_info, background='#333333', foreground='white').pack(pady=5)

def reservar_hotel_gui(gestion_clientes):
    ventana_reserva = tk.Toplevel()
    ventana_reserva.title("Reservar Hotel")
    ventana_reserva.geometry("400x300")
    ventana_reserva.configure(bg='#333333')

    ttk.Label(ventana_reserva, text="Ingrese su Identificación:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_reserva)
    entrada_identificacion.pack(pady=5)

    ttk.Label(ventana_reserva, text="ID del Hotel:", background='#333333', foreground='white').pack(pady=5)
    entrada_id_hotel = ttk.Entry(ventana_reserva)
    entrada_id_hotel.pack(pady=5)

    def reservar():
        identificacion = entrada_identificacion.get()
        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        
        if not cliente:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado. Debe registrarse en Gestión Clientes.")
            return
        
        id_hotel = int(entrada_id_hotel.get())
        hotel_seleccionado = next((h for h in hoteles_disponibles if h["id"] == id_hotel), None)
        
        if not hotel_seleccionado:
            messagebox.showwarning("No Encontrado", "Hotel no encontrado. Intente nuevamente.")
            return
        
        cliente.historial_reservas.append({"tipo": "hotel", "detalle": hotel_seleccionado})
        messagebox.showinfo("Reserva Exitosa", f"Reserva confirmada para el hotel {hotel_seleccionado['nombre']} en {hotel_seleccionado['ubicacion']}.")

    ttk.Button(ventana_reserva, text="Confirmar Reserva", command=reservar).pack(pady=20)

def consultar_reservas_gui(gestion_clientes):
    ventana_consulta = tk.Toplevel()
    ventana_consulta.title("Consultar Reservas")
    ventana_consulta.geometry("400x300")
    ventana_consulta.configure(bg='#333333')

    ttk.Label(ventana_consulta, text="Ingrese su Identificación:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_consulta)
    entrada_identificacion.pack(pady=5)

    def consultar():
        identificacion = entrada_identificacion.get()
        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        
        if not cliente:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado. Debe registrarse en Gestión Clientes.")
            return
        
        if not cliente.historial_reservas:
            messagebox.showinfo("Sin Reservas", "No tiene reservas registradas.")
            return
        
        reservas_info = ""
        for reserva in cliente.historial_reservas:
            if reserva["tipo"] == "vuelo":
                reservas_info += f"Vuelo: {reserva['detalle']['origen']} a {reserva['detalle']['destino']} por ${reserva['detalle']['precio']}\n"
            elif reserva["tipo"] == "hotel":
                reservas_info += f"Hotel: {reserva['detalle']['nombre']} en {reserva['detalle']['ubicacion']} por ${reserva['detalle']['precio_noche']} la noche, Calificación: {reserva['detalle']['calificacion']}/5\n"
        
        messagebox.showinfo("Reservas", f"Reservas para {cliente.nombre_completo}:\n{reservas_info}")

    ttk.Button(ventana_consulta, text="Consultar", command=consultar).pack(pady=20)

def iniciar_reservas(gestion_clientes):
    root = tk.Tk()
    root.title("Reservas de Vuelos y Hoteles")
    root.geometry("600x500")
    root.configure(bg='#333333')
    establecer_estilo()

    ttk.Button(root, text="Mostrar Vuelos Disponibles", command=mostrar_vuelos_gui).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Reservar Vuelo", command=lambda: reservar_vuelo_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Mostrar Hoteles Disponibles", command=mostrar_hoteles_gui).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Reservar Hotel", command=lambda: reservar_hotel_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Consultar Reservas", command=lambda: consultar_reservas_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)

    root.mainloop()