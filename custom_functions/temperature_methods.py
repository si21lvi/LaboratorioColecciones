def promedio_temp (lista):
    suma= 0
    promedio=0
    for item in lista:
        suma = suma + item

    promedio = suma / len(lista)

    return promedio

def mes_caliente (lista):
    tt=lista[0]
    posicion=0
    for i in range (0,len(lista)):
     if lista[i] > tt:
         tt= lista[i]
         posicion =lista.index(tt)
    if posicion==0:
        print("El mes más caliente fue Enero")
    if posicion==1:
        print("El mes más caliente fue Febrero")
    if posicion==2:
        print("El mes más caliente fue Marzo")
    if posicion==3:
        print("El mes más caliente fue Abril")
    if posicion==4:
        print("El mes más caliente fue Mayo")
    if posicion==5:
        print("El mes más caliente fue Junio")
    if posicion==6:
        print("El mes más caliente fue Julio")
    if posicion==7:
        print("El mes más caliente fue Agosto")
    if posicion==8:
        print("El mes más caliente fue Septiembre")
    if posicion==9:
        print ("El mes más caliente fue Octubre")
    if posicion==10:
        print ("El mes más caliente fue Noviembre")
    if posicion==11:
        print("El mes más caliente fue Diciembre")

    return posicion

def meses_caliente (lista):
    tt=lista[0]
    posicion=0
    for i in range (0,len(lista)):
     if lista[i] > tt:
         tt= lista[i]
         posicion =lista.index(tt)
    if posicion==0:
        return("En el mes de Enero")
    if posicion==1:
        return("En el mes de Febrero")
    if posicion==2:
        return("En el mes de Marzo")
    if posicion==3:
        return("En el mes de Abril")
    if posicion==4:
        return("En el mes de Mayo")
    if posicion==5:
        return("En el mes de Junio")
    if posicion==6:
        return("En el mes de Julio")
    if posicion==7:
        return("En el mes de Agosto")
    if posicion==8:
        return("En el mes de Septiembre")
    if posicion==9:
        return ("En el mes de Octubre")
    if posicion==10:
        return ("En el mes de Noviembre")
    if posicion==11:
        return("En el mes de Diciembre")



def mayor_temp (lista):
    tt=lista[0]
    for i in range (0,len(lista)):
        if lista[i] > tt:
            tt= lista[i]
    return tt


def promedio_mayor (lista):
    tt=lista[0]
    posicion=0
    for i in range (0,len(lista)):
     if lista[i] > tt:
         tt= lista[i]
         posicion=lista.index(tt)
    if posicion==0:
        print ("La temperatura promedio mas alta fue en Santander")
    if posicion==1:
        print ("La temperatura promedio mas alta fue en Guajira")
    if posicion==2:
        print ("La temperatura promedio mas alta fue en Nariño")

    return tt


def temp_dpto_mayor (lista):
    tt=lista[0]
    posicion=0
    for i in range (0,len(lista)):
     if lista[i] > tt:
            tt= lista[i]
            posicion=lista.index(tt)
    if posicion==0:
     print ("Se presentó en Santander")
    if posicion==1:
     print ("se presentó en Guajira")
    if posicion==2:
     print("Se presentó en Nariño")

    return posicion


