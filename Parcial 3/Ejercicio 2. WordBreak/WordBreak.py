class Solution:
    def wordBreak(self, s, wordDict):
        """
        Estrategia DP:
        Usamos un arreglo dp donde dp[i] indica si el prefijo s[0:i]
        puede segmentarse en palabras del diccionario.

        Justificación:
        Si existe un punto j < i tal que dp[j] es True y s[j:i] está
        en el diccionario, entonces dp[i] también es True.

        Complejidad:
        Tiempo: O(n^2) por evaluar todos los cortes posibles.
        Espacio: O(n) para el arreglo dp.
        """

        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]