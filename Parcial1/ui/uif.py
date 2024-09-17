"""This module is the user interface of the program"""
import api.apif as piapi

def request_size():
    """This function requests the size of the data to be extracted"""
    print("Ingrese el tamaño de la solicitud")
    size = int(input())
    return size

def request_departament():
    """This function requests the department to be extracted"""
    print("Ingrese el departamento")
    departament = input()
    return departament

def get_user_data(client):
    """This function gets the user data"""
    size = request_size()
    departament = request_departament()
    client = piapi.contact_api()
    
    # Obtener datos de la API
    raw_results = piapi.get_data(size, departament, client)
    
    # Convertir a DataFrame
    results = piapi.save_data(raw_results)
    
    # Exploración inicial de los datos extraídos
    piapi.initial_exploration(results)
    
    # Formatear y procesar los datos
    formatted_results = piapi.format_data(results)
    wrangled_results = piapi.data_wrangling(formatted_results)
    
    # Identificación de valores faltantes en los datos procesados
    piapi.missing_values(wrangled_results)
    
    # Estadísticas básicas de los datos procesados
    piapi.basic_statistics(wrangled_results)
    
    return wrangled_results

def show_data(data):
    """This function shows the data"""
    print(data)
    




