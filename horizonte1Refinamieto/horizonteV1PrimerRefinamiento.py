class Trabajador:
    def __init__(self, nombre, sueldo_basico, dias_falta, minutos_tardanza, horas_extras):
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.dias_falta = dias_falta
        self.minutos_tardanza = minutos_tardanza
        self.horas_extras = horas_extras

    def calcular_bonificaciones(self):
        bonificacion_movilidad = 1000
        bonificacion_suplementaria = self.sueldo_basico * 0.03
        bonificacion_horas_extras = self.sueldo_basico * 0.5 * self.horas_extras
        return bonificacion_movilidad + bonificacion_suplementaria + bonificacion_horas_extras

    def calcular_descuentos(self):
        remuneracion_computable = self.sueldo_basico + self.calcular_bonificaciones()
        descuento_faltas = self.dias_falta * (remuneracion_computable / 30)
        descuento_tardanzas = self.minutos_tardanza * (remuneracion_computable / (30 * 8 * 60))
        return descuento_faltas + descuento_tardanzas

    def calcular_sueldo_neto(self):
        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()
        return self.sueldo_basico + bonificaciones - descuentos

    def imprimir_boleta_pago(self):
        sueldo_neto = self.calcular_sueldo_neto()
        print("Boleta de Pago")
        print("Nombre del Trabajador:", self.nombre)
        print("Sueldo Básico:", self.sueldo_basico)
        print("Bonificaciones:", self.calcular_bonificaciones())
        print("Descuentos:", self.calcular_descuentos())
        print("Sueldo Neto:", sueldo_neto)


# Uso de la clase Trabajador
trabajador = Trabajador("Juan Perez", 2000, 2, 30, 10)
trabajador.imprimir_boleta_pago()
