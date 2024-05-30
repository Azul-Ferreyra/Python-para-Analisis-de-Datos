
#--------------------------------------PSEUDO MATRIZ------------------------------------------------------------#
#################################################################################################################

import os
from colorama import init, Fore
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

def crear():
    len_ = ""
    while len_.isdigit() is False or int(len_) <3:
        len_ = input("Ingrese el 'len' de la matriz(>=3): ")
    print (f"Bien {int(len_)}")
    
    len_=int(len_)
    return len_
#Pedimos un numero lo convertimos a entero y lo devolvemos 
#################################################################################################################

def cargar(len_):
    matriz = list()
    dim = range(0,len_)
    for index_fila in dim:
        vector = list()
        for index_col in dim:
            dato=""
            while dato.isdigit() is False:
                dato = input(f"Ingrese el valor de la fila {index_fila+1} columna{index_col+1} : ")
                vector.append(int(dato))
        matriz.append(vector)
    return matriz

# cargamos la matriz, la matriz de la dimension es len, la matriz es cuadrada por eso realizamos dos bucles          
#################################################################################################################

def mostrar(matriz):
    dim = range(0,len(matriz))
    print(f"+{'----+'*(len(matriz)-1)}----+")
    for index_fila in  dim:
        for index_col in  dim:
            valor  = matriz[index_fila][index_col]
            caracteres = str(valor)
            if len(caracteres)==1:
               caracteres=f" {caracteres} "
            elif len(caracteres)==2:
               caracteres=f" {caracteres}"
            else:#if len(caracteres)==3:
               caracteres=f"{caracteres} "
            print (f"| {caracteres}",end="")
            if index_col==len(matriz)-1:    print ("|",end="")
        print()
        print(f"+{'----+'*(len(matriz)-1)}----+")
            
#Mostramos la matriz de una forma mas prolija 
#################################################################################################################           

def check (matriz):
    dim = range(0,len(matriz))
    """
    sum_filas=[]
    for index_x in dim:
        sum_filas.append(sum(matriz[index_x])) #check filas
    print(sum_filas)
    
    sum_columnas=[]
    for index_x in dim:
        temp_1=[]
        for index_y in dim:
           temp_1.append(matriz[index_y][index_x]) #check columnas
           sum_columnas.append(sum(temp_1))
    print(sum_columnas)
    
    temp_2=[]
    sum_diagonales=[]
    for index_x in dim:
        for index_y in dim:
           temp_2.append(matriz[index_y][index_y]) #check diagonal principal o alfa
           sum_diagonales.append(sum(temp_2))

    
    temp_3=[]
    for index_x in dim:
        for index_y in dim:
           temp_3.append(matriz[index_y][len(matriz)-1-index_y]) #check diagonal secundaria o beta
           sum_diagonales.append(sum(temp_3))
    print(sum_diagonales)
       """
       #index_x = primario index_y = secundario
    temp_2=[]
    sum_diagonales=[]
    temp_3=[]
    sum_columnas=[]
    sum_filas=[]
    for primario in dim:
        sum_filas.append(sum(matriz[primario])) #check filas
        temp_1=[]
        for secundario in dim:
           temp_1.append(matriz[secundario][primario]) #check columnas
           sum_columnas.append(sum(temp_1))
           temp_2.append(matriz[primario][primario]) #check diagonal principal o alfa
           temp_3.append(matriz[primario][len(matriz)-1-primario]) #check diagonal secundaria o beta
           sum_diagonales.append(sum(temp_2))
           sum_diagonales.append(sum(temp_3))
           
    print(f"{sum_filas=}")
    print(f"{sum_columnas=}")
    print(f"{sum_diagonales=}")
    filas_suma_todas = [True if sum_filas[0]==sum_filas[index_fila] else False for index_fila in range( 1, len (sum_filas) )]
    columnas_suma_todas = [True if sum_columnas[0]==sum_columnas[index_col] else False for index_col in range( 1, len (sum_columnas) )]
    
    print( all (filas_suma_todas), all(columnas_suma_todas), sum_diagonales[0]==sum_diagonales[1])
        
    if not ( all (filas_suma_todas)and \
        all(columnas_suma_todas)and\
            sum_diagonales[0]==sum_diagonales[1]):
        return(False,0) #no puede ser magica 
    if not (sum_filas[0]==sum_columnas[0]==sum_diagonales[0]):
        return(False,0)
    else:
        return (True, sum_diagonales[0])
    
       
#################################################################################################################   
pseudo_matriz_a = [ [4,3,8], [9,5,1],[2,7,6]]
pseudomatrices={
                    "A" : [
                                    [4,3,8],
                                    [9,5,1],
                                    [2,7,6]
                                ],
                    "B" : [
                                    [8,1,6],
                                    [3,5,7],
                                    [4,9,2]
                                ],
                    "C" : [
                                    [16, 3, 2,13],
                                    [ 5,10,11, 8],
                                    [ 9, 6, 7,12],
                                    [ 4,15,14, 1]
                                ],
                    "D" : [
                                    [16, 2, 3,13],
                                    [ 5,11,10, 8],
                                    [ 9, 7, 6,12],
                                    [ 4,14,15, 1]
                                ],
                    "E" : [
                                    [ 4,14,15, 1],
                                    [ 9, 7, 6,12],
                                    [ 5,11,10, 8],
                                    [16, 2, 3,13]
                                ],

                    "F" : [
                                    [17,24, 1, 8,15],
                                    [23, 5, 7,14,16],
                                    [ 4, 6,13,20,22],
                                    [10,12,19,21, 3],
                                    [11,18,25, 2, 9]
                                ],
                    "G" : [
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

#---------------------------------selecciono una pseudo matriz mágica      
#################################################################################################################     
while True:
    opcion =input(f"""Seleccione:
                  1) Para Crear Matriz
                  2) Usar una Matriz Existente

      
                  3) Salir 
                  : """ 
                  )
    match (opcion):
        case "3":
            break
        case "1":
            # ~ #-----------------------------------crear y mostrar pseudomatrices
            # #------------------------------------
             len_    = crear()
            # #------------------------------------
             print (f"{len_}\n{type(len_)}")
            # #------------------------------------
             Matriz_2 = cargar(len_)
            # #------------------------------------
             print(f"{Matriz_2=}")

        case "2":
                while opcion not in ["A","B","C","D","E","F","G"]:
                    opcion = input("""Seleccione entre las matricez A a G :""").upper()
                    #------------------------------------
                    Matriz_2=pseudomatrices[opcion]
                    #------------------------------------
                    len_=len(Matriz_2)
                    #------------------------------------

    mostrar(Matriz_2)
    #------------------------------------
    start_time = time()
    #------------------------------------
    bool_,numero_magico =  check(Matriz_2)
    #------------------------------------
    elapsed_time = time() - start_time
    #------------------------------------
    print (f"tiempo de cheque {elapsed_time}")
    if bool_ is True:
        print (f"La Matriz es mágica !!!!!!!!\n el número mágico es {numero_magico} para una matriz de {len_} por {len_} ")
    else:
        print ("La Matriz No es mágica")
        





exit()


                






#--------------------------------------------------Anzur--------------------------------------------------------#
#################################################################################################################