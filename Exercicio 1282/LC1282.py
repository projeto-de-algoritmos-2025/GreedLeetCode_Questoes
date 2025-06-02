import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Inicializa heap e variáveis
        min_heap = []
        current_max = float('-inf')
        
        # Coloca o primeiro elemento de cada lista no heap
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, i, 0))  # (valor, índice da lista, índice dentro da lista)
            current_max = max(current_max, val)
        
        # Inicializa a menor faixa possível
        best_range = [float('-inf'), float('inf')]
        
        while True:
            current_min, list_idx, element_idx = heapq.heappop(min_heap)
            
            # Atualiza o intervalo se for menor
            if current_max - current_min < best_range[1] - best_range[0] or \
               (current_max - current_min == best_range[1] - best_range[0] and current_min < best_range[0]):
                best_range = [current_min, current_max]
            
            # Move para o próximo elemento da mesma lista
            if element_idx + 1 == len(nums[list_idx]):
                break  # Chegou ao final de uma lista, não é mais possível incluir todos
            next_val = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
            current_max = max(current_max, next_val)
        
        return best_range
