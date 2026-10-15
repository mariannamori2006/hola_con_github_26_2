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