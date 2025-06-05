#Escribe un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de galones de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro

kilometros = float(input("¿Cuántos kilómetros recorriste en motocicleta?: "))
galones = float(input("¿Cuánto galones consumiste en ese recorrido?: "))
consumo = kilometros / galones
if kilometros > 0:
  print(f"El consumo de combustible por kilómetro fue de: {consumo} galones p/km.")
else:
  print("Los kilometros recorridos deben ser mayor de cero.")