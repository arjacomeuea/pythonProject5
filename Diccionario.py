# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Angel",
    "edad": 36,
    "ciudad": "Puyo",
    "profesion": "Policia"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Puyo"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Policia"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0981083148"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal actualizada:")
print(informacion_personal)