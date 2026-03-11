class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        Estrategia greedy:
        Ordenamos los intervalos por su tiempo de finalización y seleccionamos
        siempre el que termina primero para minimizar solapamientos.

        Justificación:
        Al mantener el intervalo que termina antes dejamos más espacio disponible
        para los siguientes, reduciendo la cantidad de intervalos que deben eliminarse.

        Complejidad:
        Tiempo: O(n log n) por ordenar los intervalos.
        Espacio: O(1) adicional.
        """

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        remove = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                remove += 1
            else:
                end = intervals[i][1]

        return remove