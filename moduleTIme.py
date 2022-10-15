from collections import Counter
import time as t


def alarma(tiempo_horas,tiempo_minutos):

    while True:
        tiempo_h= t.localtime().tm_hour
        tiempo_m = t.localtime().tm_min

        if tiempo_horas == tiempo_h and tiempo_minutos == tiempo_m: 
            count = 0
            while count < 10: 
                print("ALARMA SONANDO, HORA DE SALIR DEL TRABAJO")
                t.sleep(1)
                count += 1    
            break
        else:
            tiempo_actual = (tiempo_h * 60) + tiempo_m
            tiempo_alarmar = (tiempo_horas * 60) + tiempo_minutos
            
            if tiempo_actual > tiempo_alarmar:
                tiempo = tiempo_actual - tiempo_alarmar
                tiempo = (24*60) - tiempo   
                tiempo_h = tiempo // 60
                tiempo_m = tiempo % 60
                print ("Falta: ",tiempo_h,":",tiempo_m," para salir") 
            elif tiempo_alarmar > tiempo_actual:
                tiempo = tiempo_alarmar -tiempo_actual
                tiempo_h = tiempo // 60
                tiempo_m = tiempo % 60
                print ("Falt: ",tiempo_h,":",tiempo_m," para salir")
            t.sleep(5)

alarma(7,30)
