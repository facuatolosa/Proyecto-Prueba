file = open("Archivo.txt","w")
print("Creando archivo...")
file.write("Archivo creado\n")
file.close()

file = open("Archivo.txt","r")
archivo = file.read()
print("Leyendo archivo...")
print(archivo)
file.close()

file = open("Archivo.txt","a")
print("Añadiendo texto al archivo...")
file.write("Texto añadido\n")
file.close()

file = open("Archivo.txt","r")
archivo = file.read()
print("Leyendo archivo...")
print(archivo)
file.close()

file = open("Archivo.txt","r+")
print("Lectura de las líneas del archivo")
print(file.readlines())
file.close()

file = open("Archivo.txt","r+")
print("\nAñadiendo texto en una posición determinada del sistema...")
texto = file.read()
pos_inicial = texto.find("\n")+1
prev_str = texto[0:pos_inicial]
next_str = texto[pos_inicial:len(texto)-1]
file.close()

file = open("Archivo.txt","w+")
file.write(prev_str+"Texto intermedio\n"+next_str)
file.close()

file = open("Archivo.txt","r+")
print(file.read())
file.close()