from os import mkdir, listdir
from os.path import exists, isfile
from shutil import move, Error
from argparse import ArgumentParser
try:
    from colorama import init
except ModuleNotFoundError:
    """
        Si el modulo colorama no esta instalado, se instalara acontinuacion:
    """
    from os import system
    print("[!] Al parecer usted no tiene colorama instalado, ahora se lo instalaremos")
    print("[!] Mediante un \"pip install colorama\"")
    system("pip install colorama")
    from colorama import init
    
    
    
init() # iniciamos colorama

class COLOR:
          
    def __init__(self):
       
        self.BLACK           =  "\033[30m"
        self.RED             =  "\033[31m"
        self.GREEN           =  "\033[32m"
        self.YELLOW          =  "\033[33m"
        self.BLUE            =  "\033[34m"
        self.MAGENTA         =  "\033[35m"
        self.CYAN            =  "\033[36m"
        self.WHITE           =  "\033[37m"
        self.RESET           =  "\033[39m"

        self.LIGHTBLACK_EX   =  "\033[90m"
        self.LIGHTRED_EX     =  "\033[91m"
        self.LIGHTGREEN_EX   =  "\033[92m"
        self.LIGHTYELLOW_EX  =  "\033[93m"
        self.LIGHTBLUE_EX    =  "\033[94m"
        self.LIGHTMAGENTA_EX =  "\033[95m"
        self.LIGHTCYAN_EX    =  "\033[96m"
        self.LIGHTWHITE_EX   =  "\033[97m"

    def UP(self, n=1):
        return '\033[' + str(n) + 'A'
    def DOWN(self, n=1):
        return '\033[' + str(n) + 'B'
    def FORWARD(self, n=1):
        return '\033[' + str(n) + 'C'
    def BACK(self, n=1):
        return '\033[' + str(n) + 'D'
    def POS(self, x=1, y=1):
        return '\033[' + str(y) + ';' + str(x) + 'H'
    def SET_TITLE(self, text):
        return "\033]2;{}\007".format(text)
    def CLEAR(self):
        return "\033[3J\033[H\033[2J"
    def POINTGREEN(self, text1="", text2=""):
        return self.LIGHTGREEN_EX+"["+self.BLUE+"*"+self.LIGHTGREEN_EX+"] "+self.LIGHTWHITE_EX+text1+text2+self.LIGHTWHITE_EX
    def POINTRED(self, text=""):
        return self.LIGHTYELLOW_EX+"["+self.RED+"*"+self.LIGHTYELLOW_EX+"] "+self.LIGHTMAGENTA_EX+text+"\n"+self.LIGHTWHITE_EX



__version__ =  2.0
__autor__   =  "Mario"
__github__  =  "https://github.com/Maalfer?tab=repositories"
__doc__     =  "Script para organizar archivos en diferentes "
__doc__    +=  "carpetas según la extensión que tengan"


def crear_carpetas_si_no_existe(carpetas, ruta="./"):
    """
        Esta funcion recibe en forma de lista, las carpetas a crear
        si no existen. Ejemplo de uso:

            carpetas = ["documentos", "fotos"]
            crear_carpetas_si_no_existe(carpetas)

        Esto comprueba si exite la carpeta documentos y la carpeta fotos,
        en caso contrario, la crea
    """
    _COLOR = COLOR()
    BannerInformativo = "{}[{}*{}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTRED_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTYELLOW_EX)
    for carpeta in carpetas:
        if exists(ruta+carpeta) != True:
            # si la carpeta no existe exists() retorna False lo cual es diferente a True
            #  y esta condicion se llevara a cabo
            mkdir(ruta+carpeta)
            print("{} Creando la carpeta -> {}".format(BannerInformativo, carpeta))
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

def asociar_carpetas_con_extensiones(nombre_carpeta, extensiones_de_archivos, ruta=".", ArchivosExcepciones=[]):
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
        if archivo.endswith(extensiones_de_archivos) == True and archivo not in ArchivosExcepciones and isfile(ruta+archivo):
            """"
                "archivo not in ArchivosExcepciones" comprueba que nuestro archivo no esta
                en la lista de ArchivosExcepciones, en caso de que lo este, este archivo no
                se agrega a la lista de ArchivosParaEstaCarpeta, ya que no queremos mover los
                archivos que se contiene en ArchivosExcepciones.
                isfile() comprueba que sea un archivo y un carpeta, pues si hay una carpeta que
                lleve en su nombre alguna extension, el programa generar un error.
            """
            ArchivosParaEstaCarpeta.append(ruta+archivo)
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

    parse = ArgumentParser() # Realizamos una instancia de la clase ArgumentParser
    
    # creamos parametros para nuestro script, si no se usan, usaremos datos por defectos:
    parse.add_argument("-rf", "--directoryFile", help="se le indica la ruta donde se encuentran los archivos que queremos organizar.", type=str, default="./")
    parse.add_argument("-ro", "--directoryOutput", help="Se le indica la ruta donde se creara las carpetas y se ordenara los elementos en ellas.", type=str, default="./")

    # parseamos los parametros del programa para poder usarlos
    parse = parse.parse_args()
    # Los valores por defecto son la ruta "./", es decir, el directorio actual.
    
    
    # Aqui hacemos una instancia a la clase COLOR para poder usar colores en nuestros print:
    _COLOR = COLOR()
    BannerAlerta = "{}[{}!{}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTMAGENTA_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTWHITE_EX)
    BannerInformativo = "{}[{}*{}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTRED_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTYELLOW_EX)
    BannerOtros = "{}[{}${}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTBLUE_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTWHITE_EX)
    
    """
        En esta lista metemos los archivos especiales que no queremos mover, como es el caso
        de nuestro script. __file__ almacena como valor el nombre de este script, por lo que
        si cambiamos el nombre de este archivo, esta variable se encargara de poner su valor
        correspondiente
    """
    ArchivosExcepciones = [__file__.split("\\")[-1], "requirements.txt"]
    """
        __file__ = 'C:\\Users\\Usuario\\Documents\\GitHub\\Organizar-Archivos-Por-Su-Extension\\Orden.py'
    
        >>> archivo = __file__.split("\\")
        >>> print(archivo)
        ['C:', 'Users', 'Usuario', 'Documents', 'GitHub', 'Organizar-Archivos-Por-Su-Extension', 'Orden.py']
        >>> print(archivo[-1])
        "Orden.py"
        
    """


    carpetas = ["documentos", "fotos", "videos", "musica", "otros"]
    crear_carpetas_si_no_existe(carpetas, ruta=parse.directoryOutput)
    # crea las carpetas necesarias
    
    extensionesdocumentos = [   
                                (".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".ppt", ".pptx"),# documentos
                                (".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp"),                 # fotos
                                (".mp4", ".mkv", ".avi", ".mov", ".flv", ".divx"),                  # videos
                                (".mp3", ".aac", ".wav", ".aiff", ".wma", ".opus", ".ogg"),         # musica
                                (   
                                    ".py", ".rar", ".zip", ".html", ".tmp", ".dat", ".exe", ".deb", 
                                    ".dmg", ".psd", ".c", ".asm", ".java", ".rst"
                                ), # otros
                            ]
    
    for carpetaNumero in range(0, len(carpetas)):
        """
            Con este bucle, asociamos las carpetas y las extensiones mediante un indice.
            Este bucle se repetira tantas veces como carpetas alla en la lista. y ira guardando
            valores de tipo int en la variable carpetaNumero.
        """
        
        ListaDeArchivos = asociar_carpetas_con_extensiones(carpetaNumero, extensionesdocumentos[carpetaNumero], ruta=parse.directoryFile, ArchivosExcepciones=ArchivosExcepciones) 
        print("{} Archivos a guardar en la carpeta {}, en total un cantidad de {}:".format(BannerOtros, carpetas[carpetaNumero], len(ListaDeArchivos)))
        print("\n".join(ListaDeArchivos))
        """
            Aqui imprimimos los archivos que se van a guardar en la carpeta,
        """
        
        
        for archivo in ListaDeArchivos:
            """
                este bucle, mueve los archivos del directorio que se desea a las carpetas creadas o ya
                existentes que se especificaron
            """
            try:
                print("{} Moviendo el archivo ({}) a la carpeta ({})".format(BannerInformativo, archivo, carpetas[carpetaNumero]))
                move(archivo, parse.directoryOutput+carpetas[carpetaNumero])
            except Error:
                print("{} El archivo {} \t ya existe en el directorio {}".format(BannerAlerta, archivo, carpetas[carpetaNumero]))
            
        


    