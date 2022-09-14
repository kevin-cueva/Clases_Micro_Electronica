"""Escriba una función que solicite el nombre al usuario y le regrese un
saludo con el nombre digitado. Posteriormente escriba un decorador
que sólo permita ejecutar la función escrita anteriormente si una
contraseña es correcta."""
global password;
password = "123"

#Decorador
def autenticacion(function):
    password_usuario = input("DIgite la contraseña: ")
    def wrapper():
        if (password == password_usuario):
            return function()
        
    return wrapper

@autenticacion
def solicita_nombre():
    request =  input("digite su nombe: ")
    input(f'Un placer verte {request}')
    return request


print(solicita_nombre())




