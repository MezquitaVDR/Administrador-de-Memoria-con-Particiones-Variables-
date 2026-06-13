import tkinter as tk
from tkinter import ttk, messagebox

from memoria import Memoria


class Interfaz:

    def __init__(self):

        # Tres memorias independientes
        self.first = Memoria(1000)
        self.best = Memoria(1000)
        self.worst = Memoria(1000)

        self.ventana = tk.Tk()
        self.ventana.title(
            "Administrador de Memoria con Particiones Variables"
        )

        self.ventana.geometry("1400x800")

        # =====================
        # PROCESO
        # =====================

        tk.Label(
            self.ventana,
            text="Proceso"
        ).pack()

        self.entry_proceso = tk.Entry(
            self.ventana
        )

        self.entry_proceso.pack()

        # =====================
        # TAMAÑO
        # =====================

        tk.Label(
            self.ventana,
            text="Tamaño (MB)"
        ).pack()

        self.entry_tamaño = tk.Entry(
            self.ventana
        )

        self.entry_tamaño.pack()

        # =====================
        # BOTONES
        # =====================

        tk.Button(
            self.ventana,
            text="Agregar proceso",
            command=self.asignar
        ).pack()

        tk.Button(
            self.ventana,
            text="Liberar proceso",
            command=self.liberar
        ).pack()

        tk.Button(
            self.ventana,
            text="Compactar",
            command=self.compactar
        ).pack()

        # =====================
        # FIRST FIT
        # =====================

        tk.Label(
            self.ventana,
            text="FIRST FIT"
        ).pack()

        self.tabla_first = self.crear_tabla()

        # =====================
        # BEST FIT
        # =====================

        tk.Label(
            self.ventana,
            text="BEST FIT"
        ).pack()

        self.tabla_best = self.crear_tabla()

        # =====================
        # WORST FIT
        # =====================

        tk.Label(
            self.ventana,
            text="WORST FIT"
        ).pack()

        self.tabla_worst = self.crear_tabla()

        # =====================
        # COMPARACIÓN
        # =====================

        tk.Label(
            self.ventana,
            text="Comparación"
        ).pack()

        self.tabla_comparacion = ttk.Treeview(
            self.ventana,
            columns=(
                "Algoritmo",
                "Fragmentación"
            ),
            show="headings",
            height=3
        )

        self.tabla_comparacion.heading(
            "Algoritmo",
            text="Algoritmo"
        )

        self.tabla_comparacion.heading(
            "Fragmentación",
            text="Fragmentación externa"
        )

        self.tabla_comparacion.pack(
            fill="x"
        )

        # =====================
        # MEJOR ALGORITMO
        # =====================

        self.label_mejor = tk.Label(
            self.ventana,
            text="",
            fg="blue",
            font=(
                "Arial",
                12,
                "bold"
            )
        )

        self.label_mejor.pack(
            pady=10
        )

        self.actualizar_tablas()

        self.ventana.mainloop()

    # =====================================

    def crear_tabla(self):

        tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "Inicio",
                "Tamaño",
                "Estado"
            ),
            show="headings",
            height=5
        )

        tabla.heading(
            "Inicio",
            text="Inicio"
        )

        tabla.heading(
            "Tamaño",
            text="Tamaño"
        )

        tabla.heading(
            "Estado",
            text="Estado"
        )

        tabla.pack(
            fill="x"
        )

        return tabla

    # =====================================

    def asignar(self):

        proceso = self.entry_proceso.get()

        tamaño = int(
            self.entry_tamaño.get()
        )

        self.first.first_fit(
            proceso,
            tamaño
        )

        self.best.best_fit(
            proceso,
            tamaño
        )

        self.worst.worst_fit(
            proceso,
            tamaño
        )

        self.actualizar_tablas()

    # =====================================

    def liberar(self):

        proceso = self.entry_proceso.get()

        self.first.liberar(
            proceso
        )

        self.best.liberar(
            proceso
        )

        self.worst.liberar(
            proceso
        )

        self.actualizar_tablas()

    # =====================================

    def compactar(self):

        self.first.compactar()

        self.best.compactar()

        self.worst.compactar()

        self.actualizar_tablas()

    # =====================================

    def llenar_tabla(
            self,
            tabla,
            memoria):

        for fila in tabla.get_children():

            tabla.delete(
                fila
            )

        for bloque in memoria.bloques:

            estado = (
                "Libre"
                if bloque.libre
                else bloque.proceso
            )

            tabla.insert(
                "",
                tk.END,
                values=(
                    bloque.inicio,
                    bloque.tamaño,
                    estado
                )
            )

    # =====================================

    def actualizar_tablas(self):

        self.llenar_tabla(
            self.tabla_first,
            self.first
        )

        self.llenar_tabla(
            self.tabla_best,
            self.best
        )

        self.llenar_tabla(
            self.tabla_worst,
            self.worst
        )

        # =====================
        # COMPARACIÓN
        # =====================

        for fila in self.tabla_comparacion.get_children():

            self.tabla_comparacion.delete(
                fila
            )

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=(
                "First Fit",
                self.first.fragmentacion_externa()
            )
        )

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=(
                "Best Fit",
                self.best.fragmentacion_externa()
            )
        )

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=(
                "Worst Fit",
                self.worst.fragmentacion_externa()
            )
        )

        algoritmos = {

            "First Fit":
                self.first.fragmentacion_externa(),

            "Best Fit":
                self.best.fragmentacion_externa(),

            "Worst Fit":
                self.worst.fragmentacion_externa()
        }

        mejor = min(
            algoritmos,
            key=algoritmos.get
        )

        self.label_mejor.config(
            text=
            f"🏆 Mejor algoritmo: {mejor}"
        )


Interfaz()