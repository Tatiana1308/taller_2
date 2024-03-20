# Comentario de una linea
# Todo lo que va despues es ignorado por el interprete de Python

# Espacio de memoria, con nombre, donde guardo valores
# Los nombres de variables deben ser cortos, descriptivos, NO TENER ESPACIOS 
# EN BLANCO ni caracteristicas especiales, no deben empezar por un numero

# Descriptivo significa que respresenta la categoria del dato que quiero guardar
# En Python las variables pueden contener  cualquier dato de tipo primitivo
# numero (enteros, reales), cadenas de caracteres(string), booleanos (verdadero, falso)
#caracteres(letras).

variable= 1

variable= 'Juventud divino tesoro, te vas para no volver, cuando quiero llorar'

variable= True

variable= 'a'

variable= 3.1415926535

# Para asignar un valor a la variable se usa el operador =


# Operadores: Mecanismo para obtener un dato a partir de otros datos
# Los datos que intervienen se llaman operandos

# Aritmeticos: + - * / %
# De comparacion: retornar True or False. > < >= <= == !=
# Los de logica booleana: OR AND. retornan True or False de acuerdo a una
 #tabla de verdad. Los operandos siempre son booleanos (True or False)

a= True
b= False

print (a and b)

# Los operandos booleanos y de comparacion son muy utilizados al
#definir condiciones

# Sentencias de control de flujo: en general un programa se ejecuta
# linea por linea de manera secuencial. Se puede romper esa sencuencialidad 
# empleando un conjunto de sentencias (expresiones) que permite:
# 1. seleccionar la ejecucion de un bloque de codigo
# 2. seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo
# de esa manera podemos "romper# la secuencialidad 
# principios del paradigma de programacion estructurado

# Sentencia if. Si se cumple una condicion (se evalua como True) se ejecuta un bloque de codigo
# se ejecuta un bloque de codigo

print("linea 1")
print ("linea 2")

if 5>3:
    print("Esto se muestra si la condicion es verdadera")

else:
    print("Esto se muestra si la condicion es falsa")

entrada= int(input("Cuantos años tiene?"))

if entrada< 18:
    print(" Es menor de edad.")

else:
    print(" ya esta grande.")



