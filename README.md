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

- En caso de que usted use Windows y no tenga Python instalado:
```batch
start Orden.exe
```


----