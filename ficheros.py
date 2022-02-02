import glob
import os.path
import shutil
from turtle import pen



def escribir_menu():
    print("""
    FICHEROS
1. Leer fichero de texto
2. Copiar fichero
3. Listar archivos de directorio
0. Salir""")


def pedir_opcion():
    print('Escoja opcion: ', end= '')


def pedir_valor():
    try:
        return int(input())
    except ValueError:
        return None


def pedir_ruta():
        try:
            return input()
        except ValueError:
            return None


def comprobar_ruta(ruta):
    if(os.path.isfile(ruta)):
        file = open(ruta)
        print(file.read())
    else:
        print(f'La ruta {ruta} no es un fichero')

def leer_fichero():
    print('Escriba la ruta del fichero: ', end='')
    ruta = pedir_ruta()
    if (os.path.isfile(ruta)):
        comprobar_ruta(ruta)
    else:
        print(f"{ruta} no existe")

def copiar_fichero():
        print('Escriba la ruta del fichero de origen: ', end='')
        ruta_origen = pedir_ruta()
        if os.path.isfile(ruta_origen):
            print('Escriba la ruta del fichero de destino: ', end='')
            ruta_destino = pedir_ruta()
            shutil.copyfile(ruta_origen, ruta_destino)
            print("archivo copiado")


        else:
            print(f"{ruta_origen} no existe")


def lista_ficheros():
    print("Escriba ruta del directorio: ", end='')
    ruta = pedir_ruta()
    if os.path.isdir(ruta):

        for path, x, file in os.walk(ruta):
            for f in file:
                size = os.path.getsize(os.path.join(path, f))
                print(f, size)
    else:
        print(f"{ruta} no es un directorio")

if __name__ == "__main__":
    while True:
        escribir_menu()
        pedir_opcion()
        valor = pedir_valor()

        if valor==1:
            leer_fichero()

        elif valor==2:
            copiar_fichero()
        elif valor==3:
            lista_ficheros()
        elif valor==0:
            exit(0)
        else:
            print('Opcion no valida')