
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Descripción:
        Recorro cada carácter de s y lo busco en una copia de t.
        Si lo encuentro, lo elimino para simular el emparejamiento de letras.
        Si en algún momento no está disponible, no es anagrama.

        Complejidad
        Tiempo O(n^2) — búsqueda y eliminación en lista para cada carácter
        Espacio O(n) — copia de la cadena t
        """
        if len(s) != len(t):
            return False
        
        t_list = list(t)
        
        for c in s:
            if c not in t_list:
                return False
            t_list.remove(c)
        
        return True
