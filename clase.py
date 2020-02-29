# Autor: Elena Itzel Ramírez Tovar
# Descripcion: Calcular porcentaje de alumnos por sexo

# Escribe tu programa después de esta línea.
m=int(input("Ingrese el número de estudiantes de sexo masculino: "))
f=int(input("Ingrese el número de estudiantes de sexo femenino: "))
t=m+f
pm=float((m*100)/t)
pf=float((f*100)/t)
print("Para un grupo de %d estudiantes, los porcentajes por sexo son: " %(t))
print("Femenino: %%%0.2f" %(pf))
print("Masculino: %%%0.2f" %(pm))
