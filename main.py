 def menu_tesorero(self):
        while True:
            print("------- Menú del Tesorero -------")
            print("1. Consultar gastos de sueldos para un agente")
            print("0. Salir")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                dni = input("Ingrese el número de documento del agente: ")
                self.lista_agentes.gastos_sueldo_por_empleado(dni)
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def menu_director(self):
        while True:
            print("------- Menú del Director -------")
            print("1. Modificar sueldo básico de un agente")
            print("2. Modificar porcentaje por cargo de un docente")
            print("3. Modificar porcentaje por categoría de un personal de apoyo")
            print("4. Modificar importe extra de un docente investigador")
            print("0. Salir")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                dni = input("Ingrese el número de documento del agente: ")
                nuevo_basico = float(input("Ingrese el nuevo sueldo básico: "))
                self.lista_agentes.modificar_basico(dni, nuevo_basico)
            elif opcion == "2":
                dni = input("Ingrese el número de documento del docente: ")
                nuevo_porcentaje = float(input("Ingrese el nuevo porcentaje por cargo: "))
                self.lista_agentes.modificar_porcentaje_por_cargo(dni, nuevo_porcentaje)
            elif opcion == "3":
                dni = input("Ingrese el número de documento del personal de apoyo: ")
                nuevo_porcentaje = float(input("Ingrese el nuevo porcentaje por categoría: "))
                self.lista_agentes.modificar_porcentaje_por_categoria(dni, nuevo_porcentaje)
            elif opcion == "4":
                dni = input("Ingrese el número de documento del docente investigador: ")
                nuevo_importe_extra = float(input("Ingrese el nuevo importe extra: "))
                self.lista_agentes.modificar_importe_extra(dni, nuevo_importe_extra)
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Intente nuevamente.")


sistema = SistemaUniversitario()
sistema.autenticar_usuario()

if __name__=='__main__':
                  menu_tesorero()
  menu_director()
























