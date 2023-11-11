class Solution:
    @staticmethod
    def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
        x_list = []
        [x_list.append(i[0]) for i in points]
        x_list.sort()
        print(x_list)

        max_sub = 0
        for i in range(len(x_list) - 1):
            max_sub = max(max_sub, x_list[i + 1] - x_list[i])

        return max_sub


print(Solution.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))