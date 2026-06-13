import tkinter as tk
from tkinter import ttk, messagebox

from memoria import Memoria


class Interfaz:

    def __init__(self):

        self.memoria = Memoria(1000)

        self.ventana = tk.Tk()
        self.ventana.title(
            "Administrador de Memoria con Particiones Variables"
        )

        self.ventana.geometry("1100x700")

        # ===== PROCESO =====

        tk.Label(
            self.ventana,
            text="Proceso"
        ).pack()

        self.entry_proceso = tk.Entry(
            self.ventana
        )

        self.entry_proceso.pack()

        # ===== TAMAÑO =====

        tk.Label(
            self.ventana,
            text="Tamaño (MB)"
        ).pack()

        self.entry_tamaño = tk.Entry(
            self.ventana
        )

        self.entry_tamaño.pack()

        # ===== ALGORITMO =====

        tk.Label(
            self.ventana,
            text="Algoritmo"
        ).pack()

        self.combo = ttk.Combobox(
            self.ventana,
            values=[
                "First Fit",
                "Best Fit",
                "Worst Fit"
            ]
        )

        self.combo.current(0)

        self.combo.pack()

        # ===== BOTONES =====

        tk.Button(
            self.ventana,
            text="Asignar",
            command=self.asignar
        ).pack()

        tk.Button(
            self.ventana,
            text="Liberar",
            command=self.liberar
        ).pack()

        tk.Button(
            self.ventana,
            text="Compactar",
            command=self.compactar
        ).pack()

        # ===== TABLA MEMORIA =====

        tk.Label(
            self.ventana,
            text="Estado de Memoria"
        ).pack()

        self.tabla_memoria = ttk.Treeview(
            self.ventana,
            columns=(
                "Inicio",
                "Tamaño",
                "Estado"
            ),
            show="headings",
            height=10
        )

        self.tabla_memoria.heading(
            "Inicio",
            text="Inicio"
        )

        self.tabla_memoria.heading(
            "Tamaño",
            text="Tamaño"
        )

        self.tabla_memoria.heading(
            "Estado",
            text="Estado"
        )

        self.tabla_memoria.pack(
            fill="x"
        )

        # ===== TABLA HISTORIAL =====

        tk.Label(
            self.ventana,
            text="Historial"
        ).pack()

        self.tabla_historial = ttk.Treeview(
            self.ventana,
            columns=(
                "Operación",
                "Proceso",
                "Tamaño"
            ),
            show="headings",
            height=10
        )

        self.tabla_historial.heading(
            "Operación",
            text="Operación"
        )

        self.tabla_historial.heading(
            "Proceso",
            text="Proceso"
        )

        self.tabla_historial.heading(
            "Tamaño",
            text="Tamaño"
        )

        self.tabla_historial.pack(
            fill="x"
        )

        self.label_fragmentacion = tk.Label(
            self.ventana,
            text=""
        )

        self.label_fragmentacion.pack()

        self.actualizar_tablas()

        self.ventana.mainloop()

    def asignar(self):

        proceso = self.entry_proceso.get()
        tamaño = int(
            self.entry_tamaño.get()
        )

        algoritmo = self.combo.get()

        if algoritmo == "First Fit":

            exito = self.memoria.first_fit(
                proceso,
                tamaño
            )

        elif algoritmo == "Best Fit":

            exito = self.memoria.best_fit(
                proceso,
                tamaño
            )

        else:

            exito = self.memoria.worst_fit(
                proceso,
                tamaño
            )

        if not exito:

            messagebox.showerror(
                "Error",
                "No hay espacio suficiente"
            )

        self.actualizar_tablas()

    def liberar(self):

        proceso = self.entry_proceso.get()

        self.memoria.liberar(
            proceso
        )

        self.actualizar_tablas()

    def compactar(self):

        self.memoria.compactar()

        self.actualizar_tablas()

    def actualizar_tablas(self):

        for fila in self.tabla_memoria.get_children():
            self.tabla_memoria.delete(
                fila
            )

        for fila in self.tabla_historial.get_children():
            self.tabla_historial.delete(
                fila
            )

        # MEMORIA

        for bloque in self.memoria.bloques:

            estado = (
                "Libre"
                if bloque.libre
                else bloque.proceso
            )

            self.tabla_memoria.insert(
                "",
                tk.END,
                values=(
                    bloque.inicio,
                    bloque.tamaño,
                    estado
                )
            )

        # HISTORIAL

        for operacion in self.memoria.historial:

            self.tabla_historial.insert(
                "",
                tk.END,
                values=(
                    operacion["operacion"],
                    operacion["proceso"],
                    operacion["tamaño"]
                )
            )

        self.label_fragmentacion.config(
            text=
            f"Fragmentación externa: "
            f"{self.memoria.fragmentacion_externa()} MB"
        )


Interfaz()