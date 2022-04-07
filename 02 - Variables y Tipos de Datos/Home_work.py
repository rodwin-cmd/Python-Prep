##1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
from ast import MatchMapping


num1 = 2
print(num1)
##2) Imprimir el tipo de dato de la constante 8.5
num2= 8.5
type(num1)
##3) Imprimir el tipo de dato de la variable creada en el punto 1
type(num1)
##4) Crear una variable que contenga tu nombre
Nombre = "Rodwin"
##5) Crear una variable que contenga un número complejo
num3 = 1 + 1j
#6) Mostrar el tipo de dato de la variable crada en el punto 5
type(num3)
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
numeropi= 3.1416
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
valoreal = True
valorfalso = False
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
type(valoreal)
type(valorfalso)
#10) Asignar a una variable, la suma de un número entero y otro decimal
suma =  4 + float(5.6)
print(suma)
#1) Realizar una operación de suma de números complejos
numercom = 1j + 2j
print (numercom)
#12) Realizar una operación de suma de un número real y otro complejo
sumanu = 3 + complex (1j)
print (sumanu)
#13) Realizar una operación de multiplicación
num4 =  1 * 2
print(num4)
#14) Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2 ** 2
print (potencia)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
division = 27 / 4
print (division)
#16) De la división anterior solamente mostrar la parte entera
division = 27 // 4
print(division)
#17) De la división de 27 entre 4 mostrar solamente el 
27 % 4
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
6 * 4 + 3
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

variable1 = "buenas noches"
variable2 = "Colombia"
print (variable1+variable2)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
"2" == 2 #Es False, ya que esta comparando un string con un dato entero.

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
"2" == str(2)

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# no funciona ya que no se convierte un valor floar en un string
a = float(3.8)

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

variable3 =  3
variable3-= 1
print(variable3)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# << devuelve un valor a la izquierda en la escala binaria en N veces que se defina. >> devuelve un valor a la derecha en escala binaria N veces que se defina
 #128 64 32 16 8 4 2 0
 1 << 2

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
float(2) + float ('2')
 
#26) Realizar una operación válida entre valores de tipo entero y string
numero = '2'

2 + int(numero)