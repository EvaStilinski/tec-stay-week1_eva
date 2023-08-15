#Definición de variables
name = "John"  # Nombre del individuo
age = 25  # Edad del individuo
is_student = True  # Indicador de si es estudiante o no

#Operaciones matemáticas
a = 10
b = 5

#Suma
result_add = a + b
print("Addition:", result_add)  # Salida: 15

#Resta
result_sub = a - b
print("Subtraction:", result_sub)  # Salida: 5

#Multiplicación
result_mul = a * b
print("Multiplication:", result_mul)  # Salida: 50

#División
try:
    result_div = a / b
    print("Division:", result_div)  # Salida: 2.0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")

#Arreglos (listas)
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)  # Salida: ["apple", "banana", "orange"]

#Diccionarios (pares clave-valor)
person = {"name": "John", "age": 25, "is_student": True}
print("Person:", person)  # Salida: {"name": "John", "age": 25, "is_student": True}

#Operaciones en arreglos
fruits.append("grape")  # Agregar "grape" al arreglo
print("Updated Fruits:", fruits)  # Salida: ["apple", "banana", "orange", "grape"]

#Operaciones en diccionarios
person["location"] = "New York"  # Agregar una nueva clave-valor al diccionario
print("Updated Person:", person)  # Salida: {"name": "John", "age": 25, "is_student": True, "location": "New York"} 
#Declaración condicional (if)
x = 10
if x > 5:
    print("x is greater than 5")  # Salida si x > 5
elif x == 5:
    print("x is equal to 5")  # Salida si x = 5
else:
    print("x is less than 5")  # Salida en otros casos

#Bucle "for each" (usando el bucle for)
for fruit in fruits:
    print(fruit)  # Salida: "apple", "banana", "orange", "grape"


#Bucle "while"
count = 0
while count < 5:
    print("Count:", count)  # Salida de los valores de 'count' mientras sea menor que 5
    count += 1

#Apertura de un archivo usando un administrador de contexto
filename = "example.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File Content:", content)  # Mostrar el contenido del archivo
except FileNotFoundError:
    print(f"Error: Archivo '{filename}' no encontrado.")

#Declaraciones de impresión
print("Name:", name, "Age:", age)  # Mostrar nombre y edad

#interpolación de cadenas usando f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")  # Mostrar nombre y edad utilizando f-strings