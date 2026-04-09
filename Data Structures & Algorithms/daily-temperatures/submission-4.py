class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            days_higher = 0
            higher_achieved = False
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    days_higher += 1
                    higher_achieved = True
                    break
                else:
                    days_higher += 1
            result.append(days_higher if higher_achieved else 0)
        return result

        