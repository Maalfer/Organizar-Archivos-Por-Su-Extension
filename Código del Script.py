import os
import shutil
import re
from tkinter import messagebox as MessageBox
from tkinter import *


def rutas():
    result=escribirrutas.get()
    patron = r"\s+"
    carpeta = re.sub(patron, "", result)
    os.chdir(carpeta)
    while(True):
        
        if os.path.exists("documentos") == True:
            pass
        else: 
            os.mkdir("documentos")
            continue
        
        if os.path.exists("fotos") == True:
            pass
        else:
            os.mkdir("fotos")
            continue
            
        if os.path.exists("videos") == True:
            pass
        else:
            os.mkdir("videos")
            continue
            
        if os.path.exists("otros") == True:
            pass
        else:
            os.mkdir("otros")
        break
                  
    rutadocumentos = "documentos"
    rutafotos = "fotos"
    rutavideos = "videos"
    rutaotros = "otros"
    moverdoc(carpeta, rutadocumentos, rutafotos, rutavideos, rutaotros)

def moverdoc(carpeta, rutadocumentos, rutafotos, rutavideos, rutaotros):
    documentos = r".pdf", r".doc", r".docx", r".txt", r".odt"
    moverdocumentos = [_ for _ in os.listdir(carpeta) if _.endswith(documentos)]

    for i in moverdocumentos:
        shutil.move(carpeta + i, rutadocumentos)
    moverfotos(carpeta, rutafotos, rutavideos, rutaotros)


def moverfotos(carpeta, rutafotos, rutavideos, rutaotros):
    fotos = r".png", r".jpeg", r".jpg", r".gif"
    moverfotos = [_ for _ in os.listdir(carpeta) if _.endswith(fotos)]

    for i in moverfotos:
        shutil.move(carpeta + i, rutafotos)
    movervideos(carpeta, rutavideos, rutaotros)

def movervideos(carpeta, rutavideos, rutaotros):
    videos = r".mp4", r".avi", r".mkv", r".mov", r".wmv"
    movervideos = [_ for _ in os.listdir(carpeta) if _.endswith(videos)]

    for i in movervideos:
        shutil.move(carpeta + i, rutavideos)
    moverotros(carpeta, rutaotros)

def moverotros(carpeta, rutaotros):
    otros = r".exe", r".py", r".zip", r".rar", r".html"
    moverotros = [_ for _ in os.listdir(carpeta) if _.endswith(otros)]

    for i in moverotros:
        shutil.move(carpeta + i, rutaotros)

def popup():
    MessageBox.showinfo("Sobre mí","Enlace a mi perfil de LinkedIn:\nhttps://www.linkedin.com/in/maalfer1/")

def ayuda():
    MessageBox.showinfo("Instrucciones de uso", "Para utilizar este programa sólo tienes que copiar y pegar la ruta de la carpeta que quieras organizar. Por ejemplo usando este formato C:/Users/mario/Desktop/Trabajo/ ")


root = Tk()
root.config(bd=15)
root.title("Script para organizar una carpeta")

imagen = PhotoImage(file="disco.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Para más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor",command=popup)
menubar.add_cascade(label="Clic para las instrucciones de Uso", command=ayuda)
menubar.add_command(label="Salir", command=root.destroy)


instrucciones = Label(root, text="Programa creado en Python para ordenar archivos automáticamente\nInserte la ruta de la carpeta que quieras organizar\n")
instrucciones.grid(row=0, column=1)

escribirrutas = Entry(root)
escribirrutas.grid(row=1, column=1)

boton = Button(root, text="Clícame para organizar tu carpeta :)", command=rutas)
boton.grid(row=2, column=1)

root.mainloop()



