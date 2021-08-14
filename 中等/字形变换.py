class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if not s or numRows == 1:
            return s
        # 初始化输出表格
        res = []
        for i in range(numRows):
            res.append([])

        flag = True  # 行数递增
        row_num = 0
        for item in s:
            if flag:
                res[row_num].append(item)
                if row_num == numRows - 1:
                    row_num -= 1
                    flag = False
                else:
                    row_num += 1
            else:
                res[row_num].append(item)
                if row_num == 0:
                    row_num += 1
                    flag = True
                else:
                    row_num -= 1
        out = ''
        for row in res:
            out += ''.join(row)
        return out
