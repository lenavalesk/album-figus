# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:50:05 2019

@author: LenaP
"""

import random
import numpy as np

def main():
    figus_en_album = input("Ingrese la cantidad de figuritas en album:")
    Nrep = input("Ingrese la cantidad de intentos de llenado:")
    figus_paquete = input("Ingrese la cantidad de figuritas por paquete:" )
    repes = input("Ingrese la cantidad de repeticiones con paquetes para llenar: ")
    
    
    if (not figus_en_album):
        figus_en_album = 669
    if (not Nrep):
        Nrep = 10
    if (not figus_paquete):
        figus_paquete = 5
    if (not repes):
        repes = 100
        
        
        
    figus_en_album = int(figus_en_album)
    Nrep = int(Nrep)
    figus_paquete = int(figus_paquete)
    repes = int(repes)
    
    compra_figus_para_llenar = cantidad_figu(figus_en_album)
    promedio_intentos = mean_intentos_llenado(figus_en_album, Nrep)
    armado_paquete = paquete(figus_en_album, figus_paquete)
    paquetes_para_llenar = paquetes_llenado(figus_paquete, figus_en_album) 
    promedio_intentos_paquete = promedio_paquetes_llenado(figus_paquete, figus_en_album, repes)
    
    
    
    print("Para llenar el album compro esta cantidad de figuritas: ", (compra_figus_para_llenar))
    print ("\n")
    print("En promedio hay que comprar esta cantidad de figuritas: ", (promedio_intentos))
    print ("\n")
    print("Un paquete que compre es: ", (armado_paquete))
    print ("\n")
    print ("Para llenar el album compro esta cantidad de paquetes: ", (paquetes_para_llenar))
    print ("\n")
    print("El promedio de las repeticiones para llenar el album con paquetes:", (promedio_intentos_paquete))
    
    
    
    
def generar_figurita(n):
    return random.randint(1, n)

def cantidad_figu(figus_en_album):
    album = []
    count = 0
    while len(album) != figus_en_album:
        figurita = generar_figurita(figus_en_album)
        if figurita not in album:
            album.append(figurita)
        count = count + 1
        

       
    return count


#figus_en_album = 100 
    
#intentosllenaralbum = cantidad_figu(figus_en_album)
#print(intentosllenaralbum)

def mean_intentos_llenado(figus_en_album, Nrep):
    intentos = []
    
    for i in range (1, Nrep):
        results = cantidad_figu(figus_en_album)
        intentos.append(results)
    return    np.mean(intentos)

#Nrep = 

#mean = mean_intentos_llenado(figus_en_album)
#print(mean)



def paquete(figus_en_album, figus_paquete):
    paqueten = []
    for i in range (figus_paquete):
        figurita = generar_figurita(figus_en_album)
        paqueten.append(figurita)
    return paqueten
    
#figus_paquete = 5
#
#paquetex = paquete(figus_en_album, figus_paquete)
#print(paquetex)

#def paquete2 (m):
#    paqueten = []
#    while len(paqueten) < m :
#        results = generar_figurita(figus_en_album)
#        paqueten.append(results)
#    return paqueten
#
#
#m = 5
#paquetey = paquete2 (m)
#print(paquetey)

def paquetes_llenado (figus_paquete, figus_en_album):
    llenado = []
    count = 0
    while len(llenado) != figus_en_album:
        compro_paquete = paquete(figus_en_album, figus_paquete)
        for i in compro_paquete:
            if i not in llenado:
                llenado.append(i)
            
        count = count + 1
    return count

def promedio_paquetes_llenado (figus_paquete, figus_en_album, repes):
    llenando_album = []
    for i in range (1, repes):
        resluts = paquetes_llenado(figus_paquete, figus_en_album)
        
        llenando_album.append(resluts)
    return np.mean(llenando_album)
    




main()






        








        








        
        




    
    



    















    
    
    

