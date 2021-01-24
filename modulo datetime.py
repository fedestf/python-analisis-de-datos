from datetime import date
from datetime import time
import datetime

fecha = date(2013, 5, 20)

print('Dia: ', fecha.day)
print('Mes: ', fecha.month)
print('Año: ', fecha.year)

print(date.today())  # fecha de hoy

tiempo = time(15, 20, 13, 40)

print(tiempo)
print('Hora : ', tiempo.hour)
print('Minutos : ', tiempo.minute)
print('Segundos : ', tiempo.second)
print('Microsegundos : ', tiempo.microsecond)

# puedo aplicar todos los metodos anteriores
fechaConHora = datetime.datetime.now()

# el metodo .weekday() nos devuelve un numero correspondiente a cada dia de la semana desde 0=lunes a 6= domingo
fechaNow = datetime.datetime.now()
print(fechaNow.weekday())

# el metodo .isoweekday() nos devuelve el numero de la semana pero con formato iso(que en iso el primer dia de la semana es el domingo)
print(fechaNow.isoweekday())

# metodo .isocalendar() nos devuelve una tupla que representa una fecha
print(fechaNow.isocalendar())

# obtener fechas con otros metodos
fechaNow_datetime = date(2020, 4, 23).isoformat()
print(fechaNow_datetime)

# el metodo .strptime() nos permite leer una cadena de texto con una fecha en un formato indeterminado

fechaParaStripTime = '22 April, 2020 13:20:13'
d1 = datetime.datetime.strptime(fechaParaStripTime, '%d %B, %Y %H:%M:%S')
print(d1)

# la clase timedelta nos permite operar entre fechas tanto hacia adelante como hacia atras , solo se necesita cambiar el + por un -
fechaPasadoMañana = fechaNow + datetime.timedelta(days=2)
print('fecha de pasado mañana: ', fechaPasadoMañana)

fechaPasadasDosSemanas = fechaNow + datetime.timedelta(weeks=2)
print('fecha de pasadas dos semanas : ', fechaPasadasDosSemanas)
