"""
Solución del laboratorio

"""
from custom_functions import temperature_methods
import statistics as stats
print("BIENVENIDO A OMN")
temperatura_santander = []
temperatura_guajira = []
temperatura_narinno = []
print("A continuación digite las temperaturas de Santander")
try:
 for i in range(0,12):
     t=int(input("Digite la temperatura del mes {}:".format(i+1)))
     temperatura_santander.append(t)
 promediosantander= temperature_methods.promedio_temp(temperatura_santander)
 print('\n')
 print("Ahora digite las temperaturas de Guajira")
 for i in range(0,12):
     t=int(input("Digite la temperatura del mes {}:".format(i+1)))
     temperatura_guajira.append(t)
 promedioguajira= temperature_methods.promedio_temp(temperatura_guajira)
 print('\n')
 print("Por último digite las temperaturas de Nariño")
 for i in range(0,12):
     t=int(input("Digite la temperatura del mes {}:".format(i+1)))
     temperatura_narinno.append(t)
 promedio_narinno= temperature_methods.promedio_temp(temperatura_narinno)
 prom_nal=[promediosantander,promedioguajira,promedio_narinno]
 promedio_nacional=temperature_methods.promedio_temp(prom_nal)
 print('\n')
 print("La lista de temperaturas de Santander es {} y el promedio es: {}".format(temperatura_santander,promediosantander))
 print("La lista de temperaturas de Guajira es  {} y el promedio es: {}".format(temperatura_guajira,promedioguajira))
 print("La lista de temperaturas de Nariño es {} y el promedio es: {}".format(temperatura_narinno,promedio_narinno))
 print('\n')
 print("El promedio de temperaturas a nivel nacional es: {}".format(promedio_nacional))
 print('\n')
 print("En Santander:")
 mes_santander =temperature_methods.mes_caliente(temperatura_santander)
 print("En Guajira:")
 mes_guajira =temperature_methods.mes_caliente(temperatura_guajira)
 print("En Nariño:")
 mes_narino = temperature_methods.mes_caliente(temperatura_narinno)

 santander=temperature_methods.meses_caliente(temperatura_santander)
 guajira=temperature_methods.meses_caliente(temperatura_guajira)
 narinno=temperature_methods.meses_caliente(temperatura_narinno)
 mayor_santander=temperature_methods.mayor_temp(temperatura_santander)
 mayor_guajira=temperature_methods.mayor_temp(temperatura_guajira)
 mayor_narinno=temperature_methods.mayor_temp(temperatura_narinno)
 print('\n')
 meses_calientes=[mayor_santander,mayor_guajira,mayor_narinno]
 prom_mes_caliente=temperature_methods.promedio_temp(meses_calientes)
 print("El promedio de los meses con mayor temperatura es: {}".format(prom_mes_caliente))
 print('\n')
 promedios_departamentos=[promediosantander,promedioguajira,promedio_narinno]
 temperature_methods.promedio_mayor(promedios_departamentos)
 print('\n')
 mayores_temp_anno=temperature_methods.mayor_temp(meses_calientes)
 print("La temperatura mayor presentada en el año fue {}".format (mayores_temp_anno))
 dpto_mayor_anno=temperature_methods.temp_dpto_mayor(meses_calientes)

 if mayores_temp_anno==mayor_santander:
     print(santander)
 elif mayores_temp_anno==mayor_guajira:
     print(guajira)
 elif mayores_temp_anno==mayor_narinno:
     print(narinno)

 print('\n')
 estandar_santander=stats.stdev(temperatura_santander)
 print("La desviación estandar de Santander es: {}".format(estandar_santander))
 estandar_guajira=stats.stdev(temperatura_guajira)
 print("La desviación estandar de Guajira es: {}".format(estandar_guajira))
 estandar_narinno=stats.stdev(temperatura_narinno)
 print("La desviación estandar de Nariño es: {}".format(estandar_narinno))
except ValueError:
    print("No está permitido ingresar letras")
except ZeroDivisionError:
    print("No hay temperaturas, por favor ingreselas")