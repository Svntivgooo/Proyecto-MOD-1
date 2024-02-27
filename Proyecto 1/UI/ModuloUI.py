############ Modulo Interfaz ############
from tabulate import tabulate

def mostrar_keys(results_df):
    for key in results_df.keys():
        pass

def mostrar_resultados_en_tabla(results_df, resultados):
    print()
    print(results_df[resultados].to_markdown(index=False, headers=["Ciudad de ubicación", "Departamento", "Edad", "Tipo de contagio", "Estado", "País de residencia"]))