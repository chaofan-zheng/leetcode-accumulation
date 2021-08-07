"""
墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。
投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。
请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。
 
示例 1：

输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
输出：4
解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
示例 2：

输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
输出：5
解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
示例 3：

输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
输出：1
示例 4：

输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
输出：4
 

提示：

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import copy
from math import sqrt

""" 大体思路是，两点定圆，遍历所有两点，得到所有圆心列表。用圆心列表求的所有点对应的距离得到count"""


class Solution:
    def numPoints(self, points: list, r: int) -> int:
        # 保护输入
        if len(points) == 1:
            return 1
        counts = []
        circle_list = self.gen_circle_run(points, r)
        for point in circle_list:
            counts.append(self.count_in_circle(point, points, r))
        if not counts:
            return 1
        print(max(counts))
        return max(counts)

    def gen_circle_run(self, points, r):
        circle_list = []
        my_points = copy.deepcopy(points)
        while len(my_points) >= 2:
            point_a = my_points.pop(0)
            for point in my_points:
                # print(self.gen_circle(point_a, point, r))
                a, b = self.gen_circle(point_a, point, r)
                if a and a not in circle_list:
                    circle_list.append(a)
                if b and b not in circle_list:
                    circle_list.append(b)
        # for point in circle_list:
        #     print(point)
        return circle_list

    def gen_circle(self, point_a, point_b, r):
        """以a点为圆心，b为圆心分别做圆相交，两个交点就是圆心坐标，需要推导以下公式"""
        try:
            if point_a[0] == point_b[0]:
                y0 = y1 = (point_a[1] + point_b[1]) / 2
                deltay = (y0 - point_a[1]) ** 2
                deltax = sqrt(r ** 2 - deltay)
                x0 = point_b[0] - deltax
                x1 = point_b[0] + deltax
            else:
                C1 = (point_b[0] ** 2 + point_b[1] ** 2 - point_a[0] ** 2 - point_a[1] ** 2) / 2 / (point_b[0] - point_a[0])
                C2 = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
                A = 1 + C2 ** 2
                B = 2 * (point_a[0] - C1) * C2 - 2 * point_a[1]
                C = (point_a[0] - C1) ** 2 + point_a[1] ** 2 - r ** 2
                y0 = (-B + sqrt(B * B - 4 * A * C)) / (2 * A)
                y1 = (-B - sqrt(B * B - 4 * A * C)) / (2 * A)
                x0 = C1 - C2 * y0
                x1 = C1 - C2 * y1
        except:
            return None,None
        return [x0, y0], [x1, y1]

    def count_in_circle(self, point, points, r):
        count = 0
        for i in points:
            distance2 = (point[0] - i[0]) ** 2 + (point[1] - i[1]) ** 2
            if distance2 <= r ** 2:
                count += 1
        return count


if __name__ == '__main__':
    points = [[-2, 0], [2, 0], [0, 2], [0, -2]]
    r = 1
    # points = [[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]]
    # r = 5
    # points = [[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]]; r = 2
    solution = Solution()
    solution.numPoints(points, r)
