############ Modulo API ############
import pandas as pd
from sodapy import Socrata

def obtener_datos(limite_registros, nombre_departamento):
    client = Socrata("www.datos.gov.co", "z8hjJYbAY3udhGO55bp3A7hQu")
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=nombre_departamento)
    results_df = pd.DataFrame.from_records(results)
    return results_df