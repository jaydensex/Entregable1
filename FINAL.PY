import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


#Verificacion de vectores
def validar_vector(vector):
    if vector is None or len(vector) == 0:
        raise ValueError("El vector no puede estar vacío.")
    if not isinstance(vector, np.ndarray):
        raise ValueError("Debe ser un np.array.")
    return vector


def verificar_propiedad(propiedad, a, b=None, c=None, escalar=None):
    a = validar_vector(a)


    if propiedad == "conmutativa":
        b = validar_vector(b)
        return a + b, b + a, np.array_equal(a + b, b + a)

    elif propiedad == "asociativa":
        b = validar_vector(b)
        c = validar_vector(c)
        return (a + b) + c, a + (b + c), np.array_equal((a + b) + c, a + (b + c))

    elif propiedad == "distributiva":
        b = validar_vector(b)
        if escalar is None:
            raise ValueError("Falta el escalar")
        return escalar * (a + b), escalar * a + escalar * b, np.array_equal(escalar * (a + b), escalar * a + escalar * b)

    elif propiedad == "identidad":
        cero = np.zeros_like(a)
        return a + cero, a, np.array_equal(a + cero, a)

    elif propiedad == "inverso":
        return a + (-a), np.zeros_like(a), np.array_equal(a + (-a), np.zeros_like(a))

    else:
        raise ValueError("Propiedad no válida")


#GRAFICOS
def ejecutar():
    prop = propiedad_var.get()
    try:
        a = np.array(eval(entry_a.get()))
        b = np.array(eval(entry_b.get())) if entry_b.get() else None
        c = np.array(eval(entry_c.get())) if entry_c.get() else None
        k = float(entry_k.get()) if entry_k.get() else None

        r1, r2, cumple = verificar_propiedad(prop, a, b, c, k)
        resultado.set(f"Lado 1: {r1}\nLado 2: {r2}\nCumple: {'Sí' if cumple else 'No'}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Verificación de propiedades vectoriales")

propiedad_var = tk.StringVar()
resultado = tk.StringVar()

frame = tk.Frame(root, padx=30, pady=30)
frame.pack()

options = ["conmutativa", "asociativa", "distributiva", "identidad", "inverso"]
ttk.Label(frame, text="Propiedad:").grid(row=0, column=0)
ttk.Combobox(frame, textvariable=propiedad_var, values=options).grid(row=0, column=1)

ttk.Label(frame, text="Vector A:").grid(row=1, column=0)
entry_a = ttk.Entry(frame)
entry_a.grid(row=1, column=1)

ttk.Label(frame, text="Vector B:").grid(row=2, column=0)
entry_b = ttk.Entry(frame)
entry_b.grid(row=2, column=1)

ttk.Label(frame, text="Vector C:").grid(row=3, column=0)
entry_c = ttk.Entry(frame)
entry_c.grid(row=3, column=1)

ttk.Label(frame, text="Escalar:").grid(row=4, column=0)
entry_k = ttk.Entry(frame)
entry_k.grid(row=4, column=1)

ttk.Button(frame, text="Verificar", command=ejecutar).grid(row=5, columnspan=2)

ttk.Label(frame, textvariable=resultado, wraplength=300).grid(row=6, columnspan=2)

root.mainloop()