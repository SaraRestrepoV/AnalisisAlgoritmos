
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Descripción:
        Cuento cuántas veces aparece cada letra en s usando un diccionario.
        Luego recorro t restando esas frecuencias.
        Si alguna frecuencia se vuelve negativa, significa que hay más letras
        en t que en s y no es anagrama.

        Complejidad
        Tiempo O(n) — un solo recorrido de ambas cadenas
        Espacio O(1) — alfabeto fijo (26 letras)
        """
        if len(s) != len(t):
            return False
        
        cuenta = {}
        
        for c in s:
            cuenta[c] = cuenta.get(c, 0) + 1
        
        for c in t:
            cuenta[c] = cuenta.get(c, 0) - 1
            if cuenta[c] < 0:
                return False
        
        return True
