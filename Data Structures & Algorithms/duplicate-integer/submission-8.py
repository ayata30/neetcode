class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()


        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False



        '''
        Input: nums = [1, 2, 3, 3]
                       0  1  2   3

                  if nums[i]      

Output: true
'''
        