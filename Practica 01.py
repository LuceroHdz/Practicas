# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#Escriban un script que reciba un nu´mero n y sume todos los nu´meros 
#enteros de 1 hasta n (incluido).

n=input("Escribe un numero aqui> ")
n=int(n)
print(n)
suma=0
for x in range(1,n+1):
    suma=x+suma
print(" La suma  es", suma)
  
 #Escriban un programa que reciba una entrada de texto desde el teclado y 
 #sustituya todas las vocales de la oración según
 #las reglas del Lenguaje de la F:
Texto=input("Ingrese la frase")
tex=Texto.replace("a","afa")
tex1=tex.replace("á","áfa")
tex2=tex1.replace("e", "efe")
tex3=tex2.replace("é", "éfe")
tex4=tex3.replace("i", "ifi")
tex5=tex4.replace("í", "ífi")
tex6=tex5.replace("ó", "ófo")
tex7=tex6.replace("o", "ofo")
tex8=tex7.replace("u", "ufu")
tex9=tex8.replace("ú", "úfo")
print(tex9)


