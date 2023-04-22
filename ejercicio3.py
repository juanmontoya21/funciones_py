def convertir(valor,medida_Origen,medida_Destino):    
    if medida_Origen == "c" and medida_Destino == "f":
        farenheit = (valor * 9/5) + 32
        print(f"farenheit = {farenheit}")
    
    if medida_Origen == "c" and medida_Destino == "k":
        kelvin = valor + 273.15
        print(f"kelvin = {kelvin}")
    
    if medida_Origen == "f" and medida_Destino == "c":
        celscius= (valor - 32) * 5/9
        print(f"celsius = {celscius}")
    if medida_Origen == "f" and medida_Destino == "k":
        kelvin = (valor + 459.67) * 5/9
        print(f"kelvin = {kelvin}")
    
    if medida_Origen == "k" and medida_Destino == "f":
        farenheit = (valor * 9/5) - 459.67
        print(f"farenheit = {farenheit}")
    if medida_Origen == "k" and medida_Destino == "c":   
        celscius = valor - 273.15
        print(f"celsius = {celscius}")

convertir(10,"c","f")
convertir(10,"c","k")
convertir(10,"f","k")
convertir(10,"f","c")
convertir(10,"k","f")
convertir(10,"k","c") 