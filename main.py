import api.apif as piapi
import ui.uif as piui

def main():
    """This is the main function"""
    # Conectar con la API
    client = piapi.contact_api()
    # Obtener los datos del usuario
    user_data = piui.get_user_data(client)
    # Mostrar los datos formateados
    piui.show_data(user_data)

if __name__ == "__main__":
    main()
