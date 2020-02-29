# Autor: Elena Itzel Ramírez Tovar, A0137638
# Descripcion: Calcular cuenta con propina e IVA

# Escribe tu programa después de esta línea.
sub=float(input("Ingrese el total de su cuenta: "))
P=float(sub*0.13)
IVA=float(sub*0.16)
T=float(sub+P+IVA)
print("Para una cuenta de$ %0.2f, corresponde: " %(sub))
print("PROPINA: $%0.2f" %(P))
print("IVA: $%0.2f" %(IVA))
print(" TOTAL A PAGAR: $%0.2f" %(T))