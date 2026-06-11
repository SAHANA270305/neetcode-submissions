class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur,tot):
            if tot==target:
                res.append(cur.copy()) # as u want to re-use cur again by removing/adding new elements
                return
            if i>=len(nums) or tot>target: #in case its out of bounds
                return
            cur.append(nums[i]) #cheks with all possible combination using a single number and the previous numbers(eg it checks [2,2,1] and keeps adding 1 until out of bound comes)
            dfs(i,cur,tot+nums[i])
            cur.pop() 
            dfs(i+1,cur,tot)
        dfs(0,[],0)
        return res
        