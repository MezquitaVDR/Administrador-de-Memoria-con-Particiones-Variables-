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

    # =================================

    def first_fit(
            self,
            proceso,
            tamaño):

        for bloque in self.bloques:

            if bloque.libre and bloque.tamaño >= tamaño:

                self._asignar_bloque(
                    bloque,
                    proceso,
                    tamaño
                )

                return True

        return False

    # =================================

    def best_fit(
            self,
            proceso,
            tamaño):

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

    # =================================

    def worst_fit(
            self,
            proceso,
            tamaño):

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

    # =================================

    def _asignar_bloque(
            self,
            bloque,
            proceso,
            tamaño):

        sobrante = bloque.tamaño - tamaño

        indice = self.bloques.index(
            bloque
        )

        bloque.libre = False
        bloque.proceso = proceso
        bloque.tamaño = tamaño

        if sobrante > 0:

            self.bloques.insert(
                indice + 1,
                Bloque(
                    bloque.inicio + tamaño,
                    sobrante
                )
            )

        self.historial.append(
            {
                "operacion": "Asignar",
                "proceso": proceso,
                "tamaño": tamaño
            }
        )

    # =================================

    def liberar(
            self,
            proceso):

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

    # =================================

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

    # =================================

    def compactar(self):

        nuevos = []

        posicion = 0

        libre = 0

        for bloque in self.bloques:

            if bloque.libre:

                libre += bloque.tamaño

            else:

                bloque.inicio = posicion

                nuevos.append(
                    bloque
                )

                posicion += bloque.tamaño

        if libre > 0:

            nuevos.append(
                Bloque(
                    posicion,
                    libre
                )
            )

        self.bloques = nuevos

        self.historial.append(
            {
                "operacion": "Compactar",
                "proceso": "-",
                "tamaño": "-"
            }
        )

    # =================================

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