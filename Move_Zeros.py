"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Here is a starting point:
"""


class Solution:
    @staticmethod
    def get_zero_index(numbers: 'list') -> 'int':
        """
        :param numbers: list of elements
        :return: index of first 0 in numbers
        """
        for index in range(len(numbers)):
            if numbers[index] == 0:
                return index

    def move_zeros(self, input_list: 'list') -> 'None':
        """
        Instead of moving 0 to right we move all other numbers to left
        """
        zero_index = Solution.get_zero_index(input_list)
        if zero_index is None:
            return
        left_index = 0
        while left_index + 1 < len(input_list) and zero_index < len(input_list):
            left_index = max(left_index, zero_index + 1)
            while left_index < len(input_list) and input_list[left_index] == 0:
                left_index += 1
            if left_index < len(input_list):
                input_list[left_index], input_list[zero_index] = input_list[zero_index], input_list[left_index]
            zero_index += 1

if __name__=='__main__':
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    Solution().move_zeros(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
