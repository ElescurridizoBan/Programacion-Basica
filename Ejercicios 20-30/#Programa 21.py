#Programa 21
print("1.-Cubo")
print("2.-Cilindro")
print("3.-Esfera")

pi=3.14

numero=int(input("Digite que que figura quiere calcular:"))

if numero==1:
    lado=int(input("Ingrese cuanto miden los lados: "))

    area= 6*(lado*lado)
    volumen=lado*lado*lado

    print("El area del cubo es de: ",area)
    print("El volumen del cubo es de: ",volumen)

elif numero==2:
    radio=int(input("Ingrese el radio del cilindro: "))
    altura=int(input("Ingrese la altura del cilindro: "))

    area= 2*pi*radio(radio + altura)
    volumen=pi*(radio*radio)*altura

    print("El area del cilindro es de: ",area)
    print("El volumen del cilindro es de: ",volumen)

elif numero==3:
    radio=int(input("Ingrese el radio:"))

    area= 4*pi*(radio*radio)
    volumen= 4/3*pi*(radio*radio*radio)

    print("El area de la esfera es de: ",area)
    print("El volumen de la esfera es de: ",volumen)

else:
    print("Esa opcion no existe")
    