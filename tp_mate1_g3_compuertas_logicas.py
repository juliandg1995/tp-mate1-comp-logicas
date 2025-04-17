# Compuerta OR
def c_or(a, b):
    if (a == 1 or b == 1):
        return 1
    else:
        return 0

# Compuerta AND
def c_and(a, b):
    if (a == 1 == b ):
        return 1.
    else:
        return 0.

# Compuerta NOT
def c_not(a):
     if (a == 1):
         return 0.
     elif(a == 0):
         return 1.
     
# Compuerta NAND --> AND + NOT
def compuerta_nand(a, b):
    return c_not( c_and(a,b) )

# Compuerta NOR --> OR + NOT
def compuerta_nor(a, b):
    return c_not( c_or(a,b) )

# Compuerta XOR --> (A AND NOT B) OR (NOT A AND B)
def compuerta_xor(a, b):
    return c_or( c_and(a, c_not(b)), c_and( c_not(a), b) )

a = 1
b = 0

print(f"El resultado de aplicar una operación NAND con las variables {a} y {b} es {compuerta_nand(a,b)}")


print("Holis")

