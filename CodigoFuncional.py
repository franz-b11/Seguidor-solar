#Inicio del programa 
from machine import ADC, Pin, PWM
from time  import sleep_ms

# Asignar las fotoresistencias En los pines De ADC
ldr1 = ADC(28) # Fotoresistencia superior verde
ldr2 = ADC(27) # Fotoresistencia derecha  naranja
ldr3 = ADC(26) # Fotoresitencia izquierda  cafe

#Asignar los pines y limites conectados a el servomotor Horizo                                               
servoh = PWM(Pin(13))     # Asignacion del pin PWM 
servoh.freq(50)   #Establecer frecuencia a trabajar 
servohLimitHigh = 2500000
servohLimitLow = 27777
servoh_contador=1250000   # iniciar en 2
#Asignar los pines y limites conectados a el servomotor Vertical                             
# servov = 145
servov = PWM(Pin(14))
servov.freq(50)
servovLimitHigh = 2500000  # Limite superior del angulo 
servovLimitLow = 1666666   # Limite inferior del angulo
servov_contador=1944444  # iniciar en 145
while True:
    leer1 = ldr1.read_u16() #iz-arri
    leer2 = ldr2.read_u16() #de-arri
    leer3 = ldr3.read_u16() #abajo
    sleep_ms(70)
    #print(

    #servov.duty_ns(500000)
    
    promedio_arri = ((leer1 + leer2 )/2)
    promedio_iz = ((leer1 + leer3)/2)
    promedio_de = ((leer2 + leer3)/2)
    #print(promedio_arri)
    #print(promedio_iz)
    #print(promedio_de)
    if (promedio_arri > leer3 ):
        servov.duty_ns(servov_contador) #Se mueve
        servov_contador=servov_contador+27777 # 1 grado hacia arriba
       #print('servov_contador',servov_contador)
        if (servov_contador >= servovLimitHigh):
            servov_contador = servovLimitHigh
    elif (promedio_arri < leer3):
        servov.duty_ns(servov_contador)
        servov_contador = servov_contador-27777 # 2
        #print('servov_contador',servov_contador)
        if (servov_contador <= servovLimitLow):
            servov_contador = servovLimitLow
    else:
        servov.duty_ns(servov_contador)    
    if (promedio_de > promedio_iz):
        servoh.duty_ns(servoh_contador) #Se mueve
        servoh_contador=servoh_contador+27777 # 1 grado hacia arriba
        #print('servoh_contador',servoh_contador)
        if (servoh_contador >= servohLimitHigh):
            servoh_contador = servohLimitHigh
    elif (promedio_de < promedio_iz):
        servoh.duty_ns(servoh_contador)
        servoh_contador = servoh_contador-27777 # 2
        #print('servov_contador',servov_contador)
        if (servoh_contador <= servohLimitLow):
            servoh_contador = servohLimitLow
    else:
        servoh.duty_ns(servoh_contador)             
                 
            
            
        
        
        
            
            
            

    
        
    
    
    