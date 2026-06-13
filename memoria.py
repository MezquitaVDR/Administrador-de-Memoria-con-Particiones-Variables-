from bloque import Bloque


class Memoria:

    def __init__(self, tamaño_total):

        self.tamaño_total = tamaño_total

        self.bloques = [
            Bloque(
                0,
                tamaño_total
            )
        ]

        self.historial = []

    # =====================
    # FIRST FIT
    # =====================

    def first_fit(self, proceso, tamaño):

        for bloque in self.bloques:

            if bloque.libre and bloque.tamaño >= tamaño:

                self._asignar_bloque(
                    bloque,
                    proceso,
                    tamaño
                )

                return True

        return False

    # =====================
    # BEST FIT
    # =====================

    def best_fit(self, proceso, tamaño):

        candidatos = [
            bloque
            for bloque in self.bloques
            if bloque.libre and bloque.tamaño >= tamaño
        ]

        if not candidatos:
            return False

        mejor = min(
            candidatos,
            key=lambda x: x.tamaño
        )

        self._asignar_bloque(
            mejor,
            proceso,
            tamaño
        )

        return True

    # =====================
    # WORST FIT
    # =====================

    def worst_fit(self, proceso, tamaño):

        candidatos = [
            bloque
            for bloque in self.bloques
            if bloque.libre and bloque.tamaño >= tamaño
        ]

        if not candidatos:
            return False

        peor = max(
            candidatos,
            key=lambda x: x.tamaño
        )

        self._asignar_bloque(
            peor,
            proceso,
            tamaño
        )

        return True

    # =====================
    # ASIGNAR BLOQUE
    # =====================

    def _asignar_bloque(
            self,
            bloque,
            proceso,
            tamaño):

        sobrante = bloque.tamaño - tamaño

        indice = self.bloques.index(bloque)

        bloque.libre = False
        bloque.proceso = proceso
        bloque.tamaño = tamaño

        if sobrante > 0:

            nuevo_bloque = Bloque(
                bloque.inicio + tamaño,
                sobrante
            )

            self.bloques.insert(
                indice + 1,
                nuevo_bloque
            )

        self.historial.append(
            {
                "operacion": "Asignar",
                "proceso": proceso,
                "tamaño": tamaño
            }
        )

    # =====================
    # LIBERAR
    # =====================

    def liberar(self, proceso):

        for bloque in self.bloques:

            if bloque.proceso == proceso:

                tamaño_liberado = bloque.tamaño

                bloque.libre = True
                bloque.proceso = None

                self.fusionar_bloques()

                self.historial.append(
                    {
                        "operacion": "Liberar",
                        "proceso": proceso,
                        "tamaño": tamaño_liberado
                    }
                )

                return True

        return False

    # =====================
    # FUSIONAR BLOQUES
    # =====================

    def fusionar_bloques(self):

        i = 0

        while i < len(self.bloques) - 1:

            actual = self.bloques[i]
            siguiente = self.bloques[i + 1]

            if actual.libre and siguiente.libre:

                actual.tamaño += siguiente.tamaño

                self.bloques.pop(
                    i + 1
                )

            else:

                i += 1

    # =====================
    # COMPACTAR
    # =====================

    def compactar(self):

        nuevos_bloques = []

        posicion_actual = 0

        espacio_libre = 0

        for bloque in self.bloques:

            if bloque.libre:

                espacio_libre += bloque.tamaño

            else:

                bloque.inicio = posicion_actual

                nuevos_bloques.append(
                    bloque
                )

                posicion_actual += bloque.tamaño

        if espacio_libre > 0:

            nuevos_bloques.append(
                Bloque(
                    posicion_actual,
                    espacio_libre
                )
            )

        self.bloques = nuevos_bloques

        self.historial.append(
            {
                "operacion": "Compactar",
                "proceso": "-",
                "tamaño": "-"
            }
        )

    # =====================
    # FRAGMENTACIÓN EXTERNA
    # =====================

    def fragmentacion_externa(self):

        total_libre = 0

        bloque_mayor = 0

        for bloque in self.bloques:

            if bloque.libre:

                total_libre += bloque.tamaño

                bloque_mayor = max(
                    bloque_mayor,
                    bloque.tamaño
                )

        return total_libre - bloque_mayor

    # =====================
    # FRAGMENTACIÓN INTERNA
    # =====================

    def fragmentacion_interna(self):

        return 0