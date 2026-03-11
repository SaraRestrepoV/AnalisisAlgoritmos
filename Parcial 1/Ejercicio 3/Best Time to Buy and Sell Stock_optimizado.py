class Solution:
    def maxProfit(self, prices):
        precio_minimo = float('inf')
        maxima_ganancia = 0

        for precio_actual in prices:

            if precio_actual < precio_minimo:
                precio_minimo = precio_actual

            ganancia_potencial = precio_actual - precio_minimo

            if ganancia_potencial > maxima_ganancia:
                maxima_ganancia = ganancia_potencial

        return maxima_ganancia