# Ejercicio calculadora BMI:

# Pide al usuario que ingrese su peso en kilogramos y su altura en metros.
# Calcula y muestra su BMI utilizando la fórmula: BMI = Peso / (Altura^2).
# Luego, clasifica el BMI en las categorías: "Bajo peso", "Normal", "Sobrepeso" u "Obeso"
# según los siguientes rangos:

# BMI menor que 18.5 => Bajo peso
# BMI mayor o igual que 18.5 y menor que 24.9 => Peso normal
# BMI mayor o igual que 24.9 y menor que 29.9 => Sobrepeso
# BMI mayor que 29.9 => Obeso



peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el BMI 
bmi = peso / (altura ** 2)

if bmi < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= bmi < 24.9:
    categoria = "Peso normal"
elif 24.9 <= bmi < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obeso"

# Mostrar el BMI y la categoría correspondiente
print(f"Tu BMI es: {bmi:.2f}")
print(f"Categoría: {categoria}")
