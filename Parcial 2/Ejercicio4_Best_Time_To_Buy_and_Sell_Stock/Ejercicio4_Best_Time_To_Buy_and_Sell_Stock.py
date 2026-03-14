class Solution:
    def maxProfit(self, prices):
        """
        Estrategia greedy:
        Se aprovecha cada aumento de precio entre días consecutivos. 
        Si el precio de hoy es mayor que el de ayer, se suma esa diferencia como ganancia.

        Explicación breve del código:
        ganancia_total guarda la ganancia acumulada.
        Se recorre el arreglo desde el segundo día.
        Si el precio actual es mayor que el anterior, se suma la diferencia a la ganancia.
        Al final se retorna la ganancia total obtenida.

        Complejidad

        Tiempo: O(n) porque el arreglo se recorre una sola vez.
        Espacio: O(1) porque solo se utiliza una variable adicional para acumular la ganancia.
        """
        
        ganancia_total = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] > prices[i - 1]:
                ganancia_total += prices[i] - prices[i - 1]
        
        return ganancia_total