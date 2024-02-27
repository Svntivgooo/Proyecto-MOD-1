############ Modulo MAIN ############
from ModuloAPI import obtener_datos
from ModuloUI import mostrar_keys, mostrar_resultados_en_tabla

def main():
    limite_registros = int(input("Ingrese el número límite de registros: "))
    nombre_departamento = input("Ingrese el nombre del departamento: ")
    resultados = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio"]

    datos = obtener_datos(limite_registros, nombre_departamento)

    mostrar_keys(datos)
    print()
    mostrar_resultados_en_tabla(datos, resultados)

main()