def agregar_compra(compras, total_gastado):
    compra = float(input("Ingrese el monto de la compra: $"))
    compras.append(compra)
    total_gastado += compra
    print("La compra se ha agregado correctamente.")
    main()

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i in range(len(compras)):
            print(f"Compra {i + 1}: ${compras[i]:.f}")
            main()


def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.f}")
    main()

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

main()
