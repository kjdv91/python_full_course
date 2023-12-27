import shutil
import os
test = "Hola mme llamo Kevin"

# escribir archivo
try:
    with open('hello.txt','w') as file:
        file.write(test)

except FileNotFoundError as e:
    print(e)

# leer archivo
with open('hello.txt', 'r') as fileR :
    print(fileR.read())

# copiar archivo

shutil.copyfile('hello.txt','copy.txt')  # origen , destino se crea al ejecutar

# mover archivo
source = "copy.txt"
destino = "C:\\Users\\Kevin\\Documents\\"
try:
    if os.path.exists(destino):
        print("There is already a file there")
    else:
        os.replace(source,destino)
        print(source + "was moved")
except FileNotFoundError as e:
    print(source + "was not found")



# eliminar archivo
path3 = 'copy.txt'
try:

    os.remove(path3)
   # os.rmdi('name_carpeta')
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
else:
    print(path3 + " was a delete")