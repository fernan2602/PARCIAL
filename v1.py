class trabajador:
    def __init__(self):
        self.nombreTrabajador = (input("Ingrese el nombre del trabajador: "))
        self.sueldoBasico = int(input("Ingrese el sueldo basico del trabajador: "))
        self.horasExtra = int(input("Ingrese las horas extras del trabajador: "))
        self.diasFalta = int(input("Ingrese los dias de falta: "))
        self.horasTardanza = int(input("Ingrese las horas de tardanza del trabajador: "))
    
    def imprimir(self):
        print("----------- BOLETA DEL TRABAJADOR ---------------")
        print("Nombre del trabajador: ",self.nombreTrabajador)
        print("Sueldo basico del trabajador: ",self.sueldoBasico)
        print("Las horas extra del trabajador son: ",self.horasExtra)
        print("Los dias de falta del trabajadr: ",self.diasFalta)