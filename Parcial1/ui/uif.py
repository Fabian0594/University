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
    results = piapi.save_data(piapi.get_data(size, departament, client))
    return results

def show_data(data):
    """This function shows the data"""
    print(piapi.format_data(data))
