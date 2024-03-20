class Fecha:
    def __init__(self, fecha: str) -> None:
        dia,mes,año = Fecha.separarFecha(fecha)
        self.dia = dia
        self.mes = mes
        self.año = año

    def separarFecha(fecha: str):
        separado = fecha.split("/")
        return separado[0], separado[1], separado[2]

    def toString(self):
        return f"""{self.dia}/{self.mes}/{self.año}"""