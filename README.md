# Script para ordenar archivos según la extensión que tengan.

Con este sencillo script podremos organizar los archivos que tengamos en una carpeta dependiendo de la extensión que tengan.

- Autor del codigo: [Mario](https://github.com/Maalfer)

----

### El funcionamiento es sl siguiente:

1. El script comprueba si existen las carpetas donde se enviarán los archivos, en caso de no encontrarlas, las crea.

2. Se comprueban las extensiones de todos los archivos uno por uno.

3. Se mueven los diferentes tipos de archivos en función de si son documentos, fotos, vídeos, música u otros tipos de archivos.

Este script es ideal para automatizar el ordenamiento de la carpeta de descargas y tener todo archivo descargado ordenado.

----
### Clonar con:
```batch
git clone https://github.com/desmonHak/Organizar-Archivos-Por-Su-Extension.git
```
y acceder a la carpeta con:
```batch
cd Organizar-Archivos-Por-Su-Extension
```
----

### Instalacion de librerias:

```batch
pip install -r requirements.txt
```

----

### Lectura del archivo README.md y LICENSE
- Para Windows:

```batch
type README.md | more
type LICENSE | more
```

- Para Linux:
```bash
cat README.md | more
cat LICENSE | more
```

----
### Ejecutar con:

```batch
python Orden.py
```

- En caso de que usted use Windows y no tenga `python` instalado:
```batch
start Orden.exe
```
----
### Como obtener ayuda del modulo:
para poder hacer esto, tenemos que abrir un interprete `python` en la carpeta donde se encuentra el archiv `Orden.py`, a continuacion importamos(`import Orden`) y realizamos un `help(Orden)`:

```python

>>> import Orden
>>> help(Orden)

Help on module Orden:

NAME
    Orden - Script para organizar archivos en diferentes carpetas según la extensión que tengan

CLASSES
    builtins.object
        COLOR

    class COLOR(builtins.object)
     |  Methods defined here:
     |
     |  BACK(self, n=1)
     |
     |  CLEAR(self)
     |
     |  DOWN(self, n=1)
     |
     |  FORWARD(self, n=1)
     |
     |  POINTGREEN(self, text1='', text2='')
     |
     |  POINTRED(self, text='')
     |
     |  POS(self, x=1, y=1)
     |
     |  SET_TITLE(self, text)
     |
     |  UP(self, n=1)
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    asociar_carpetas_con_extensiones(nombre_carpeta, extensiones_de_archivos, ruta='.', ArchivosExcepciones=[])
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

    crear_carpetas_si_no_existe(carpetas, ruta='./')
        Esta funcion recibe en forma de lista, las carpetas a crear
        si no existen. Ejemplo de uso:

            carpetas = ["documentos", "fotos"]
            crear_carpetas_si_no_existe(carpetas)

        Esto comprueba si exite la carpeta documentos y la carpeta fotos,
        en caso contrario, la crea

    listdir(path=None)
        Return a list containing the names of the files in the directory.

        path can be specified as either str, bytes, or a path-like object.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        If path is None, uses the path='.'.
        On some platforms, path may also be specified as an open file descriptor;\
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.

        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.

    mkdir(path, mode=511, *, dir_fd=None)
        Create a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

        The mode argument is ignored on Windows.

DATA
    __autor__ = 'Mario'
    __github__ = 'https://github.com/Maalfer?tab=repositories'

VERSION
    2.0

FILE
    c:\users\usuario\documents\github\organizar-archivos-por-su-extension\orden.py

```