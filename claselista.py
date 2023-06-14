class ListaAgentes:
    def __init__(self):
        self.coleccion = []

    def insertar_elemento(self, agente, posicion):
        if posicion < 0 or posicion > len(self.coleccion):
            raise ValueError("Posición inválida")
        self.coleccion.insert(posicion, agente)

    def agregar_elemento(self, agente):
        self.coleccion.append(agente)

    def mostrar_elemento(self, posicion):
        if posicion < 0 or posicion >= len(self.coleccion):
            raise ValueError("Posición inválida")
        agente = self.coleccion[posicion]
        print(agente.__class__.__name__)

    def mostrar_docentes_investigadores_por_carrera(self, carrera):
        docentes_investigadores = []
        for agente in self.coleccion:
            if isinstance(agente, DocenteInvestigador) and agente.carrera == carrera:
                docentes_investigadores.append(agente)
        docentes_investigadores.sort(key=lambda x: x.apellido)
        for agente in docentes_investigadores:
            print(f"{agente.apellido}, {agente.nombre} - Tipo de agente: {agente.__class__.__name__}")

    def contar_agentes_por_area_investigacion(self, area_investigacion):
        count_docente_investigador = 0
        count_investigador = 0
        for agente in self.coleccion:
            if isinstance(agente, DocenteInvestigador) and agente.area_investigacion == area_investigacion:
                count_docente_investigador += 1
            elif isinstance(agente, Investigador) and agente.area_investigacion == area_investigacion:
                count_investigador += 1
        print(f"Cantidad de docentes investigadores en el área {area_investigacion}: {count_docente_investigador}")
        print(f"Cantidad de investigadores en el área {area_investigacion}: {count_investigador}")

    def mostrar_datos_agentes(self):
        agentes = sorted(self.coleccion, key=lambda x: x.apellido)
        for agente in agentes:
            print(f"{agente.apellido}, {agente.nombre} - Tipo de agente: {agente.__class__.__name__} - Sueldo: {agente.calcular_sueldo()}")

    def listar_docentes_investigadores_por_categoria(self, categoria):
        docentes_investigadores = []
        total_importe_extra = 0
        for agente in self.coleccion:
            if isinstance(agente, DocenteInvestigador) and agente.categoria == categoria:
                docentes_investigadores.append(agente)
                total_importe_extra += agente.importe_extra
        docentes_investigadores.sort(key=lambda x: x.apellido)
        for agente in docentes_investigadores:
            print(f"{agente.apellido}, {agente.nombre} - Importe extra: {agente.importe_extra}")
        print(f"Total de importe extra para la categoría {categoria}: {total_importe_extra}")

    def guardar_agentes(self):
        with open("personal.json", "w") as file:
            for agente in self.coleccion:
                data = {
                    "cuil": agente.cuil,
                    "apellido": agente.apellido,
                    "nombre": agente.nombre,
                    "sueldo_basico": agente.sueldo_basico,
                    "antiguedad": agente.antiguedad
                }
                if isinstance(agente, Docente):
                    data["carrera"] = agente.carrera
                    data["cargo"] = agente.cargo
                    data["catedra"] = agente.catedra
                elif isinstance(agente, PersonalApoyo):
                    data["categoria"] = agente.categoria
                elif isinstance(agente, Investigador):
                    data["area_investigacion"] = agente.area_investigacion
                    data["tipo_investigacion"] = agente.tipo_investigacion
                elif isinstance(agente, DocenteInvestigador):
                    data["carrera"] = agente.carrera
                    data["cargo"] = agente.cargo
                    data["catedra"] = agente.catedra
                    data["area_investigacion"] = agente.area_investigacion
                    data["tipo_investigacion"] = agente.tipo_investigacion
                    data["categoria"] = agente.categoria
                    data["importe_extra"] = agente.importe_extra
                file.write(str(data) + "\n")

