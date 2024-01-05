"""
    1) Crear una función capaz de convertir números enteros de base 10 a base 2. Debe recibir como parámetro el número a convertir<br>
    Consideraciones:<br> 
    a. Tratar de resolverlo sin usar la función format(nro,"b")<br>
    b. El pdf "conversion-de-decimal-a-binario.pdf" puede servir de ayuda.
"""

def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if((type(numero) != int) or (numero < 0)):
        return None
    if(numero == 0):
        resultado = 0
        return resultado
    else:    
        num_Bin = 0
        multiplicador = 1
        while numero != 0:
            num_Bin = num_Bin + numero % 2 * multiplicador
            numero //= 2
            multiplicador *= 10
    return num_Bin

print(NumeroBinario(29))

def FracBin(num):
    num_Bin = 0
    parte_entera = 0
    while num != 0:
        x = num * 2
        if x > 1:
            x == 1
        elif x < 1:
            x == 0
        elif num * 2 == 1:
            x == 1
            num_Bin = num_Bin * x
            break
        num_Bin = num_Bin * x
    return num_Bin

print(FracBin(0.3125))
