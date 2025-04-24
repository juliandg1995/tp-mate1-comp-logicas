#### COMPUERTAS LÓGICAS #####
# Este módulo contiene las funciones para las compuertas lógicas OR, AND, NOT, NAND, NOR y XOR.
# Se definen las funciones para cada compuerta lógica, que toman dos entradas (a y b) y devuelven el resultado de la operación lógica correspondiente.

# Compuerta OR
def c_or(a, b):
    if (a == 1 or b == 1):
        return int(1)
    else:
        return int(0)

# Compuerta AND
def c_and(a, b):
    if (a == 1 == b ):
        return int(1)
    else:
        return int(0)

# Compuerta NOT
def c_not(a):
     if (a == 1):
         return int(0)
     elif(a == 0):
         return int(1)
     
# Compuerta NAND --> AND + NOT
def compuerta_nand(a, b):
    return int(c_not( c_and(a,b)))

# Compuerta NOR --> OR + NOT
def compuerta_nor(a, b):
    return int(c_not( c_or(a,b)))

# Compuerta XOR --> (A AND NOT B) OR (NOT A AND B)
def compuerta_xor(a, b):
    return int(c_or( c_and(a, c_not(b)), c_and( c_not(a), b)))
