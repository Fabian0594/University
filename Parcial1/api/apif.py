""" This module is responsible for the interaction with the API."""
import pandas as pd
from sodapy import Socrata

def contact_api():
    """ This function is responsible for the connection with the API."""
    client = Socrata("www.datos.gov.co", None)
    return client

def get_data(data_size, department, client):
    """ This function is responsible for the data extraction from the API."""
    results = client.get("gt2j-8ykr", limit = data_size, departamento_nom = department)
    return results


def save_data(results):
    """ This function is responsible for the data storage."""
    results = pd.DataFrame.from_records(results)
    return results

def format_data(results):
    """this funcions is responsible for the data formatting."""
    formatted_data = results[["ciudad_municipio_nom", "departamento_nom", "edad", "sexo", "estado", "fecha_muerte"]]
    return formatted_data

def data_wrangling(results):
    """This function is responsible for the data wrangling."""
    # usar .loc[] para modificar el DataFrame
    results.loc[:, "ciudad_municipio_nom"] = results["ciudad_municipio_nom"].str.upper()
    results.loc[:, "departamento_nom"] = results["departamento_nom"].str.upper()
    results.loc[:, "edad"] = pd.to_numeric(results["edad"], errors='coerce')  # Convertir a numérico, invalidos se convierten en NaN
    results.loc[:, "sexo"] = results["sexo"].str.upper()
    results.loc[:, "estado"] = results["estado"].str.upper()
    
    # Convertir a datetime y manejar errores
    results.loc[:, "fecha_muerte"] = pd.to_datetime(results["fecha_muerte"], errors='coerce')  # Convertir a datetime, invalidos se convierten en NaT
    
    # Reemplazar NaT con "RECUPERADO" después de convertir a string
    results.loc[:, "fecha_muerte"] = results["fecha_muerte"].astype('str').replace('NaT', 'RECUPERADO')

    return results


def basic_statistics(results):
    """Obtain basic descriptive statistics."""
    print("Estadísticas descriptivas básicas:")
    print(results.describe(include='all'))


def initial_exploration(results):
    """Initial exploration of the dataset."""
    print("Cantidad de registros y columnas:")
    print(results.shape)
    
def missing_values(results):
    """Identify missing values in the dataset."""
    print("Cantidad de valores faltantes por columna:")
    print(results.isnull().sum())
    
