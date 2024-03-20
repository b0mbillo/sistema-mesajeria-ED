class Direccion:
    def __init__(self, direccion: str) -> None:
        calle,numero,nomenclatura,barrio,ciudad = Direccion.separarDireccion(direccion) 
        self.tipo_calle = calle
        self.numero = numero
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad

    def separarDireccion(direccion: str):
        separado = direccion.split()
        return separado[0], separado[1], separado[2], separado[3], separado[4]
    
    def toString(self):
        return f"""{self.tipo_calle} {self.numero} {self.nomenclatura} {self.barrio} {self.ciudad}"""