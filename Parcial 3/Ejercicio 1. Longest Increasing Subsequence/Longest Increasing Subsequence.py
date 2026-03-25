class Solution:
    def lengthOfLIS(self, nums):
        """
        Estrategia DP:
        dp[i] = longitud de la subsecuencia creciente más larga que termina en i.

        Recurrencia:
        Si nums[j] < nums[i], entonces dp[i] = max(dp[i], dp[j] + 1).

        Caso base:
        dp[i] = 1.

        Complejidad:
        Tiempo: O(n^2)
        Espacio: O(n)
        """

        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # caso base

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)