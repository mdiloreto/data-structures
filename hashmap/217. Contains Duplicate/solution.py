class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for n in nums: 
            if nums.count(n) > 1:
                return True
        return False
    
class OtherSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # Initialize an empty set
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
        return False  # No duplicates found