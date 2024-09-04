import tkinter as tk
from tkinter import ttk
from Gestion_Clientes import GestionClientes, iniciar_aplicacion as iniciar_gestion
from Reserva_Vuelos_Hoteles import iniciar_reservas
from Gestion_PaquetesTuristicos import iniciar_paquetes

def establecer_estilo():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='white', background='#0078D7', borderwidth=1)
    style.map('TButton',
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    style.configure('TLabel', font=('Helvetica', 12), background='#333333', foreground='white')
    style.configure('TEntry', foreground='black', fieldbackground='white', borderwidth=1)

def iniciar_gestion_clientes(gestion_clientes):
    iniciar_gestion(gestion_clientes)

def iniciar_reservas_vuelos_hoteles(gestion_clientes):
    iniciar_reservas(gestion_clientes)

def iniciar_gestion_paquetes_turisticos(gestion_clientes):
    iniciar_paquetes(gestion_clientes)

def iniciar_menu_principal():
    gestion_clientes = GestionClientes()
    
    root = tk.Tk()
    root.title("Menú Principal")
    root.geometry("400x250")
    root.configure(bg='#333333')
    establecer_estilo()

    ttk.Label(root, text="Bienvenido a la Agencia de Viajes", background='#333333', foreground='white', font=('Helvetica', 16, 'bold')).pack(pady=20)

    ttk.Button(root, text="Gestión de Clientes", command=lambda: iniciar_gestion_clientes(gestion_clientes)).pack(pady=10, padx=20, fill=tk.X)
    ttk.Button(root, text="Reservas de Vuelos y Hoteles", command=lambda: iniciar_reservas_vuelos_hoteles(gestion_clientes)).pack(pady=10, padx=20, fill=tk.X)
    ttk.Button(root, text="Paquetes Turísticos", command=lambda: iniciar_gestion_paquetes_turisticos(gestion_clientes)).pack(pady=10, padx=20, fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    iniciar_menu_principal()