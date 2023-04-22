divisor=2
def dividir(dividendo):
    if divisor == 0 :
        print("no se puede dividir")
    return dividendo / divisor
print(dividir(10))

#FUNCIONES 
#sirve para reutilizar codigo
    #javascript: function name (parametross){codigo}

#java: public tipo de dato a retonar Nombrefuncion(parametros){codigos}

#PYTHON
#def nombreFuncion(parametros,parametro = valor por deffecto, *arg, **kwarg):
    #codigo
    #return valor,varios valores, resultadodeunavariable
#nombrefuncio(argumentos)


numero= 1,2
def Numero_Mayor_Menor(numero1,numero2):
    if numero1 > numero2:
        return numero1,numero2
    elif numero1 == numero2:
        return f"numero1:{numero2} y numero2:{numero1} son iguales"
    else:
        return numero2,numero1
    
print(Numero_Mayor_Menor(100,10))

#recursividadd: uso o llamado de la misma funcion declarada 

#eermplo:
#imprimir los numero del 10 al 1
def Mostrar(num):
    if num == 0:
        return 
    print(num)
    Mostrar(num-1)

    
    
Mostrar(10)
    

def factorial(num):
    if num > 1:
        num = num * factorial(num-1)
        
    return num

print(factorial(6))

