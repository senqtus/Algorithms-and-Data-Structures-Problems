"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""
from collections import defaultdict


class Solution:
    def is_valid(self, string: 'str') -> 'bool':
        stack_open = []
        dict_paren = defaultdict()
        dict_paren[')'] = '('
        dict_paren['}'] = '{'
        dict_paren[']'] = '['
        for index in range(len(string)):
            if not string[index] in dict_paren:
                stack_open.append(string[index])
            else:
                if len(stack_open) < 1 or stack_open[-1] != dict_paren[string[index]]:
                    return False
                else:
                    stack_open.pop()
        if len(stack_open) > 0:
            return False
        return True

if __name__=='__main__':
    s = '((())])'
    print(Solution().is_valid(s))
