def sumar_dos():
    while True:
        a = input("Ingrese un número: ")
        b = input("Ingrese otro número: ")
        try:
            resultado = float(a) + float(b)                                                                           
        # except Exception as e: #Si el except se ejecuta, no se ejecuta el else y viceversa
        except ValueError as e:
            print("Por favor, ingrese solo números")
            print(f"Error: {e}")
            # print(f"Error: {type(e).__name__}")
        else: #Se ejecuta si no hay excepciones al finalizar el bloque try
            break
        finally: #Se ejecuta siempre, haya excepciones o no
            print("Gracias por usar el programa")
    return resultado
    
print(sumar_dos())