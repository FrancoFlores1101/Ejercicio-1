import csv
from clasemail import clase
from manejadormails import manejador
import email

def modificarcontrasenia():
    print('ingrese la contraseña actual para modificar')
    if(input() == email.contraseña):
        print('ingrese la nueva contraseña')
        email.contrasenia=input()
    else:
        print('contraseña incorrecta')

def crearobjeto():
    print('ingrese mail')
    email2=clase('','','','')
    email2.CrearCuenta(input())

def cargardirec():
    archivo=open('emails.csv')
    reader=csv.reader(archivo)
    for fila in reader:
        for i in range(10):
            p = clase('','','','')
            p.CrearCuenta(fila[i])
            m.agregarmail(p)


if __name__ == '__main__':
    print('ingrese nombre y su id de cuenta,dominio,tipo de dominio y contraseña')
    nom=input()
    email=clase(input(),input(),input(),input())
    print('estimado',nom,'te enviaremos mensajes a la dirección',email.retornaEmail())
    modificarcontrasenia()
    crearobjeto()
    m=manejador()
    cargardirec()
    m.buscarmail(input('ingrese mail a buscar\n'))
