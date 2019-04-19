import unittest
from custom_functions import temperature_methods

class TestTemperatureMethods (unittest.TestCase):


    def test_promedio_temp (self):

        list_temp = [23,28,41,35,37,33,38,39,40,30,23,40]
        promedio = temperature_methods.promedio_temp(list_temp)

        self.assertAlmostEqual (promedio, 33.91666667 )

    def test_mes_caliente(self):

        list_temp = [23, 28, 41, 35, 37, 33, 38, 39, 40, 30, 23, 40]
        mes = temperature_methods.mes_caliente(list_temp)

        self.assertEqual(mes, 2)

    def test_meses_caliente(self):

        list_temp = [23, 28, 41, 35, 37, 33, 38, 39, 40, 30, 23, 40]
        mes_anno= temperature_methods.meses_caliente(list_temp)

        self.assertEqual(mes_anno, "En el mes de Marzo")

    def test_mayor_temp(self):

        list_temp = [23, 28, 41, 35, 37, 33, 38, 39, 40, 30, 23, 40]
        temperatura_mayor= temperature_methods.mayor_temp(list_temp)

        self.assertEqual(temperatura_mayor, 41)

    def test_promedio_mayor(self):

        promedios= [33,25,42]
        mayor_promedio =temperature_methods.promedio_mayor(promedios)

        self.assertEqual(mayor_promedio, 42)

    def test_temp_dpto_mayor(self):
        promedios= [33,25,42]
        temmp_mayor=temperature_methods.temp_dpto_mayor(promedios)

        self.assertEqual(temmp_mayor, 2)









