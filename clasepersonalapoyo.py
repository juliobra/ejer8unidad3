class PersonalApoyo(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.categoria = categoria