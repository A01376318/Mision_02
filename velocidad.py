# Autor: Elena Itzel Ramírez Tovar, A01376318
# Descripcion: Calcular distancias 1 y 2 y t basando en velocidad

# Escribe tu programa después de esta línea.
v=float(input("Ingrese la velocidad deseada en km/hr: "))
d1=float(6*v)
d2=float(3.5*v)
t=float(485/v)
print("A %0.1f km/hr usted recorrería..." %(v))
print("%0.1f kilómetros en 6 horas" %(d1))
print("%0.1f kilómetros en 3.5 horas" %(d2))
print("485 kilómetros en %0.1f horas" %(t))