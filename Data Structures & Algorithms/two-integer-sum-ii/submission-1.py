class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        i=0
        j=len(numbers)-1

        while i<j:
            s=numbers[i]+numbers[j]
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [i+1,j+1]
        return []
        """
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        return []
