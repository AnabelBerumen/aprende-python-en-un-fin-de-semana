print("#####################\n")
try:
    print(3/0)
except:
    print("ERROR: División por cero\n")

print("#####################\n")

print("Iniciando programa")
try:
    print(3/0)
except:
    print("ERROR: División erronea")
finally:
    print("Programa acabado\n")
print("#####################\n")

print("Iniciando programa")
try:
    print(3/1)
except:
    print("ERROR: División erronea")
finally:
    print("Programa acabado\n")
print("#####################\n")

print("Iniciando programa")
try:
    print(3/1)
except:
    print("ERROR: División erronea")
else:
    print("No se han producido errores")
finally:
    print("Programa acabado\n")
print("#####################\n")

print("Iniciando programa")
try:
    print(3/0)
except ZeroDivisionError:
    print("ERROR: Divisón por cero")
except:
    print("Error general")
else:
    print("No se han producido errores")
finally:
    print("Programa acabado\n")
print("#####################\n")