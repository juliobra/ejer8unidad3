class Docente(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.carrera = carrera
        self.cargo = cargo
        self.catedra = catedra