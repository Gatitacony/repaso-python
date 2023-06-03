# obtener informacion del usuario a traves del teclado.
# title le agrega la mayus al nombre. upper pone todo en mayuscula. lower pone todo en minusculas.  
name = input (" dime tu nombre: ")
print (f"hola {name.title()}")
print (f"hola {name.upper()}")
print (f"hola {name.lower()}")
# La función input SIEMPRE entrega texto, si queremos pasar a número (int), debemos usar la transformación con la función int()
age = int (input ("dime tu edad: "))

print (f"{name} en un año mas tendras {age + 1}")