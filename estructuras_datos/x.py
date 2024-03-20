class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def recorrido_por_niveles(raiz):
    if raiz is None:
        return
    
    cola = []
    cola.append(raiz)

    while cola:
        nodo_actual = cola.pop(0)
        print(nodo_actual.valor)

        if nodo_actual.izquierda:
            cola.append(nodo_actual.izquierda)
        if nodo_actual.derecha:
            cola.append(nodo_actual.derecha)

# Ejemplo de uso
# Creamos un árbol binario de búsqueda
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)
raiz.derecha.derecha = Nodo(18)

# Realizamos el recorrido por niveles e imprimimos los valores
recorrido_por_niveles(raiz)