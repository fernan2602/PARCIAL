class Trabajador:
    def __init__(self, nombre, sueldo_basico, dias_falta, minutos_tardanza, horas_extra):
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.dias_falta = dias_falta
        self.minutos_tardanza = minutos_tardanza
        self.horas_extra = horas_extra

    def calcular_bonificaciones(self):
        pago_horas_extra = 1.50 * self.horas_extra * self.sueldo_basico / 30 / 8
        movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = movilidad + bonificacion_suplementaria + pago_horas_extra
        remuneracion_computable = self.sueldo_basico + movilidad + bonificacion_suplementaria
        return bonificaciones, remuneracion_computable

    def calcular_descuentos(self, bonificaciones, remuneracion_computable):
        remuneracion_minima = self.sueldo_basico + bonificaciones
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas
        return descuentos

    def calcular_sueldo_neto(self):
        bonificaciones, remuneracion_computable = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos(bonificaciones, remuneracion_computable)
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos
        return sueldo_neto

    def imprimir_boleta_pago(self):
        bonificaciones, remuneracion_computable = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos(bonificaciones, remuneracion_computable)
        sueldo_neto = self.calcular_sueldo_neto()

        print("----- Boleta de Pago -----")
        print("Nombre del Trabajador:", self.nombre)
        print("Sueldo Básico:", self.sueldo_basico)
        print("Bonificaciones:", bonificaciones)
        print("Descuentos:", descuentos)
        print("Sueldo Neto a Pagar:", sueldo_neto)

# Ingreso de datos
nombre = input("Ingrese el nombre del trabajador: ")
sueldo = float(input("Ingrese el sueldo básico del trabajador: "))
dias_falta = int(input("Ingrese los días de faltas del trabajador: "))
minutos_tardanza = int(input("Ingrese los minutos de tardanzas del trabajador: "))
horas_extra = int(input("Ingrese las horas extras trabajadas por el trabajador: "))

# Crear una instancia de la clase Trabajador
trabajador = Trabajador(nombre, sueldo, dias_falta, minutos_tardanza, horas_extra)
trabajador.imprimir_boleta_pago()