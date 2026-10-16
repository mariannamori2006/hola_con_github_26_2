from tkinter import ttk
import tkinter as tk

class Login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        
        self.ven = ventana
        self.ven.geometry("350x450+800+150") #tamaño de la ventana
        self.ven.title("Sistema Login")
        self.ven.config(bg="#eebeee")
        self.ven.resizable(False, False) #no permite cambiar el tamaño de la ventana
        self.ven.wm_attributes("-alpha",0.89) #transparencia de la ventana
        self.ven.iconbitmap("iconos/icono.ico") #icono de la ventana
        
        #Quitamos la barra de menu
        self.ven.overrideredirect(True)
        
        def Salir():
            self.ven.destroy()
        
        #Ponemos un boton de salir
        self.btnSalir = tk.Button(self.ven, text="X", width=6, height=2, command=Salir)
        self.btnSalir.place(x=290,y=5)
        self.btnSalir.config(bg="#e5f799")
        
        #Variables
        self.user = tk.StringVar()
        self.pas = tk.StringVar()
        
        #Imagenes
        self.img = tk.PhotoImage(file="image/logo.png")
        
        #Etiquetas
        #Etiqueta para ña imagen de logo
        self.lblLogo = tk.Label(self.ven,image=self.img)
        self.lblLogo.place(x=123,y=40)
        self.lblLogo.config(bg="#eebeee")
        
        self.lblTitulo = tk.Label(self.ven,text="ACCESO",font=("Arial", 20, "bold"))
        self.lblTitulo.place(x=112,y=140)
        self.lblTitulo.config(bg="#eebeee")
        
        self.lblUser = tk.Label(self.ven,text="Usuario",font=("Arial", 17, "bold"))
        self.lblUser.place(x=40,y=200)
        self.lblUser.config(bg="#eebeee")
        self.txtUser = tk.Entry(self.ven,textvariable=self.user,font=("Arial",17,"bold"))
        self.txtUser.place(x=40,y=240)
        self.txtUser.config(bg="#ffffff")
        
        self.lblPass = tk.Label(self.ven,text="Contraseña",font=("Arial", 17, "bold"))
        self.lblPass.place(x=40,y=280)
        self.lblPass.config(bg="#eebeee")
        self.txtPass = tk.Entry(self.ven,textvariable=self.pas,font=("Arial",17,"bold"))
        self.txtPass.place(x=40,y=320)
        self.txtPass.config(bg="#ffffff")
        
        self.btnIngresar = tk.Button(self.ven,text="Ingresar",font=("Arial",19,"bold"),width="17")
        self.btnIngresar.place(x=40,y=370)
        self.btnIngresar.config(bg="#e5f799")