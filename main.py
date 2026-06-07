from memoria import Memoria


procesos = [
    ("A", 200),
    ("B", 300),
    ("C", 100),
    ("D", 150),
    ("E", 180)
]

# =====================
# FIRST FIT
# =====================

first = Memoria(1000)

for proceso, tamaño in procesos:
    first.first_fit(proceso, tamaño)

# =====================
# BEST FIT
# =====================

best = Memoria(1000)

for proceso, tamaño in procesos:
    best.best_fit(proceso, tamaño)

# =====================
# WORST FIT
# =====================

worst = Memoria(1000)

for proceso, tamaño in procesos:
    worst.worst_fit(proceso, tamaño)

# =====================
# MOSTRAR ESTADOS
# =====================

print("\n===== FIRST FIT =====")
first.mostrar_memoria()

print("\n===== BEST FIT =====")
best.mostrar_memoria()

print("\n===== WORST FIT =====")
worst.mostrar_memoria()

# =====================
# COMPARACIÓN
# =====================

print("\n===== COMPARACIÓN =====")

print(
    "First Fit:",
    first.fragmentacion_externa(),
    "MB de fragmentación externa"
)

print(
    "Best Fit:",
    best.fragmentacion_externa(),
    "MB de fragmentación externa"
)

print(
    "Worst Fit:",
    worst.fragmentacion_externa(),
    "MB de fragmentación externa"
)

# =====================
# MEJOR ALGORITMO
# =====================

algoritmos = {
    "First Fit": first.fragmentacion_externa(),
    "Best Fit": best.fragmentacion_externa(),
    "Worst Fit": worst.fragmentacion_externa()
}

menor_fragmentacion = min(algoritmos.values())

mejores = [
    nombre
    for nombre, fragmentacion in algoritmos.items()
    if fragmentacion == menor_fragmentacion
]

print("\nMejor algoritmo:", ", ".join(mejores))
print("Fragmentación externa:", menor_fragmentacion, "MB")

# =====================
# HISTORIALES
# =====================

print("\n===== HISTORIAL FIRST FIT =====")
first.mostrar_historial()

print("\n===== HISTORIAL BEST FIT =====")
best.mostrar_historial()

print("\n===== HISTORIAL WORST FIT =====")
worst.mostrar_historial()