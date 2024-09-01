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
    formatted_data = results[["ciudad_municipio_nom", "departamento_nom", "edad", "sexo", "estado"]]
    return formatted_data
