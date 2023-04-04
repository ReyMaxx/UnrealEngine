# Importar la librería getpass para ocultar la contraseña
import getpass

# Definir la contraseña
password = "Chocolate"

# Pedir al usuario que ingrese la contraseña
input_password = getpass.getpass("Ingrese su contraseña: ")

# Verificar si la contraseña ingresada es correcta
if input_password == password:
    print("Contraseña correcta. Sesión iniciada.")
else:
    print("Contraseña incorrecta. Intente de nuevo.")
