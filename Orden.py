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

def asociar_carpetas_con_extensiones(nombre_carpeta, extensiones_de_archivos, ruta="."):
    """
        Esta funcion recibe una tupla en el argumento extensiones_de_archivos 
        que contiene las extensiones de los archivos que se quiere
        guardar en la carpeta que se especificar en el argumento nombre_carpeta.
        nombre_carpeta es un argumento de tipo string(str), este valor a de ser el nombre
        de la carpeta a la que se le asociara lass extensiones. Opcionalmente se le puede
        especificar la ruta a trabajar, con el argumento ruta, el cual a de ser un string.
        Ejemplo de uso:
        
            MisExtensiones = (".txt", ".docx")
            MiCarpeta      = "Documentos"
            asociar_carpetas_con_extensiones(MisExtensiones, MiCarpeta)
    """
    ArchivosParaEstaCarpeta = []
    
    for archivo in listdir(ruta):
        if archivo.endswith(extensiones_de_archivos) == True:
            ArchivosParaEstaCarpeta.append(archivo)
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
    
    return ArchivosParaEstaCarpeta
    


if __name__ == "__main__":
    """
        Este codigo solo sera ejecutado si no a sido importado este archivo.
        Es decir, solo si se a ejecutado mediante python Orden.py.
        Si se a importado mediante un import Orden, este codigo no se
        ejecutara.
    """

    ruta = "./" # en este campo podemos especificar la ruta en la que trabaja el script
    # en este caso, la ruta es ./ que es el directorio actual.


    carpetas = ["documentos", "fotos", "videos", "musica", "otros"]
    crear_carpetas_si_no_existe(carpetas)
    
    extensionesdocumentos = [   
                                (".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".ppt", ".pptx"),# documentos
                                (".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp"),                 # fotos
                                (".mp4", ".mkv", ".avi", ".mov", ".flv", ".divx"),                  # videos
                                (".mp3", ".aac", ".wav", ".aiff", ".wma", ".opus", ".ogg"),         # musica
                                (".py", ".rar", ".zip", ".html", ".tmp", ".dat", ".exe", ".deb", ".dmg", ".psd"), # otros
                            ]
    
    for carpetaNumero in range(0, len(carpetas)):
    
        ListaDeArchivos = asociar_carpetas_con_extensiones(carpetaNumero, extensionesdocumentos[carpetaNumero], ruta=ruta) 
        for archivo in ListaDeArchivos:
            try:
                print("[*] Moviendo el archivo ({}) a la carpeta ({})".format(archivo, carpetas[carpetaNumero]))
                shutil.move(archivo, carpetas[carpetaNumero])
            except shutil.Error:
                print("[!] El archivo {} \t ya existe en el directorio {}".format(archivo, carpetas[carpetaNumero]))
            
        


    