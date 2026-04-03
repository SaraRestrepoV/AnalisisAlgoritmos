class Solution:
    def longestCommonSubsequence(self, texto1: str, texto2: str) -> int:
        """
        Estrategia DP:
        dp[i][j] = longitud de la subsecuencia común más larga entre
        los primeros i caracteres de texto1 y j de texto2.

        Recurrencia:
        Si texto1[i-1] == texto2[j-1] → dp[i][j] = dp[i-1][j-1] + 1
        Si no → dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        Caso base:
        dp[i][0] = 0
        dp[0][j] = 0

        Complejidad:
        Tiempo: O(n*m)
        Espacio: O(n*m)
        """

        longitud_texto1 = len(texto1)
        longitud_texto2 = len(texto2)

        # Crear matriz DP inicializada en 0
        dp = [[0] * (longitud_texto2 + 1) for _ in range(longitud_texto1 + 1)]

        for i in range(1, longitud_texto1 + 1):
            for j in range(1, longitud_texto2 + 1):

                caracter_texto1 = texto1[i - 1]
                caracter_texto2 = texto2[j - 1]

                # Si los caracteres coinciden
                if caracter_texto1 == caracter_texto2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Tomar el máximo entre eliminar uno u otro
                    dp[i][j] = max(
                        dp[i - 1][j],  # eliminar caracter de texto1
                        dp[i][j - 1]   # eliminar caracter de texto2
                    )

        return dp[longitud_texto1][longitud_texto2]