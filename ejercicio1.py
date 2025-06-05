#Escribe un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla. A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

var1 = int(input("Inserte el primer número: "))
var2= int(input("Inserte el segundo número: "))
resultado = var1 + var2
print(f"La suma es: {resultado}.")
var3 = int(input("Inserte un tercer número: "))
resultado2= resultado * var3
print(f"Multiplicando el resultado anterior con el número ingresado, el resultado es: {resultado2}.")