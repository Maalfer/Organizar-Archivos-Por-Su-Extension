import os
import shutil
import re

ruta = input("Introduce la ruta de la carpeta que quieras organizar: ")

def rutas(ruta):
    patron = r"\s+"
    carpeta = re.sub(patron, "", ruta)
    os.chdir(carpeta)
    if os.path.exists("fotos") == False:
        os.mkdir("documentos")
        os.mkdir("fotos")
        rutadocumentos = "documentos"
        rutafotos = "fotos"
        moverdoc(carpeta, rutadocumentos, rutafotos)
    else:
        rutadocumentos = "documentos"
        rutafotos = "fotos"
    moverdoc(carpeta, rutadocumentos, rutafotos)

def moverdoc(carpeta, rutadocumentos, rutafotos):
    documentos = r".pdf", r".doc", r".docx", r".txt", r".odt"
    moverdocumentos = [_ for _ in os.listdir(carpeta) if _.endswith(documentos)]

    for i in moverdocumentos:
        shutil.move(carpeta + i, rutadocumentos)
    moverfotos(carpeta, rutafotos)


def moverfotos(carpeta, rutafotos):
    fotos = r".png", r".jpeg", r".jpg", r".gif"
    moverfotos = [_ for _ in os.listdir(carpeta) if _.endswith(fotos)]

    for i in moverfotos:
        shutil.move(carpeta + i, rutafotos)


rutas(ruta)