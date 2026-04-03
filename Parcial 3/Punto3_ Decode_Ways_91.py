class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Estrategia DP:
        dp[i] = número de formas de decodificar los primeros i caracteres.

        Recurrencia:
        Si un dígito (1-9) es válido → dp[i] += dp[i-1]
        Si dos dígitos (10-26) son válidos → dp[i] += dp[i-2]

        Caso base:
        dp[0] = 1
        dp[1] = 1 si el primer dígito ≠ "0"

        Complejidad:
        Tiempo: O(n)
        Espacio: O(1)
        """

        if not s or s[0] == "0":
            return 0

        anterior_dos = 1
        anterior_uno = 1

        for i in range(1, len(s)):
            actual = 0

            # tomar un dígito
            if s[i] != "0":
                actual += anterior_uno

            # tomar dos dígitos
            dos_digitos = int(s[i-1:i+1])
            if 10 <= dos_digitos <= 26:
                actual += anterior_dos

            anterior_dos = anterior_uno
            anterior_uno = actual

        return anterior_uno