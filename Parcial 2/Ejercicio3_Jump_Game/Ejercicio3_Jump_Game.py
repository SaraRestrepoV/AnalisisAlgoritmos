class Solution:
    
    def canJump(self, nums):
        """
        Estrategia greedy:
       En cada paso se mantiene el salto más lejano posible alcanzable hasta el momento.
        Si en algún punto el índice actual queda fuera de ese alcance, entonces no es posible 
        avanzar más y no se puede llegar al final del arreglo.

       Explicación breve del código 
       alcance_maximo guarda el índice más lejano que se puede alcanzar hasta el momento. 
       Se recorre el arreglo con un for. 
       Si el índice actual i es mayor que alcance_maximo, significa que no se puede llegar a
       esa posición, por lo tanto se retorna False.
       En cada posición se actualiza el alcance máximo calculando i + nums[i].
       Si en algún momento el alcance máximo llega o supera el último índice del arreglo, se
       retorna True.

       
       Complejidad
       
        Tiempo : O(n) porque el arreglo se recorre una sola vez.
        Espacio: O(1) porque solo se utiliza una variable adicional para guardar el alcance
        máximo.
        
       
         """
        alcance_maximo = 0
        
        for i in range(len(nums)):
            
            if i > alcance_maximo:
                return False
            
            alcance_maximo = max(alcance_maximo, i + nums[i])
            
            if alcance_maximo >= len(nums) - 1:
                return True
        
        return True