from os import mkdir, listdir
from os.path import exists

import shutil


__version__ = 2.0
__autor__   = "Mario"
__github__  = "https://github.com/Maalfer?tab=repositories"

def crear_carpetas_si_no_existe(carpetas):
    """
        Esta funcion recibe en forma de lista, las carpetas a crear
        si no existen. Ejemplo de uso:

            carpetas = ["documentos", "fotos"]
            crear_carpetas_si_no_existe(carpetas)

        Esto comprueba si exite la carpeta documentos y la carpeta fotos,
        en caso contrario, la crea
    """
    while (True):
        for carpeta in carpetas:
            if exists(carpeta) != True:
                # si la carpeta no existe exists() retorna False lo cual es diferente a True
                #  y esta condicion se llevara a cabo
                mkdir(carpeta)
                print("[*] Creando la carpeta -> {}".format(carpeta))
    """
        # Este fragmento de codigo se a optimizado anteriormente
        if exists("documentos") == True: 
            pass
        else: 
            mkdir("documentos")
            continue
        if exists("fotos") == True: pass
        else:
            mkdir("fotos") 
            continue
        if exists("videos") == True:
            pass
        else:
            mkdir("videos")
            continue
        if exists("otros") == True:
            pass
        else:
            mkdir("videos")
            continue
        if exists("musica") == True:
            pass
        else:
            mkdir("musica")
        break
    """

if __name__ == "__main__":
    """_summary_
        Este codigo solo sera ejecutado si no a sido importado este archivo.
        Es decir, solo si se a ejecutado mediante python Orden.py.
        Si se a importado mediante un import Orden, este codigo no se
        ejecutara.
    """

    ruta = "./" # en este campo podemos especificar la ruta en la que trabaja el script
    # en este caso, la ruta es ./ que es el directorio actual.

    carpetas = ["documentos", "fotos", "videos", "otros", "musica"]
    extensionesdocumentos = [".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".ppt", ".pptx"]
    
    documentos = [archivo for archivo in listdir() if archivo.endswith(extensionesdocumentos)]
    """
        el metodo endswith() comprueba que el archivo finaliza con la extension deseada
        ejemplo:
        
            archivo = "Imagen.png"
            extencion = ".png"    
            x = archivo.endswith(extenxion)
            print(x)
            
        En este caso, al acabar el string "Imagen.png" con la extension ".png", x valdra True.
        
        Con este bucle, se lista el contenido del directorio actual haciendo uso de la funcion
        listdir() del modulo os. A continuacion se recorre la lista que retorna y almacena
        cada valor en archivo por iteracion(repeticion). con el if comprobamos si el archivo
        acaba en la extension deseada, y solo si es asi, se agrega dicho archivo a la lista documentos.
    """

    print(documentos)
    #crear_carpetas_si_no_existe(carpetas)

    for i in documentos:
        shutil.move(i, "documentos")



    extensionesfotos = r".png", r".jpg", r".jpeg", r".gif",r".tiff", r".bmp"
    fotos = [_ for _ in listdir() if _.endswith(extensionesfotos)]

    for i in fotos:
        shutil.move(i, "fotos")



    extensionesvideos = r".mp4", r".mkv", r".avi", r".mov",r".flv", r".divx"
    videos = [_ for _ in listdir() if _.endswith(extensionesvideos)]

    for i in videos:
        shutil.move(i, "videos")


    extensionesmusica = r".mp3", r".aac", r".wav", r".aiff",r".wma",r".opus",r".ogg"
    musica = [_ for _ in listdir() if _.endswith(extensionesmusica)]

    for i in musica:
        shutil.move(i, "musica")


    extensionesotros = r".py", r".rar", r".zip", r".html",r".tmp",r".dat",r".exe",r".deb",r".dmg"r".psd"
    otros = [_ for _ in listdir() if _.endswith(extensionesotros)]

    for i in otros:
        shutil.move(i, "otros")