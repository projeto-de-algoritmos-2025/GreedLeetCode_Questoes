class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        # Ordena os intervalos com base no tempo de término (greedy)
        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1  # sobreposição, remover esse intervalo
            else:
                end = intervals[i][1]  # atualiza o fim do último intervalo aceito

        return count
