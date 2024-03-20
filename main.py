from menu_registro import MenuRegistro
from mensajeria import Mensajeria
from estructuras_datos.prueba import Prueba

def main():
    menu = MenuRegistro()
    while True:
        opcion = menu.menu()
        match opcion:
            case 1:
                if menu.crearRegistro():
                    print("Registro creado exitosamente")
            case 2:
                if not menu.mostrarRegistro(): 
                    print("No existe ningun registro, porfavor cree uno")
            case 3:
                nombre_txt = input("Digite el nombre del archivo de texto que contiene el registro (ej: miregistro.txt): ")
                if not menu.importarRegistro(nombre_txt):
                    print("No existe ningun archivo con el nombre",nombre_txt)
                else: print("Registro Cargado Correctamente")
            case 4:
                nombre_txt = input("Digite el nombre que desea para el archivo txt (ej: miregistro.txt): ")
                if menu.exportarRegistro(nombre_txt):
                    print("Registro Exportado Correctamente")
                else:
                    print("No hay registro para exportar a .txt")
            case 5:
                eliminado = menu.eliminarRegistro()
                if eliminado:
                    print("Registro eliminado exitosamente")
                elif eliminado is False:
                    print("No existe ningun registro para eliminar")
            case 6:
                if not menu.getRegistro():
                    print("No existe ningun registro, porfavor cree uno")
                    continue
                while True:
                    documento = int(input("Ingrese el documento: "))
                    contraseña = input("Ingrese la contraseña: ")
                    mensajeria = Mensajeria(menu.getRegistro())
                    inicio = mensajeria.iniciarSesion(documento, contraseña)
                    if inicio:
                        mensajeria.main()
                        break
                    elif inicio is False:
                        print("Contraseña Incorrecta\n")
                    else:
                        print("No existe un usuario con ese documento")
                        break
            case 0: break
            case _: print("Opcion invalida: intente de nuevo")

main()