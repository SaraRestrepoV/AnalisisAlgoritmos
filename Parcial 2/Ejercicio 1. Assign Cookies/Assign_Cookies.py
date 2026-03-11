class Solution:
    def findContentChildren(self, g, s):
        """
        Estrategia greedy:
        Ordenamos niños y cookies, y asignamos a cada niño la cookie más pequeña
        que pueda satisfacer su codicia.

        Justificación:
        Al usar primero las cookies más pequeñas para los niños menos exigentes,
        evitamos desperdiciar cookies grandes y maximizamos el número de niños satisfechos.

        Complejidad:
        Tiempo: O(n log n + m log m) por ordenar los arreglos.
        Espacio: O(1) adicional.
        """

        g.sort()
        s.sort()

        i = j = content = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
            j += 1

        return content