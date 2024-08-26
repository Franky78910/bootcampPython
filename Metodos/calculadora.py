def Calculadora(num1, num2, Operación):
    print('Bienvenido a la calculadora'.center(50, "-"))
    if Operación== 1:
        return num1 + num2
    elif Operación== 2:
        return num1 - num2 
    elif Operación== 3:
        return num1 * num2
    elif Operación== 4:
        return num1 / num2
    else:
        print('esa opción no esta disponible')
        
print("Calculadora = 5, 5, 1")