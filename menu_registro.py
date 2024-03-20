from registro import Registro

class MenuRegistro:
    SI_NO = (1,0)
    def __init__(self) -> None:
        self.registro_actual = None

    def menu(self):
        try:
            opcion = int(input("""\nBienvenido, Que desea hacer?

        0 : Salir
        1 : Crear Registro
        2 : Mostrar Registro
        3 : Importar Registro
        4 : Exportar Registro
        5 : Eliminar Registro
        6 : Entrar en Mensajeria
                         
        Digite su opcion: """))
        
        except ValueError:
            opcion = None
        return opcion


    def crearRegistro(self):
        if self.registro_actual:
            try: 
                decision = int(input("""Esta seguro que desea sobreescribir el Registro?
        0 : NO,  1 : SI
        Digite su decision: """))
                if decision not in MenuRegistro.SI_NO:
                    print("Opcion invalida")
                    return
            except ValueError:
                    print("Opcion invalida")
                    return
            if not decision:
                    return
        try:
            capacidad = int(input("Digite la capacidad del Registro: "))
        except ValueError:
            print("Capacidad invalida, Digite un entero")
            return
        self.registro_actual = Registro(capacidad)
        return True

    def mostrarRegistro(self):
        if not self.registro_actual:
            return False
        self.registro_actual.mostrarRegistro()
        return True

    def importarRegistro(self, nombre_txt):
        cargar = Registro.cargarRegistro(nombre_txt)
        if not cargar:
            return False
        self.registro_actual = cargar
        return True
    
    def exportarRegistro(self, nombre_txt):
        if not self.registro_actual:
                return False

        self.registro_actual.exportarRegistro(nombre_txt)
        return True

    def eliminarRegistro(self):
        if not self.registro_actual:
            return False
        try: 
            decision = int(input("""Esta seguro que desea eliminar el Registro?
        0 : NO,  1 : SI
        Digite su decision: """))
            if decision not in MenuRegistro.SI_NO:
                        print("Opcion invalida")
                        return
        except ValueError:
                print("Opcion invalida")
                return
        if decision:
            self.registro_actual = None
            return True
        
    def getRegistro(self):
         return self.registro_actual