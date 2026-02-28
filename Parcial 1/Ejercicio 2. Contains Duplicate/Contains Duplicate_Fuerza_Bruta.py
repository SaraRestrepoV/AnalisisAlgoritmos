class Solution:
    def containsDuplicate(self, nums):
        total_elementos = len(nums)

        for indice_actual in range(total_elementos):
            for indice_siguiente in range(indice_actual + 1, total_elementos):

                if nums[indice_actual] == nums[indice_siguiente]:
                    return True

        return False