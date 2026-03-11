class Solution:
    def maxProfit(self, prices):
        total_dias = len(prices)
        maxima_ganancia = 0

        for dia_compra in range(total_dias):
            for dia_venta in range(dia_compra + 1, total_dias):

                precio_compra = prices[dia_compra]
                precio_venta = prices[dia_venta]

                ganancia = precio_venta - precio_compra

                if ganancia > maxima_ganancia:
                    maxima_ganancia = ganancia

        return maxima_ganancia