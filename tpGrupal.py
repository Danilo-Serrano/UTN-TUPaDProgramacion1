# #16)
class Cadena:
    def contiene_numero(self, texto):
        for caracter in texto:
            if caracter.isdigit():
                print("La cadena contiene números")
                return
        print("La cadena no contiene números")
c = Cadena()
c.contiene_numero(input("Ingresa una cadena "))
# #17)
class FuncionesPrograma:
    @staticmethod
    def getFechaString(fecha):
        dia, mes, anio = fecha.split("/")
        dias = {
            "1": "Uno", "2": "Dos", "3": "Tres", "4": "Cuatro", "5": "Cinco",
            "6": "Seis", "7": "Siete", "8": "Ocho", "9": "Nueve", "10": "Diez",
            "11": "Once", "12": "Doce", "13": "Trece", "14": "Catorce", "15": "Quince",
            "16": "Dieciséis", "17": "Diecisiete", "18": "Dieciocho", "19": "Diecinueve",
            "20": "Veinte", "21": "Veintiuno", "22": "Veintidós", "23": "Veintitrés",
            "24": "Veinticuatro", "25": "Veinticinco", "26": "Veintiséis", "27": "Veintisiete",
            "28": "Veintiocho", "29": "Veintinueve", "30": "Treinta", "31": "Treinta y uno"
        }
        meses = {
            "1": "Enero", "2": "Febrero", "3": "Marzo", "4": "Abril",
            "5": "Mayo", "6": "Junio", "7": "Julio", "8": "Agosto",
            "9": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
        }
        dia_literal = dias.get(str(int(dia)), dia)
        mes_literal = meses.get(str(int(mes)), mes)
        print(f"{dia_literal} de {mes_literal} de {anio}")
FuncionesPrograma.getFechaString(input("Ingresa una fecha así dd/mm/aaaa "))
#18)
from datetime import date
class FuncionesPrograma:
    @staticmethod
    def getFechaDate(dia: int, mes: int, anio: int) -> date:
        return date(anio, mes, dia)
class Principal:
    @staticmethod
    def main():
        d = int(input("Ingrese el día: "))
        m = int(input("Ingrese el mes: "))
        a = int(input("Ingrese el año: "))
        fecha = FuncionesPrograma.getFechaDate(d, m, a)
        print("La fecha es:", fecha)
Principal.main()
#19)
class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = None
    def sumarNumeros(self):
        return self.valor1 + self.valor2
    def restarNumeros(self):
        return self.valor1 - self.valor2
    def multiplicarNumeros(self):
        return self.valor1 * self.valor2
    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: división por cero"
    def aplicarOperacion(self, operacion):
        self.operacion = operacion
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"
class Calculo:
    @staticmethod
    def main():
        v1 = float(input("Ingrese el primer valor: "))
        v2 = float(input("Ingrese el segundo valor: "))
        op = OperacionMatematica(v1, v2)
        print("Suma:", op.aplicarOperacion("+"))
        print("Resta:", op.aplicarOperacion("-"))
        print("Multiplicación:", op.aplicarOperacion("*"))
        print("División:", op.aplicarOperacion("/"))
Calculo.main()
#20)
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    @staticmethod
    def sumarFracciones(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)
    @staticmethod
    def restarFracciones(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)
    @staticmethod
    def multiplicarFracciones(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)
    @staticmethod
    def dividirFracciones(f1, f2):
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)
    def mostrar(self):
        return f"{self.numerador}/{self.denominador}"
class OperacionesFraccion:
    @staticmethod
    def main():
        n1 = int(input("Ingrese numerador de la primera fracción: "))
        d1 = int(input("Ingrese denominador de la primera fracción: "))
        n2 = int(input("Ingrese numerador de la segunda fracción: "))
        d2 = int(input("Ingrese denominador de la segunda fracción: "))
        f1 = Fraccion(n1, d1)
        f2 = Fraccion(n2, d2)
        suma = Fraccion.sumarFracciones(f1, f2)
        resta = Fraccion.restarFracciones(f1, f2)
        multi = Fraccion.multiplicarFracciones(f1, f2)
        divi = Fraccion.dividirFracciones(f1, f2)
        print("Suma:", suma.mostrar())
        print("Resta:", resta.mostrar())
        print("Multiplicación:", multi.mostrar())
        print("División:", divi.mostrar())
OperacionesFraccion.main()


