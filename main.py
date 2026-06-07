from memoria import Memoria

memoria = Memoria(1000)

print("\nFIRST FIT")

memoria.first_fit("A", 200)
memoria.first_fit("B", 300)
memoria.first_fit("C", 100)

memoria.mostrar_memoria()

print("\nLiberando B")

memoria.liberar("B")

memoria.mostrar_memoria()

print("\nAsignando D (150 MB)")

memoria.first_fit("D", 150)

memoria.mostrar_memoria()

print("\nLiberando C")

memoria.liberar("C")

memoria.mostrar_memoria()

print("\nCompactando memoria")

memoria.compactar()

memoria.mostrar_memoria()

memoria.mostrar_historial()