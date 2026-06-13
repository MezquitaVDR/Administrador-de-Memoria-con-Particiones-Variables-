import tkinter as tk
from tkinter import ttk, messagebox

from memoria import Memoria


class Interfaz:

    def __init__(self):
        self.first = Memoria(1000)
        self.best = Memoria(1000)
        self.worst = Memoria(1000)

        self.ventana = tk.Tk()
        self.ventana.title("Administrador de Memoria con Particiones Variables")
        self.ventana.geometry("1200x750")

        tk.Label(self.ventana, text="Proceso").pack()
        self.entry_proceso = tk.Entry(self.ventana)
        self.entry_proceso.pack()

        tk.Label(self.ventana, text="Tamaño (MB)").pack()
        self.entry_tamaño = tk.Entry(self.ventana)
        self.entry_tamaño.pack()

        tk.Button(self.ventana, text="Agregar Proceso", command=self.asignar).pack(pady=3)
        tk.Button(self.ventana, text="Liberar Proceso", command=self.liberar).pack(pady=3)
        tk.Button(self.ventana, text="Compactar", command=self.compactar).pack(pady=3)
        tk.Button(
            self.ventana,
            text="Reiniciar Simulación",
            command=self.reiniciar,
            bg="red",
            fg="white"
        ).pack(pady=3)

        tk.Label(self.ventana, text="FIRST FIT").pack()
        self.tabla_first = self.crear_tabla()

        tk.Label(self.ventana, text="BEST FIT").pack()
        self.tabla_best = self.crear_tabla()

        tk.Label(self.ventana, text="WORST FIT").pack()
        self.tabla_worst = self.crear_tabla()

        tk.Label(self.ventana, text="Comparación de Algoritmos").pack()

        self.tabla_comparacion = ttk.Treeview(
            self.ventana,
            columns=("Algoritmo", "Fragmentación Externa"),
            show="headings",
            height=3
        )

        self.tabla_comparacion.heading("Algoritmo", text="Algoritmo")
        self.tabla_comparacion.heading("Fragmentación Externa", text="Fragmentación Externa")
        self.tabla_comparacion.pack(fill="x", padx=10, pady=5)

        self.label_mejor = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 12, "bold"),
            fg="blue"
        )
        self.label_mejor.pack(pady=10)

        self.actualizar_tablas()
        self.ventana.mainloop()

    def crear_tabla(self):
        tabla = ttk.Treeview(
            self.ventana,
            columns=("Inicio", "Tamaño", "Estado"),
            show="headings",
            height=5
        )

        tabla.heading("Inicio", text="Inicio")
        tabla.heading("Tamaño", text="Tamaño")
        tabla.heading("Estado", text="Estado")

        tabla.pack(fill="x", padx=10, pady=5)

        return tabla

    def asignar(self):
        proceso = self.entry_proceso.get().strip()

        if proceso == "":
            messagebox.showerror("Error", "Ingrese el nombre del proceso.")
            return

        try:
            tamaño = int(self.entry_tamaño.get())
        except ValueError:
            messagebox.showerror("Error", "El tamaño debe ser un número entero.")
            return

        if tamaño <= 0:
            messagebox.showerror("Error", "El tamaño debe ser mayor que cero.")
            return

        exito_first = self.first.first_fit(proceso, tamaño)
        exito_best = self.best.best_fit(proceso, tamaño)
        exito_worst = self.worst.worst_fit(proceso, tamaño)

        if not exito_first and not exito_best and not exito_worst:
            messagebox.showerror("Error", "No hay espacio suficiente para asignar el proceso.")

        self.actualizar_tablas()

    def liberar(self):
        proceso = self.entry_proceso.get().strip()

        if proceso == "":
            messagebox.showerror("Error", "Ingrese el nombre del proceso a liberar.")
            return

        self.first.liberar(proceso)
        self.best.liberar(proceso)
        self.worst.liberar(proceso)

        self.actualizar_tablas()

    def compactar(self):
        self.first.compactar()
        self.best.compactar()
        self.worst.compactar()

        self.actualizar_tablas()

    def reiniciar(self):
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Desea reiniciar toda la simulación?"
        )

        if respuesta:
            self.first = Memoria(1000)
            self.best = Memoria(1000)
            self.worst = Memoria(1000)

            self.entry_proceso.delete(0, tk.END)
            self.entry_tamaño.delete(0, tk.END)

            self.actualizar_tablas()

    def llenar_tabla(self, tabla, memoria):
        for fila in tabla.get_children():
            tabla.delete(fila)

        for bloque in memoria.bloques:
            estado = "Libre" if bloque.libre else bloque.proceso

            tabla.insert(
                "",
                tk.END,
                values=(
                    bloque.inicio,
                    f"{bloque.tamaño} MB",
                    estado
                )
            )

    def actualizar_tablas(self):
        self.llenar_tabla(self.tabla_first, self.first)
        self.llenar_tabla(self.tabla_best, self.best)
        self.llenar_tabla(self.tabla_worst, self.worst)

        for fila in self.tabla_comparacion.get_children():
            self.tabla_comparacion.delete(fila)

        frag_first = self.first.fragmentacion_externa()
        frag_best = self.best.fragmentacion_externa()
        frag_worst = self.worst.fragmentacion_externa()

        self.tabla_comparacion.insert("", tk.END, values=("First Fit", f"{frag_first} MB"))
        self.tabla_comparacion.insert("", tk.END, values=("Best Fit", f"{frag_best} MB"))
        self.tabla_comparacion.insert("", tk.END, values=("Worst Fit", f"{frag_worst} MB"))

        algoritmos = {
            "First Fit": frag_first,
            "Best Fit": frag_best,
            "Worst Fit": frag_worst
        }

        menor_fragmentacion = min(algoritmos.values())

        mejores = [
            nombre
            for nombre, fragmentacion in algoritmos.items()
            if fragmentacion == menor_fragmentacion
        ]

        self.label_mejor.config(
            text=f"Mejor algoritmo: {', '.join(mejores)} con {menor_fragmentacion} MB de fragmentación externa"
        )


Interfaz()