"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)


"""


class Solution:

    def max_area_of_island(self, grid: 'list(list([int]))') -> int:

        def check(grid, x, y):
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
                return True
            return False

        def recurse(grid, x, y, area):
            grid[x][y] = 0
            if check(grid, x + 1, y):
                area = max(area, recurse(grid, x + 1, y, area + 1))
            if check(grid, x - 1, y):
                area = max(area, recurse(grid, x - 1, y, area + 1))
            if check(grid, x, y + 1):
                area = max(area, recurse(grid, x, y + 1, area + 1))
            if check(grid, x, y - 1):
                area = max(area, recurse(grid, x, y - 1, area + 1))
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if check(grid, i, j):
                    max_area = max(max_area, recurse(grid, i, j, 1))
        return max_area
