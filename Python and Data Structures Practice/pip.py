import os

def checkforfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def movethem(foldername, files):
    for file in files:
        os.replace(file, f'{foldername}/{file}')

files = os.listdir()
checkforfolder("Images")
checkforfolder("Docs")
checkforfolder("HTML files")
checkforfolder("Others")
checkforfolder("Python DS Practice")

imgExt = ['.jpeg','.jpg','.png',]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt ]

docExt = ['.doc','.docx','.txt','.pdf']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt ]

htmlExt = ['.html','.HTML']
html= [file for file in files if os.path.splitext(file)[1].lower() in htmlExt ]

pyExt = ['.py','.PY']
py = [file for file in files if os.path.splitext(file)[1].lower() in pyExt]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExt) and (ext not in docExt) and (ext not in htmlExt) and os.path.isfile(file):
        others.append(file)
print(others)

movethem("Images",images)
movethem("Docs",docs)
movethem("HTML files",html)
movethem("Others",others)
movethem("Python DS Practice",py)