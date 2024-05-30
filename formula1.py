#1-Proporcionar los datos en un diccionario con listas como valores.
#2-Tranformalo en un diccionario con otro diccionario anidado en base a la auxiliar 
#3-Generar dos listas de los pilotos que abandonaron y los que no 
#4-Tiempo de vueltas totales del ganador 
#5-Generar el diccionario del podio con los tres pilotos mas rapidos 

#   -------------------------------------- FORMULA 1 -----------------------------------  #

import json
import os
from colorama import init, Fore

def pausa():
    input(Fore.YELLOW + "\tPara iniciar presione una tecla, cualquiera.\n Cual es una tecla cualquiera? \n Esc,Ctrl,Pg up... No tiene una tecla cualquiera! "+ Fore.RESET)
    

pausa()


def leer_json(nombre_archivo="Formula_1", modo="r"):
    with open(f"{nombre_archivo}.json", "r") as objeto_json:
        object_python = json.load(objeto_json)
        for piloto, datos in object_python.items():
            nombre_formateado = " ".join(word.capitalize() for word in piloto.split())
            print(f"{nombre_formateado}:")
            print(json.dumps(datos, indent=4))
    return object_python



        
def grabar_json (nombre_archivo= "Formula_1", modo="w", **diccionario_entrada):
   #  if isinstance(valor, datatime):
   #      valor=valor.strftime("%d_%m_%Y")
 #  with open(f"{nombre_archivo}.json", mode=modo , encoding="utf-8") as io_objeto:
 #     json.dump(diccionario_entrada,io_objeto, ensure_ascii=False, indent=4)
       
    with open(f"{nombre_archivo}.json", mode=modo ,encoding="utf-8" ) as io_objeto:
       json.dump(diccionario_entrada,io_objeto,ensure_ascii=False, indent=4)

############################################################################################################    
def estructura_de_datos():
    pilotos = [
        "Sergio Pérez",
        "Carlos Sainz",
        "Max Verstappen",
        "Lando Norris",
        "George Russell",
        "Esteban Ocon",
        "Charles Leclerc",
        "Yuki Tsunoda",
        "Oscar Piastri",
        "Fernando Alonso",
        "Lewis Hamilton",
        "Pierre Gasly",
        "Lance Stroll",
        "Nyck de Vries",
        "Kevin Magnussen",
        "Valtteri Bottas",
        "Guanyu Zhou",
        "Alexander Albon",
        "Logan Sargeant",
        "Nico Hulkenberg"
    ]
    
    aux = "tiempo TOTAL en_pista" , "vuelta MAS rapida", "TOTAL de vueltas"
    tiempos = [
        [6150, 115, 52],
        [6150, 115, 52],
        [6140, 116, 52],
        [6141, 116, 52],
        [6160, 115, 52],
        [6165, 114, 52],
        [6172, 112, 52],
        [6175, 115, 52],
        [6177, 114, 52],
        [4720, 111, 40],
        [6111, 114, 52],
        [700, 119, 5],
        [6201, 118, 52],
        [6133, 114, 52],
        [1205, 118, 10],
        [6272, 122, 52],
        [6375, 135, 52],
        [6475, 144, 52],
        [5720, 151, 30],
        [6130, 11, 52]
    ]
    
    pilotos_escuderias = [
        "Sergio Pérez", "RED BULL",
        "Carlos Sainz", "FERRARI",
        "Max Verstappen", "RED BULL",
        "Lando Norris", "MCLAREN",
        "George Russell", "MERCEDES",
        "Esteban Ocon", "ALPINE",
        "Charles Leclerc", "FERRARI",
        "Yuki Tsunoda", "ALPHATAURI",
        "Oscar Piastri", "MCLAREN",
        "Fernando Alonso", "ASTON MARTIN",
        "Lewis Hamilton", "MERCEDES",
        "Pierre Gasly", "ALPINE",
        "Lance Stroll", "ASTON MARTIN",
        "Nyck de Vries", "ALPHATAURI",
        "Kevin Magnussen", "HAAS",
        "Valtteri Bottas", "ALFA ROMEO",
        "Guanyu Zhou", "ALFA ROMEO",
        "Alexander Albon", "WILLIAMS",
        "Logan Sargeant", "WILLIAMS",
        "Nico Hulkenberg", "HAAS"
    ] 
    
    for cada_piloto, valores in zip(pilotos, tiempos):
        dic_tiempos[cada_piloto] = {
            aux[0]: valores[0],
            aux[1]: valores[1],
            aux[2]: valores[2]
        }
        print(f"dic_tiempos[{cada_piloto}] = {dic_tiempos[cada_piloto]}")
    
    return dic_tiempos

    for index in range(0, len(pilotos_escuderias), 2):
        print(f"Piloto {pilotos_escuderias[index]} ------------- Escuderia {pilotos_escuderias[index+1]}")
        if pilotos_escuderias[index] in dic_tiempos.keys():
            dic_tiempos[pilotos_escuderias[index]]["Escuderia"] = pilotos_escuderias[index+1]
        else:
            print("Error")
            grabar_json("Formula_1", "w", **dic_tiempos)
            return dic_tiempos
             

  

                

  
#############################################################################################################################################
 
def terminaron_la_carrera(**dic_tiempos):   
    """
    A)Genera dos listas de los pilotos que abandonaron y los que no.
    parametro de entrada **dic_tiempos con los datos de trabajo. tipo dict()
    parametros de salida dos listas de los pilotos que abandonaron y los que no.
    proceso, filtrados de diccionarios
    """
    si_terminaron=[]
    no_terminaron=[]
    for piloto , valores in dic_tiempos.items():
        if dic_tiempos[piloto]["TOTAL de vueltas"]==52:
            si_terminaron.append(piloto)
        else:
            no_terminaron.append(piloto)
    return (si_terminaron, no_terminaron)
            
#############################################################################################################################################     
    
def f_ganador(**dic_tiempos):
    """
    B)Quien gano, con que tiempo de vueltas y totales
    parametro de entrada **dic_tiempos con los datos de trabajo. tipo dict()
    parametro de salida diccionario, piloto ganador, 
    proceso de filtrados de diccionarios
    """
    menor= max ([dic_tiempos[piloto]["tiempo TOTAL en_pista"] for piloto in dic_tiempos.keys()])
    for piloto in dic_tiempos.keys():
            print(f"""
    {piloto=}
    {dic_tiempos[piloto]["TOTAL de vueltas"]=}
    {dic_tiempos[piloto]["tiempo TOTAL en_pista"]=} {menor}
    """)
            if dic_tiempos[piloto]["TOTAL de vueltas"]==52 and \
               dic_tiempos[piloto]["tiempo TOTAL en_pista"] < menor: 
                    menor = dic_tiempos[piloto]["tiempo TOTAL en_pista"]
            
                    ganador = piloto
    
    print(f"""
    {ganador=}
    """)
                
    return ganador
    
#############################################################################################################################################
def f_podio(**dic_tiempos):
    podio ={
        "primer":"",
        "segundo":"",
        "tercer":""
        }
    for lugar in podio.keys():
        menor= max ([dic_tiempos[piloto]["tiempo TOTAL en_pista"] for piloto in dic_tiempos.keys()])
        for piloto in dic_tiempos.keys():
            print(f"""
                  {piloto=}
                  {dic_tiempos[piloto]["TOTAL de vueltas"]=}
                  {dic_tiempos[piloto]["tiempo TOTAL en_pista"]=} {menor}
                  """)
            if dic_tiempos[piloto]["TOTAL de vueltas"] == 52 and \
                dic_tiempos[piloto]["tiempo TOTAL en_pista"] < menor and \
                    piloto not in podio.values():
                    menor = dic_tiempos[piloto]["tiempo TOTAL en_pista"]
                    buscado = piloto
            print(f"""
                  {buscado=}
                  """)
            podio[lugar]= buscado
    for lugar in podio.keys():
        print(f"{lugar=} piloto{podio[lugar]} {dic_tiempos[podio[lugar]]=}")
    return podio

#############################################################################################################################################

def orden(dic_estruc, **dic_tiempos):

    for lugar in dic_estruc.keys():
        menor= max ([dic_tiempos[piloto]["tiempo TOTAL en_pista"] for piloto in dic_tiempos.keys()])
        for piloto in dic_tiempos.keys():
            print(f"""
                  {piloto=}
                  {dic_tiempos[piloto]["TOTAL de vueltas"]=}
                  {dic_tiempos[piloto]["tiempo TOTAL en_pista"]=} {menor}
                  """)
            if dic_tiempos[piloto]["TOTAL de vueltas"] == 52 and \
                dic_tiempos[piloto]["tiempo TOTAL en_pista"] < menor and \
                    piloto not in dic_estruc.values():
                    menor = dic_tiempos[piloto]["tiempo TOTAL en_pista"]
                    buscado = piloto
            print(f"""
                  {buscado=}
                  """)
            dic_estruc[lugar]= buscado
    for lugar in dic_estruc.keys():
        print(f"{lugar=} piloto{dic_estruc[lugar]} {dic_tiempos[dic_estruc[lugar]]=}")
    return dic_estruc

#############################################################################################################################################

def ver_datos(**dic_tiempos):
    if len(dic_tiempos) > 0:  
        for piloto, valores in dic_tiempos.items():
            print(f"Piloto: {piloto}")
            for sub_clave, sub_valor in valores.items():
                print(f"\t{sub_clave}: {sub_valor}")
    else:
        print("Aun sin datos")  
 

   
dic_tiempos = {}

#############################################################################################################################################
while True:
    opcion =input(f"""Seleccione:
                  1) Para iniciar datos
                  2) Para leer desde archivo
                  3) Ver datos
                  4) Finalizaron la carrera
                  5) Ver Ganador
                  6) Ver podio
      
                  7) Salir 
                  : """ 
                  )
    match (opcion):
        case "1":
            dic_tiempos = estructura_de_datos()
        case "2":
            dic_tiempos =leer_json(nombre_archivo= "Formula_1", modo="r")
        case "3":
            ver_datos(**dic_tiempos)
        case "4":
            regreso = terminaron_la_carrera(**dic_tiempos) 
            si_terminaron = regreso[0]
            no_terminaron = regreso[1]
            print(f"Los pilotos que terminaron la carrera son: {si_terminaron}")
            print(f"Los pilotos que no terminaron la carrera son: {no_terminaron}")
        case "5":
            #ganador = f_ganador(**dic_tiempos)
            #print(f"El piloto ganador es {ganador}, con los valores {dic_tiempos[ganador]}")
              ganador={"primer":"" }
              ganador= orden (ganador, **dic_tiempos)
              for lugar, (piloto, registros) in enumerate(ganador.items()):
                  print(f"El piloto en {piloto} lugar fue: {registros}")
        case "6":
            # podio = f_podio(**dic_tiempos)
               podio={
                   "primer":"",
                   "segundo":"",
                   "tercer":""
                   }
               podio= orden (podio, **dic_tiempos)
               for lugar, (piloto, registros) in enumerate(podio.items()):
                   print(f"El piloto en {piloto} lugar fue: {registros}")

        case "7":
            break
               
  
#############################################################################################################################################
