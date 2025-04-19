import tp_mate1_g3_compuertas_logicas as compuertas
stop = ''
print("Bienvenido al simulador de compuertas lógicas\n")
while stop != 'X':
    stop = input("Presione 'X' para salir o cualquier otra tecla para continuar: ")
    if stop == 'X':
        break
    else:
        ##### VALORES A PROCESAR  #####
        # Se ingresa y valida el primer valor
        while True:
            entrada = input("Ingrese el primer valor (0 o 1): ")
            try:
                a = int(entrada)
                if 1 == a or 0 == a:
                    break
                else:
                    print("Error: El valor ingresado no es 0 o 1.") 
            except ValueError:
                print("Error: Eso no es un número entero.")
        
       # Se ingresa y valida el segundo valor
        while True:
            entrada = input("Ingrese el segundo valor (0 o 1): ")
            try:
                b = int(entrada)
                if 1 == b or 0 == b:
                    break
                else:
                    print("Error: El valor ingresado no es 0 o 1.")
            except ValueError:
                print("Error: Eso no es un número entero.")
                
        ##### ELECCIÓN DE COMPUERTA LÓGICA  #####
        print("Seleccione la compuerta lógica a utilizar:")
        print("1. OR")
        print("2. AND")
        print("3. NOT (Sólo aplica al primer valor ingresado)")
        print("4. NAND")
        print("5. NOR")
        print("6. XOR")
        print("7. Salir")
        
        while True:
            entrada = input("Ingrese el número de la compuerta lógica: ")
            try:
                compuerta = int(entrada)
                if 1 <= compuerta <= 7:
                    break
                else:
                    print("Error: El valor ingresado no es válido.")
            except ValueError:
                print("Error: Eso no es un número entero.")
                
        if compuerta == 7:
            break
        else:
            match compuerta:
                case 1:
                    print("Compuerta OR seleccionada.")
                    print(f"Resultado: {compuertas.c_or(a, b)}")
                case 2:
                    print("Compuerta AND seleccionada.")
                    print(f"Resultado: {compuertas.c_and(a, b)}")
                case 3:
                    print("Compuerta NOT seleccionada.")
                    print(f"Resultado: {compuertas.c_not(a)}")
                case 4:
                    print("Compuerta NAND seleccionada.")
                    print(f"Resultado: {compuertas.compuerta_nand(a, b)}")
                case 5:
                    print("Compuerta NOR seleccionada.")
                    print(f"Resultado: {compuertas.compuerta_nor(a, b)}")
                case 6:
                    print("Compuerta XOR seleccionada.")
                    print(f"Resultado: {compuertas.compuerta_xor(a, b)}")
                case _:
                    print("Error: Opción no válida.")
                    
print("\nGracias por usar el simulador de compuertas lógicas!")
print("""\nGrupo 3 - Matemática 1 TUP UTN\n
        Integrantes:\n
        - Julián Daniel Gómez\n
        - \n
        - \n
        - \n
        - \n""")
        
