import clasemail


def modificarcontrasenia():
    print('ingrese la contraseña actual para modificar')
    if(input() == email.contraseña):
        print('ingrese la nueva contraseña')
        email.contrasenia=input()
    else:
        print('contraseña incorrecta')

def crearobjeto():
    print('ingrese mail')
    email2=clasemail.clase.CrearCuentainput()

if __name__ == '__main__':
    print('ingrese nombre y su id de cuenta,dominio,tipo de dominio y contraseña')
    nom=input()
    email=clasemail.clase(input(),input(),input(),input())
    print('estimado',nom,'te enviaremos mensajes a la dirección',email.retornaEmail())
    modificarcontrasenia()
    crearobjeto()

