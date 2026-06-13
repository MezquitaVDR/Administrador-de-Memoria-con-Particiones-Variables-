# Administrador de Memoria con Particiones Variables

Proyecto desarrollado en Python utilizando Tkinter para simular la administración dinámica de memoria mediante particiones variables y comparar los algoritmos de asignación más utilizados.

## Características

- Simulación de los algoritmos:
  - First Fit
  - Best Fit
  - Worst Fit

- Asignación de procesos a memoria.
- Liberación de procesos.
- Compactación de memoria.
- Reinicio completo de la simulación.
- Comparación automática de los tres algoritmos.
- Cálculo de fragmentación externa.
- Identificación del algoritmo más eficiente.
- Interfaz gráfica desarrollada con Tkinter.

## Estructura del Proyecto

```text
AdministradorMemoria/
│
├── main.py
├── interfaz.py
├── memoria.py
└── bloque.py
```

## Descripción de los Archivos

### `main.py`
Archivo principal encargado de iniciar la aplicación.

### `interfaz.py`
Contiene la interfaz gráfica y la interacción con el usuario.

### `memoria.py`
Implementa la lógica de administración de memoria y los algoritmos:

- First Fit
- Best Fit
- Worst Fit

Además, incluye:

- Liberación de procesos.
- Fusión de bloques libres.
- Compactación.
- Fragmentación externa.

### `bloque.py`
Define la estructura de cada bloque de memoria.

## Requisitos

- Python 3.10 o superior.
- Tkinter (incluido por defecto con Python).

## Ejecución

Desde la terminal, ejecutar:

```bash
python main.py
```

## Funcionamiento

1. Ingresar el nombre del proceso.
2. Ingresar el tamaño del proceso en MB.
3. Presionar **Agregar Proceso**.
4. Los algoritmos First Fit, Best Fit y Worst Fit se ejecutan simultáneamente.
5. Se muestra el estado de memoria para cada algoritmo.
6. Se calcula automáticamente la fragmentación externa.
7. El sistema determina cuál algoritmo produjo la menor fragmentación.

También es posible:

- Liberar procesos.
- Compactar la memoria.
- Reiniciar completamente la simulación.

## Ejemplo

### Entrada

```text
Proceso: A
Tamaño: 200 MB

Proceso: B
Tamaño: 300 MB

Proceso: C
Tamaño: 100 MB
```

### Resultado

El sistema mostrará:

- Estado de memoria para First Fit.
- Estado de memoria para Best Fit.
- Estado de memoria para Worst Fit.
- Tabla comparativa de fragmentación externa.
- Mejor algoritmo para la secuencia de procesos ingresada.

## Tecnologías Utilizadas

- Python
- Tkinter

## Autor

Proyecto desarrollado para la asignatura Manejo de Estructuras de Datos.

Universidad de El Salvador

Facultad Multidisciplinaria de Occidente

Ingeniería en Desarrollo de Software
