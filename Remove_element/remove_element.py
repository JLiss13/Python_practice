# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List
class Solution:
        
    def removeElement(self, nums: List[int], val: int) -> int:
        print("Inside the remove Element function")
        
        # Add all elements to new list that do not equal the val
        original_size_of_nums = len(nums)-1
        for i in range(original_size_of_nums+1):
            if nums[original_size_of_nums-i] == val:
                del nums[original_size_of_nums-i]
        
        # Return the number of elements in nums which are not equal to val.
        k = len(nums)
        print(nums)
                
        return k
        
        
if __name__ == "__main__":
    print("Running the main function")
    nums = [3,2,2,3]
    val = 3
    solution_inst = Solution()
    k = solution_inst.removeElement(nums, val)
    print("Case 1: Number of elements not removed the list: " + str(k))
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = solution_inst.removeElement(nums, val)
    print("Case 2: Number of elements not removed the list: " + str(k))
    