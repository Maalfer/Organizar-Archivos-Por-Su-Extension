import os
import shutil

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
            continue
            
        if os.path.exists("musica") == True:
            pass
        else:
            os.mkdir("musica")
        break


extensionesdocumentos = r".pdf", r".doc", r".docx", r".txt",r".odt",r".xlsx",r".ppt",r"pptx"
documentos = [_ for _ in os.listdir() if _.endswith(extensionesdocumentos)]

for i in documentos:
    shutil.move(i, "documentos")



extensionesfotos = r".png", r".jpg", r".jpeg", r".gif",r".tiff", r".bmp"
fotos = [_ for _ in os.listdir() if _.endswith(extensionesfotos)]

for i in fotos:
    shutil.move(i, "fotos")



extensionesvideos = r".mp4", r".mkv", r".avi", r".mov",r".flv", r".divx"
videos = [_ for _ in os.listdir() if _.endswith(extensionesvideos)]

for i in videos:
    shutil.move(i, "videos")


extensionesmusica = r".mp3", r".aac", r".wav", r".aiff",r".wma",r".opus",r".ogg"
musica = [_ for _ in os.listdir() if _.endswith(extensionesmusica)]

for i in musica:
    shutil.move(i, "musica")


extensionesotros = r".py", r".rar", r".zip", r".html",r".tmp",r".dat",r".exe",r".deb",r".dmg"r".psd"
otros = [_ for _ in os.listdir() if _.endswith(extensionesotros)]

for i in otros:
    shutil.move(i, "otros")