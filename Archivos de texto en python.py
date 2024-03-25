with open("my_notes.txt", "w") as file:
    # Escribir al menos tres líneas de notas personales
    file.write("Nota 1: Hoy es un buen día.\n")
    file.write("Nota 2: No olvidar comprar leche.\n")
    file.write("Nota 3: Recordar llamar a mamá esta tarde.\n")

# Lectura de archivo de texto
with open("my_notes.txt", "r") as file:
    # Leer el contenido del archivo línea por línea
    for line in file.readlines():
        # Mostrar en la consola cada línea leída
        print(line.strip())  # Utilizamos strip() para eliminar espacios en blanco y saltos de línea

# Cierre de archivos (no es necesario debido al uso de 'with', pero es buena práctica)
# El archivo se cerrará automáticamente cuando salgamos del bloque 'with'
