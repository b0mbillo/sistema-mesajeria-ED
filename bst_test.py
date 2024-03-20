from estructuras_datos import BinarySearchTree

arbol = BinarySearchTree()
while True:
    print("""        0 : Salir
        1 : Insertar objeto
        2 : Eliminar objeto
        3 : Buscar objeto
        4 : Valor Maximo
        5 : Valor Minimo
        6 : Mostrar Arbol
        7 : Inorder """)
    opcion = input("Que desea hacer: ")
    print(" ")
    match opcion:
        case "1":
            nombre = input("Nombre: ")
            documento = input("Documento: ")
            key = sum([int(i) for i in documento])
            print(key)
            nodo = nombre + " " +documento
            arbol.insert(nodo, key)
        case "2":
            if arbol.size == 0:
                print("Ingrese datos primero")
                continue
            key = int(input("Cual es la clave: "))
            nodo = arbol.removeKey(key)
            if not nodo:
                print("No se encontraron datos con esa clave")
            else:
                print("Se elimino:",nodo.getData().getData())
        case "3":
            if arbol.size == 0:
                print("Ingrese datos primero")
                continue
            key = int(input("Cual es la clave: "))
            nodo = arbol.find(key)
            if not nodo:
                print("No se encontraron datos con esa clave")
            else:
                print(nodo.getData().getData())
        case "4":
            if arbol.size == 0:
                print("Ingrese datos primero")
            else:
                maximo = arbol.getMax().getData()
                print(maximo)
        case "5":
            if arbol.size == 0:
                print("Ingrese datos primero")
            else:
                minimo = arbol.getMin().getData()
                print(minimo)
        case "6":
            if arbol.size == 0:
                print("Ingrese datos primero")
                continue
            arbol.mostrarArbol(arbol.getRoot())
        case "7":
            if arbol.size == 0:
                print("Ingrese datos primero")
                continue
            arbol.inorder(arbol.getRoot())
        case "0": break
        case "8":
            datos = ["Juan 10101013","Pablo 10001011","Maria 10101015","Diana 10111105","Ana 1010000","Mateo 10110005"]
            for dato in datos:
                nombre = dato.split()[0]
                documento = dato.split()[1]
                key = sum([int(i) for i in documento])
                nodo = nombre + " " +documento
                arbol.insert(nodo, key)
            print("Agregados")
        case _: pass
    print(" ")