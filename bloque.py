class Bloque:

    def __init__(self, inicio, tamaño, libre=True, proceso=None):
        self.inicio = inicio
        self.tamaño = tamaño
        self.libre = libre
        self.proceso = proceso

    def __str__(self):

        estado = (
            "Libre"
            if self.libre
            else f"Ocupado por {self.proceso}"
        )

        return (
            f"Inicio: {self.inicio} | "
            f"Tamaño: {self.tamaño} MB | "
            f"{estado}"
        )