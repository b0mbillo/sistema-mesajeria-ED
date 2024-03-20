from registro import Registro
from usuario import Usuario
from fecha import Fecha
from direccion import Direccion
from mensajes import Mensajes
from copy import deepcopy
from datetime import datetime as dt

class Mensajeria():
    def __init__(self, registro: Registro) -> None:
        self.registro = registro
        self.perfil = None
        self.usuario = None

    def iniciarSesion(self, documento: int, contraseña: str):
        busqueda, indice = self.registro.buscarUsuario(documento)
        if not busqueda:
            return
        if busqueda.getPassword() != contraseña:
            return False
        self.perfil = busqueda.getPerfil()
        self.usuario = busqueda
        return True

    def getUsuario(self):
        return self.usuario

    def getPerfil(self):
        return self.perfil

    def getRegistro(self):
        return self.registro

    def menuAdministrador(self):
        """mismas  funcionalidades  que  los empleados,  pero  además  puede,  registrar  nuevos  usuarios  al  sistema,  cambiar  contraseñas,  y  eliminar 
usuarios. """
        opciones = [i for i in range(8)]
        try:
            opcion = int(input(f"""\nBienvenido {self.usuario.getNombre()}, Que desea hacer?

        0 : Salir
        1 : Revisar bandeja de entrada
        2 : Revisar mensajes leidos
        3 : Mostrar borrador
        4 : Enviar mensaje 
        5 : Registrar usuario
        6 : Eliminar usuario
        7 : Cambiar contraseña

        Digite su opcion: """))
            if opcion not in opciones:
                raise ValueError
        except ValueError: #no es necesario excepciones si evaluo la opcion como str en vez de int
            opcion = None
        return opcion


    def menuEmpleado(self):
        """El “empleado” puede revisar su bandeja de entrada, los  mensajes  leídos,  proyectar  mensaje  que  se 
mantienen en borradores, y enviar mensajes a usuarios del sistema. """
        opciones = [i for i in range(5)]
        try:
            opcion = int(input(f"""\nBienvenido {self.usuario.getNombre()}, Que desea hacer?

        0 : Salir
        1 : Revisar bandeja de entrada
        2 : Revisar mensajes leidos
        3 : Mostrar borrador
        4 : Enviar mensaje

        Digite su opcion: """))
            if opcion not in opciones:
                raise ValueError
        except ValueError: 
            opcion = None   
        return opcion
        

    def main(self):
        
        while True:
            if self.perfil == "administrador":
                opcion = self.menuAdministrador()
            else:
                opcion = self.menuEmpleado()
            match opcion:
                case 1:
                    self.revisarBandeja()
                case 2:
                    self.revisarLeidos()
                case 3:
                    self.mostrarBorrador()
                case 4:
                    documento = int(input("Digite el documento del destinatario: "))
                    titulo = input("Digite el asunto: ")
                    mensaje = input("Digite el mensaje: ")
                    self.enviarMensaje(titulo, documento, mensaje)
                case 5:
                    añadir = self.registrarUsuario()
                    if añadir:
                        print("Añadido Correctamente")
                    elif añadir is False:
                        print("Ya existe un usuario con este documento, no se pudo agregar el usuario")
                    else:
                        print("El registro esta lleno, no se puede agregar usuarios")
                case 6:
                    eliminado = self.eliminarUsuario()
                    if eliminado:
                        print("Eliminado Correctamente")
                    else:
                        print("No existe un usuario con ese documento")
                case 7:
                    documento = int(input("Digite el documento: "))
                    contraseña = input("Digite la contraseña nueva: ")
                    cambiar = self.cambiarPassword(documento, contraseña)
                    if cambiar:
                        print(f"Se cambio exitosamente la contraseña de: {cambiar.getNombre()}")
                    else:
                        print("No existe un usuario con ese documento")
                case 0: return
                case _: print("Opcion invalida: intente de nuevo")

    def registrarUsuario(self):
        if self.registro.getUsuarios() == self.registro.getCapacidad():
            return
        documento = int(input("Digite el documento: "))
        nombre = input("Digite el nombre: ")
        fecha_nacimento = input("Digite la fecha de nacimento (siguiendo el formato: dia/mes/año, ej: 12/03/2000): ")
        ciudad_nacimiento = input("Digite la ciudad de nacimiento: ")
        direccion = input("Digite la direccion (siguiendo el formato: calle numero nomenclatura barrio ciudad, ej: Calle 83 #45-23 Campo_Valdes Medellin): ")
        tel = input("Digite el telefono: ")
        email = input("Digite el email: ")
        contraseña = input("Digite la contraseña: ")
        perfil = input("Digite el tipo de perfil: ")
        fecha = Fecha(fecha_nacimento)
        direccion = Direccion(direccion) 
        usuario = Usuario(documento, nombre, fecha, ciudad_nacimiento, direccion, tel, email, contraseña, perfil, Mensajes())
        añadir = self.registro.registrarUsuario(usuario)
        return añadir

    def buscarUsuario(self, doc: int):
        busqueda, indice = self.registro.buscarUsuario(doc)
        #print(busqueda.toString())
        return busqueda

    def eliminarUsuario(self):
        doc = int(input("Digite el documento del usuario: "))
        eliminado = self.registro.eliminarUsuario(doc)
        return eliminado
    
    def cambiarPassword(self, documento, contraseña):
        busqueda, indice = self.registro.buscarUsuario(documento)
        if busqueda:
            busqueda.setPassword(contraseña)
        return busqueda
    
    def enviarMensaje(self, titulo: str, doc: int, mensaje: str, borrador = False):
        busqueda = self.buscarUsuario(doc)
        if not busqueda:
            print("No existe un usuario con este documento")
            return False
        tiempo = dt.now()
        fecha = tiempo.strftime("%d/%m/%Y %H:%M")
        bandeja = busqueda.getMensajes().getBandeja()
        borradores = self.usuario.getMensajes().getBorradores()
        
        opcion = "1"
        if not borrador:
            opcion = input("Que desea hacer: 1:Enviar 2:GuardarBorrador otro:Descartar: ")

        if opcion == "1":
            nombre = self.usuario.getNombre()
            if bandeja.addLast(f"{fecha}*{titulo}*{nombre}*{mensaje}"):
                print("Mensaje Enviado Correctamente")
                return True
        elif opcion == "2":
            nombre = busqueda.getNombre()
            if borradores.push(f"{fecha}*{titulo}*{nombre}*{mensaje}"):
                print("borrador Creado Correctamente")
                return True
        return
    
    def revisarBandeja(self):
        bandeja = self.usuario.getMensajes().getBandeja()
        nodo = bandeja.first()
        tamaño = bandeja.getSize()

        if tamaño == 0:
            print("No hay mensajes para leer")
            return False
        
        temp = bandeja.first()
        for i in range(tamaño):
            mensaje = temp.getData()
            fecha, titulo, persona, texto = mensaje.split("*")
            print(f"{i}. {fecha} Asunto:{titulo} Remitente:{persona}")
            temp = temp.getNext()


        indices = [str(i) for i in range(tamaño)]
        opcion = input("\nQue correo desea leer? ")
        if opcion not in indices:
            print("Opcion invalida")
            return 

        for _ in range(i):
            mensaje = nodo.getData()
            temp = nodo.getNext()

        fecha, titulo, persona, texto = mensaje.split("*")
        print(f"""
                  {fecha} 
                  Asunto:{titulo}
                  Remitente:{persona}
                  {texto}""")
        
        bandeja.remove(nodo)
        self.usuario.getMensajes().getLeidos().enqueue(mensaje)
        return True

    def revisarLeidos(self):
        leidos = self.usuario.getMensajes().getLeidos()
        temp = deepcopy(leidos)
        for _ in range(temp.getSize()):
            mensaje = temp.dequeue()
            fecha, titulo, persona, texto = mensaje.split("*")
            print(f"""
                  {fecha} 
                  Asunto:{titulo}
                  Remitente:{persona}
                  {texto}
""")
            decision = input("Continuar viendo? 1:Si, otro:No : ")
            if decision != "1":
                return
        print("No hay más mensajes leídos")
        return True

    def mostrarBorrador(self):
        borrador = self.usuario.getMensajes().getBorradores()
        opciones = ("1","2")
        size = borrador.getSize()
        if size == 0:
            print("No hay borradores")
            return False
        
        mensaje = borrador.top().getData()
        fecha, titulo, persona, texto = mensaje.split("*")
        print(f"""
                {fecha} 
                Asunto:{titulo}
                Destinatario:{persona}
                {texto}
""")
        decision = input("Que quiere hacer? 1:Enviar, 2:Descartar, otro:Nada : ")
        if decision not in opciones:
            return
        elif decision == "1":
            doc = self.registro.buscarUsuarioNombre(persona).getDocumento()
            if self.enviarMensaje(titulo, doc, texto, True):
                borrador.pop()
        else:
            borrador.pop()
            print("Borrador Descartado")
            return