import tkinter as tk
from tkinter import messagebox, ttk
from Gestion_Clientes import GestionClientes

planes_turisticos = {
    "San Andrés": [
        "Plan 1: 5 días y 4 noches, con vuelo en Avianca y estancia en hotel Magura (calificación 8.0). Valor: 981.000 COP por persona",
        "Plan 2: 6 días y 5 noches, con vuelo en Avianca y estancia en hotel Heaven's Beach (calificación 8.0). Valor: 1'000.000 COP por persona",
        "Plan 3: 7 días y 6 noches, con vuelo en Avianca y estancia en hotel Erlife (calificación 8.0). Valor: 1'345.000 COP por persona",
        "Plan 4: 8 días y 7 noches, con vuelo en Avianca y estancia en hotel Marea Pacífica (calificación 8.5). Valor: 4'500.000 COP por familia de 5 personas"
    ],
    "Cartagena": [
        "Plan 1: 5 días y 4 noches, con vuelo en Latam y estancia en hotel Makena (calificación 7.3). Valor: 805.000 COP por persona",
        "Plan 2: 6 días y 5 noches, con vuelo en Latam y estancia en hotel Bamboleo (calificación 7.5). Valor: 873.000 COP por persona",
        "Plan 3: 7 días y 6 noches, con vuelo en Latam y estancia en hotel Yhara (calificación 8.0). Valor: 2'650.000 COP por pareja",
        "Plan 4: 8 días y 7 noches, con vuelo en Latam y estancia en hotel Me llamo cumbia (calificación 8.5). Valor: 1'890.000 COP por persona"
    ],
    "Bucaramanga": [
        "Plan 1: 5 días y 4 noches, con vuelo en Avianca y estancia en hotel Bosque Grande (calificación 7.3). Valor: 700.000 COP por persona",
        "Plan 2: 6 días y 5 noches, con vuelo en Latam y estancia en hotel Las Palmas (calificación 8.0). Valor: 1'590.000 COP por pareja",
        "Plan 3: 7 días y 6 noches, con vuelo en Avianca y estancia en hotel Crystal Clear (calificación 8.0). Valor: 1'332.000 COP por persona",
        "Plan 4: 8 días y 7 noches, con vuelo en Latam y estancia en hotel Las Luces (calificación 8.5). Valor: 1'685.000 COP por persona"
    ],
    "Cali": [
        "Plan 1: 5 días y 4 noches, con vuelo en Latam y estancia en hotel Cielo Claro (calificación 7.0). Valor: 640.000 COP por persona",
        "Plan 2: 6 días y 5 noches, con vuelo en Latam y estancia en hotel Las cañas (calificación 8.0). Valor: 4'500.000 COP por familia de 5 personas",
        "Plan 3: 7 días y 6 noches, con vuelo en Avianca y estancia en hotel La coordillera (calificación 8.0). Valor: 1'450.000 COP por persona",
        "Plan 4: 8 días y 7 noches, con vuelo en Avianca y estancia en hotel Montañas Rojas (calificación 8.5). Valor: 1'740.000 COP por persona"
    ],
    "Bogotá": [
        "Plan 1: 5 días y 4 noches, con vuelo en Avianca y estancia en hotel Santo Tomás (calificación 8.0). Valor: 995.000 COP por persona",
        "Plan 2: 6 días y 5 noches, con vuelo en Latam y estancia en hotel Rosales (calificación 8.0). Valor: 1'200.000 COP por persona",
        "Plan 3: 7 días y 6 noches, con vuelo en Latam y estancia en hotel Los pinos (calificación 8.0). Valor: 7'250.000 COP por familia de 5 personas",
        "Plan 4: 8 días y 7 noches, con vuelo en Avianca y estancia en hotel Tenquendama (calificación 8.5). Valor: 2'000.000 COP por persona"
    ],
    "Medellín": [
        "Plan 1: 5 días y 4 noches, con vuelo en Latam y estancia en hotel Armonica (calificación 8.0). Valor: 2'100.000 COP por pareja",
        "Plan 2: 6 días y 5 noches, con vuelo en Avianca y estancia en hotel Tres cuartos (calificación 8.0). Valor: 1'545.000 COP por persona",
        "Plan 3: 7 días y 6 noches, con vuelo en Latam y estancia en hotel Arae (calificación 8.0). Valor: 1'600.000 COP por persona",
        "Plan 4: 8 días y 7 noches, con vuelo en Avianca y estancia en hotel Altair (calificación 8.5). Valor: 1'790.000 COP por persona"
    ],
    "Barranquilla": [
        "Plan 1: 5 días y 4 noches, con vuelo en Avianca y estancia en hotel La Marimonda (calificación 8.0). Valor: 4'670.000 COP por familia de 5 integrantes",
        "Plan 2: 6 días y 5 noches, con vuelo en Latam y estancia en hotel Pacific Ocean (calificación 8.0). Valor: 1'345.000 COP por persona",
        "Plan 3: 7 días y 6 noches, con vuelo en Avianca y estancia en hotel Los Guayacan (calificación 8.0). Valor: 1'950.000 COP por persona",
        "Plan 4: 8 días y 7 noches, con vuelo en Latam y estancia en hotel Porvenir (calificación 8.5). Valor: 2'500.000 COP por persona"
    ]
}

def establecer_estilo():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='white', background='#0078D7', borderwidth=1)
    style.map('TButton',
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    style.configure('TLabel', font=('Helvetica', 12), background='#333333', foreground='white')
    style.configure('TEntry', foreground='black', fieldbackground='white', borderwidth=1)

def mostrar_planes_gui(destino):
    ventana_planes = tk.Toplevel()
    ventana_planes.title(f"Planes Disponibles para {destino}")
    ventana_planes.geometry("600x400")
    ventana_planes.configure(bg='#333333')

    if destino in planes_turisticos:
        for plan in planes_turisticos[destino]:
            ttk.Label(ventana_planes, text=plan, background='#333333', foreground='white', wraplength=500).pack(pady=5)
    else:
        ttk.Label(ventana_planes, text="No hay planes disponibles para este destino.", background='#333333', foreground='white').pack(pady=20)

def reservar_plan_gui(gestion_clientes):
    ventana_reserva = tk.Toplevel()
    ventana_reserva.title("Reservar Paquete Turístico")
    ventana_reserva.geometry("600x400")
    ventana_reserva.configure(bg='#333333')

    ttk.Label(ventana_reserva, text="Ingrese su Identificación:", background='#333333', foreground='white').pack(pady=5)
    entrada_identificacion = ttk.Entry(ventana_reserva)
    entrada_identificacion.pack(pady=5)

    ttk.Label(ventana_reserva, text="Ingrese su Destino:", background='#333333', foreground='white').pack(pady=5)
    entrada_destino = ttk.Entry(ventana_reserva)
    entrada_destino.pack(pady=5)

    ttk.Label(ventana_reserva, text="Seleccione el Plan (Plan 1, Plan 2, etc.):", background='#333333', foreground='white').pack(pady=5)
    entrada_plan = ttk.Entry(ventana_reserva)
    entrada_plan.pack(pady=5)

    def reservar():
        identificacion = entrada_identificacion.get()
        destino = entrada_destino.get()
        plan_elegido = entrada_plan.get()

        cliente = gestion_clientes.buscar_cliente(identificacion=identificacion)
        
        if not cliente:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado. Debe registrarse en Gestión Clientes.")
            return
        
        if destino not in planes_turisticos:
            messagebox.showwarning("Destino No Disponible", "No hay planes turísticos disponibles para este destino.")
            return
        
        plan_disponible = None
        for plan in planes_turisticos[destino]:
            if plan.startswith(plan_elegido):
                plan_disponible = plan
                break

        if not plan_disponible:
            messagebox.showwarning("Plan No Disponible", "El plan seleccionado no está disponible. Intente nuevamente.")
            return

        cliente.historial_reservas.append({"tipo": "paquete turístico", "detalle": plan_disponible})
        messagebox.showinfo("Reserva Exitosa", f"Reserva confirmada para {plan_elegido} en {destino}.")

        ventana_reserva.destroy()

    ttk.Button(ventana_reserva, text="Confirmar Reserva", command=reservar).pack(pady=20)

def iniciar_paquetes(gestion_clientes):
    root = tk.Tk()
    root.title("Gestión de Paquetes Turísticos")
    root.geometry("600x500")
    root.configure(bg='#333333')
    establecer_estilo()

    ttk.Label(root, text="Seleccione su destino:", background='#333333', foreground='white').pack(pady=20)
    entrada_destino = ttk.Entry(root)
    entrada_destino.pack(pady=5)

    ttk.Button(root, text="Mostrar Planes Disponibles", command=lambda: mostrar_planes_gui(entrada_destino.get())).pack(pady=20, padx=20, fill=tk.X)
    ttk.Button(root, text="Reservar Paquete Turístico", command=lambda: reservar_plan_gui(gestion_clientes)).pack(pady=20, padx=20, fill=tk.X)

    root.mainloop()