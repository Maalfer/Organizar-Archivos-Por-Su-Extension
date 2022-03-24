import os
import glob
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



# Extensiones de fotos:

png = glob.glob("*.png")
jpg = glob.glob("*.jpg")
jpeg = glob.glob("*.jpeg")

# Extensiones de vídeos:

mp4 = glob.glob("*.mp4")
mkv = glob.glob("*.mkv")
avi = glob.glob("*.avi")
mov = glob.glob("*.mov")
divx = glob.glob("*.divx")

# Extensiones de audios:

wav = glob.glob("*.wav")
mp3 = glob.glob("*.mp3")
aac = glob.glob("*.aac")
aiff = glob.glob("*.aiff")
wma = glob.glob("*.wma")
flv = glob.glob("*.flv")

# Extensiones de documentos:

pdf = glob.glob("*.pdf")
doc = glob.glob("*.doc")
docx = glob.glob("*.docx")
odt = glob.glob("*.odt")
txt = glob.glob("*.txt")

# Extensiones de otros:

py = glob.glob("*.py")
rar = glob.glob("*.rar")
zip = glob.glob("*.zip")
exe = glob.glob("*.exe")

#############################################################

# Mover archivos (fotos)
for i in (png):
    shutil.move(i, "fotos")
for i in (jpg):
    shutil.move(i, "fotos")
for i in (jpeg):
    shutil.move(i, "fotos")


# Mover archivos (videos)
for i in (mp4):
    shutil.move(i, "videos")
for i in (mkv):
    shutil.move(i, "videos")
for i in (avi):
    shutil.move(i, "videos")
for i in (mov):
    shutil.move(i, "videos")
for i in (flv):
    shutil.move(i, "videos")
for i in (divx):
    shutil.move(i, "videos")

# Mover archivos (audios)
for i in (mp3):
    shutil.move(i, "musica")
for i in (aac):
    shutil.move(i, "musica")
for i in (wav):
    shutil.move(i, "musica")
for i in (aiff):
    shutil.move(i, "musica")
for i in (wma):
    shutil.move(i, "musica")

# Mover archivos (documentos)
for i in (pdf):
    shutil.move(i, "documentos")
for i in (doc):
    shutil.move(i, "documentos")
for i in (docx):
    shutil.move(i, "documentos")
for i in (txt):
    shutil.move(i, "documentos")
for i in (odt):
    shutil.move(i, "documentos")

# Mover archivos (otros)
for i in (py):
    shutil.move(i, "otros")
for i in (rar):
    shutil.move(i, "otros")
for i in (zip):
    shutil.move(i, "otros")