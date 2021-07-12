import pandas as pd

def sorteo():
    listado = pd.read_csv("participantes.csv")
    cantidad_ganadores = int(input("¿Cuántos ganadores desea? "))
    condicion = True
    while condicion:
        if cantidad_ganadores <= 0:
            cantidad_ganadores = int(input("¿Cuántos ganadores desea? "))
        elif cantidad_ganadores == 1:
            resultado = listado.sample(cantidad_ganadores)
            condicion = False
            print("---Resultado del sorteo---")
            return print(f"{resultado}")
        else: 
            resultado = listado.sample(cantidad_ganadores)
            condicion = False
            print("---Resultado del sorteo---")
            return print(f"{resultado}")

sorteo()