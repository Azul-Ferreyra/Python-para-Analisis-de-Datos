#----------------------------------------------ANZUR------------------------------------------------------------#
#################################################################################################################

import os
from colorama import init, Fore
from time import time
import numpy as np 

def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
from time import time

def pausa():
    input(Fore.RED + "\tPara iniciar presione una tecla, cualquiera: "+ Fore.RESET)
    

pausa()

#################################################################################################################


def flotantes():
    while len_.replace(".","",1).isdigit() is False :
        len_ = input ("Ingrese un numero flotante: ")
    print (f"ok {float(len_)}")
    len_ = len_.replace(".","",1)
    len_=float(len_)
#-----------------------------------------------------------------
def int_neg():
    while len_.replace("-","",1).isdigit() is False :
        len_ = input ("Ingrese un número negativo: ")
    print (f"ok {int(len_)}")
    len_=int(len_)
#-----------------------------------------------------------------
def float_neg():
    while len_.replace(".","",1).replace("-","",1).isdigit() is False :
        len_ = input ("Ingrese un flotante negativo: ")
    print (f"ok {float(len_)}")
    len_=float(len_)
    # ~ len_.replace(".","",1).replace("-","",1).isdigit()
    # ~ len_.isdigit().replace(".","",1).replace("-","",1)
    # ~ len_.replace(".","",1).isdigit().replace("-","",1)

#################################################################################################################
#Ejercicio 1
def creador(): # crea la matriz NxN que necesitamos
    len_=""
    while not len_.isdigit():
        len_ = input ("ingrese la cantidad de filas/columnas:")
    len_ = int(len_)
    valor=0
    matriz_empty=[]
    for index_f in range (0, len_):
        vector_empty=[]
        for index_c in range (0, len_):
            vector_empty.append(0)
        matriz_empty.append(vector_empty)
    #------------------------------------------------
    del matriz_empty
    vector_empty = [0 for _ in range (0, len_)]
    matriz_empty = [vector_empty for _ in range (0, len_)]
    #------------------------------------------------
    #           listas por comprehension
    matriz_empty = [[0 for _ in range (0, len_)] for _ in range (0, len_)]
    print (matriz_empty, len(matriz_empty))


    return matriz_empty
    
#################################################################################################################     
def cargador(matriz_empty): # carga la matriz NxN
    # ~ len_f=len(matriz_empty)
    # ~ len_c=len(matriz_empty[0])
    matriz= matriz_empty.copy()
    for index_f in range (0, len(matriz_empty)):
        for index_c in range (0, len(matriz_empty[index_f])):
            entrada=""
            while not entrada.isnumeric():
                entrada= input (f"ingrese el valor para ({index_f},{index_c}):")
            entrada=int(entrada)
            matriz[index_f][index_c]=entrada
        print ("-"*20)

    return matriz
################################################################################################################# 
def check(matriz):
    len_=len(matriz)
    """
    temp_f=[]
    for index_f in range(0, len(matriz)):
        temp_f.append(sum(matriz[index_f]))
    print (f"filas = {temp_f}")
    #--------------------------------------------
    temp_c=[]
    for index_f in range(0, len(matriz)):
        # ~ print (matriz[index_f])
        vertor_c=[]
        for index_c in range(0, len(matriz)):
            # ~ print (f"en {index_c=} x {index_f=}   {matriz[index_c][index_f]}")
            vertor_c.append(matriz[index_c][index_f])
        # ~ print ("-"*50)

        temp_c.append(sum(vertor_c))
    print (f"columnas = {temp_c}")
    #--------------------------------------------
    temp_d=[]
    vertor_d=[]
    for index_f in range(0, len(matriz)):

        print (f"en {index_f=} x {index_f=}   {matriz[index_f][index_f]}")
        vertor_d.append(matriz[index_f][index_f])
    temp_d.append(sum(vertor_d))
    print (f"diagonal principal = {temp_d}")
    #--------------------------------------------
    vertor_d=[]
    for index_f in range(0, len(matriz)):

        print (f"en {index_f=} x { len(matriz)-1-index_f=}   {matriz[index_f][len(matriz)-1-index_f]}")
        vertor_d.append(matriz[index_f][len(matriz)-1-index_f])
    temp_d.append(sum(vertor_d))
    print (f"diagonal principal = {temp_d}")
    #--------------------------------------------
    """


    temp_f=[]
    temp_c=[]
    temp_d=[]
    vertor_dp=[]
    vertor_ds=[]
    for index_f in range(0, len(matriz)):
        temp_f.append(sum(matriz[index_f]))
    #--------------------------------------------
        vertor_c=[]
        for index_c in range(0, len(matriz)):
            vertor_c.append(matriz[index_c][index_f])
        temp_c.append(sum(vertor_c))
    #--------------------------------------------
        # ~ print (f"en {index_f=} x {index_f=}   {matriz[index_f][index_f]}")
        vertor_dp.append(matriz[index_f][index_f])
    #--------------------------------------------
        # ~ print (f"en {index_f=} x { len(matriz)-1-index_f=}   {matriz[index_f][len(matriz)-1-index_f]}")
        vertor_ds.append(matriz[index_f][len(matriz)-1-index_f])
    temp_d.append(sum(vertor_dp))
    temp_d.append(sum(vertor_ds))
    print (f"filas = {temp_f}")
    print (f"columnas = {temp_c}")
    print (f"diagonales  = {temp_d}")
    #--------------------------------------------
    if not ( all([True for cada in range (1,len(temp_f)) if temp_f[0]==temp_f[cada] ]) and \
        all([True for cada in range (1,len(temp_c)) if temp_c[0]==temp_c[cada] ]) and \
        temp_d[0]== temp_d[1] ):
        return (False,0)#algo es diferente por lo que no puede ser mágica
    """
    # lista por one line comprehension list (dict)
    check_list = [True for cada_index in range (1,len(temp_f)) if temp_f[0]==temp_f[cada_index] ]
    # True para cada_index en rango de 1 a cantidad de filas
    #    si vector en [cada_index] es igual vector [0]
    #para cada suma de filas en el temp_f si es igual a la que esta en 0
    all( check_list ) and \
        all([True for cada_index in range (1,len(temp_c)) if temp_c[0]==temp_c[cada_index] ]) and \


    temp_d[0]== temp_d[1] ):
    # puede haber n filas / columnas pero las diagonales siempres seran 2

    """
    if temp_f[0]== temp_c[0]==temp_d[0]:
        return (True,temp_f[0])
    else :
        return (False,0)


#################################################################################################################

def mostrar(matriz): # carga la matriz NxN
    print("\n"*5)
    for fila in matriz:
        print ("\t\t",fila)
    print("\n"*5)

pseudo_matrices ={1: [
                [4,3,8],
                [9,5,1],
                [2,7,6]
            ],
        2:[
                [8,1,6],
                [3,5,7],
                [4,9,2]
            ],
        3:[
                [16, 3, 2,13],
                [ 5,10,11, 8],
                [ 9, 6, 7,12],
                [ 4,15,14, 1]
            ],
        4:[
                [16, 2, 3,13],
                [ 5,11,10, 8],
                [ 9, 7, 6,12],
                [ 4,14,15, 1]
            ],
        5:[
                [ 4,14,15, 1],
                [ 9, 7, 6,12],
                [ 5,11,10, 8],
                [16, 2, 3,13]
            ],

        6: [
                [17,24, 1, 8,15],
                [23, 5, 7,14,16],
                [ 4, 6,13,20,22],
                [10,12,19,21, 3],
                [11,18,25, 2, 9]
            ],
        7: [
                [64, 2, 3,61,60, 6, 7,57],
                [ 9,55,54,12,13,51,50,16],
                [17,47,46,20,21,43,42,24],
                [40,26,27,37,36,30,31,33],
                [32,34,35,29,28,38,39,25],
                [41,23,22,44,45,19,18,48],
                [49,15,14,52,53,11,10,56],
                [ 8,58,59, 5, 4,62,63, 1]
            ]
        }

pseudo_matriz_a = [ [4,3,8], [9,5,1],[2,7,6]]

#################################################################################################################     
opcion=""
while opcion not in ["A", "S", "1","2","3","4","5","6","7"]:
    limpiar()
    opcion = input ("""Seleccione:
            A) para cargar matriz propia
            1 al 7) para cargar matriz registrada
            S) Salir
            : """).upper()
    if opcion =="A":
        matriz_empty=creador() # crea la matriz NxN que necesitamos
        matriz=cargador(matriz_empty) # carga la matriz NxN
        mostrar(matriz)
        salida= check(matriz)
    elif opcion in [str(n) for n in range(1,8)]:
        mostrar(pseudo_matrices[int(opcion)])
        start_time = time()
        salida=check(pseudo_matrices[int(opcion)])
        elapsed_time = time() - start_time
        print (f"Tiempo estimado de consulta {elapsed_time}")
    elif opcion =="S":
        print ("Adios")
        exit()
    else:
        print ("valor no válido")
        continue
    if salida[0] is True:
        print (f"es matriz magica y su numero magico es {salida[1]}")
    else:
        print ("no es matriz magica")
    input ("        Enter para continuar")
    opcion=""
