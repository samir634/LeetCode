class Solution:
    def twoSum(nums, target):

        # Create a dictionary to store the complement of each number
        num_dict = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []  # If no solution is found, return an empty list

    # Example usage:
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # Output: [0, 1] (indices of numbers 2 and 7 that add up to 9)