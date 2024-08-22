lis= ["franklin",20,5.0]

#nos devueleve la cantidad de caracteres

cadena= "hola"
resultado=len(cadena)
print(resultado)

#agregar un elemento a lista
lis.append("EDWARD")
#se agrega a un campo
lis.insert(1,"mayo")
lis.extend(["Nariño","Pasto","2024"])
print(lis)
#listas
lista1=list([2,20,1,5,6,7,10,9])
lista1.sort()
lista1.sort(reverse=True)
elemento_encontrado=lista1.index(10)
print(lista1)
print(elemento_encontrado)