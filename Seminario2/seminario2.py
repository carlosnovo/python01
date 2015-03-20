# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#GRUPO 33

#Francisco Jose Macias Periñan
#Carlos Alberto Novo Foncubierta

#Programa que muestra la cadena mas larga posible de concatenar de una lista de palabras

def palabra_en_lista(palabra, lista, tamanno_lista): #comprueba si la palabra esta en la lista de concatenacion
    i = 0
    tam = len(lista)
    while i<tamanno_lista:
        if (tam == 0): #si la lista esta vacia
            return False #la palabra no se encuentra en la lista y devuelve FALSO
        elif (palabra == lista[i]):  #si la palabra esta en la lista de concatenacion
            return True     #devuelve VERDADERO si la palabra esta en la lista
        i = i+1
    return False            #devuelve falso si la palabra no esta en la lista

def concatenar(palabra1, palabra2): #comprueba si la ultima letra de la palabra1 es igual a la primera de la palabra2
    longitud1 = len(palabra1)
    if palabra1[longitud1-1] == palabra2[0]:
        return True                 #devuelve verdadero si se puede concatenar
    else:
        return False                #devuelve falso si no se puede concatenar



fichero = open('pokemon.txt', 'r') #abro el fichero
contenido = fichero.read().split() #convierto el fichero en una lista
tamanno_contenido = len(contenido)     #calculo el tamaño de la lista
print "El archivo txt tiene ", tamanno_contenido, " palabras"
lista = []
listaDefinitiva = []
palabra = ""
i = 0
j = 0
while (i<tamanno_contenido):
    if (len(lista) == 0):
        palabra = contenido[i]
        lista.append(palabra)
    while (j<tamanno_contenido):
        tamanno_lista = len(lista)
        if (palabra_en_lista(contenido[j], lista, tamanno_lista) == False): #si la palabra NO se encuentra en la lista provisional
                if (concatenar(palabra, contenido[j]) == True): #si puedo concatenar las dos palabras
                    palabra = contenido[j]
                    lista.append(palabra) #añado la palabra a la lista provisional
        j = j+1 #incremento j
    if len(listaDefinitiva) < len(lista): #si la lista que acabo de obtener es de mayor longitud que la definitiva
        print "Tamaño listaDefinitiva: ", len(listaDefinitiva), "Tamaño lista: ", len(lista)
        listaDefinitiva = lista[:] #guardo en listaDefinitiva la lista provisional
    j = 0               #inicializo de nuevo la variable para volver a recorrer la lista
    i = i+1         #incremento i
    del lista[:]  #vacio la lista provisional
tamanno_definitiva = len(listaDefinitiva)
print "La mayor lista encontrada tiene longitud ", tamanno_definitiva, "formada por las siguientes palabras: "
print listaDefinitiva

            
        
    

