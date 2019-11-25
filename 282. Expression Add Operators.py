# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
#
# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []


# This problem has a lot of edge cases to be considered:
#
# 1： overflow: we use a long type once it is larger than Integer.MAX_VALUE or minimum, we get over it.
# 2：0 sequence: because we can't have numbers with multiple digits started with zero, we have to deal with it too.
# 3：a little trick is that we should save the value that is to be multiplied in the next recursion.

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        if num is None or len(num) == 0:
            return res
        path = ''
        pos = 0
        val = 0
        multed = 0
        # num = list(num)
        self.helper(res, path, num, target, pos, val, multed)
        return res
    def helper(self,res,path,num,target,pos,val,multed):
        if pos == len(num):
            if target == val:
                res.append(path)
            return
        for i in range(pos,len(num)):
            if i != pos and num[pos] == '0':
                break
            cur = num[pos:i+1]
            if pos == 0:
                self.helper(res, path+cur,num, target, i+1, int(cur), int(cur))
            else:
                self.helper(res, path + '+' + cur, num, target, i + 1, val+int(cur), int(cur))
                self.helper(res, path + '-' +cur, num, target, i + 1, val-int(cur), -int(cur))
                # from'1 + 2 + 3' to '1 + 2 + 3 * 4 ',需要 (1 + 2 + 3) - 3 + (3 * 4).
                self.helper(res, path + '*' +cur, num, target, i + 1, val-multed+multed*int(cur), multed*int(cur))


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.ans = []
        self.target = target
        for i in xrange(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                continue
            self.helper(num[i:], int(num[:i]), num[:i], int(num[:i]), '#')

        return self.ans

    def helper(self, num, current, tmpAns, pre_val, pre_op):
        if not num:
            if self.target == current:
                self.ans.append(tmpAns)
            return

        for i in xrange(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                continue
            now = int(num[:i])
            self.helper(num[i:], current + now, tmpAns + '+' + num[:i], now, '+')
            self.helper(num[i:], current - now, tmpAns + '-' + num[:i], now, '-')

            if pre_op == '+':
                self.helper(num[i:], current - pre_val + pre_val * now, tmpAns + '*' + num[:i], pre_val * now, pre_op)
            elif pre_op == '-':
                self.helper(num[i:], current + pre_val - pre_val * now, tmpAns + '*' + num[:i], pre_val * now, pre_op)
            else:
                self.helper(num[i:], current * now, tmpAns + '*' + num[:i], pre_val * now, pre_op)
class Solution(object):
    def addOperators(self, num, target):
        res =[]
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res, target) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res, target):
        if not num:
            if cur == target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res, target)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res, target)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res, target)


class Solution1:
    def addOperators(self, num: str, target: int):
        num_array = [int(ele) for ele in list(num)]
        operater = ['+', '-', '*']
        res = []
        temp_array = []
        pos = 0
        pre = 0
        sum_up = 0
        self.dfs(num_array, pos, pre, operater, temp_array, target, sum_up, res)
        return res

    def dfs(self, num_array, pos, pre, operater, temp_array, target, sum_up, res):
        if pos == len(num_array) and target == sum_up:
            res.append(''.join(temp_array[:]))
        elif pos >= len(num_array):
            return
        for i in range(pos, len(num_array)): #
            if i != pos and num_array[pos] == 0: #防止cur的打头是0，类似023这一类的
                break
            cur = int(''.join(str(ele) for ele in num_array[pos: i + 1])) # cur取从头到i这段
            if pos == 0: #如果cur这段是input的头
                temp_array.append(str(cur))
                self.dfs(num_array, i + 1, cur, operater, temp_array, target, cur, res)
                temp_array.pop()
            else:
                for ele in operater: #对三种operator个做一遍
                    next_sum_up, next_pre = self.operate(ele, cur, pre, sum_up)
                    temp_array.append(ele)
                    temp_array.append(str(cur))
                    self.dfs(num_array, i + 1, next_pre, operater, temp_array, target, next_sum_up, res)
                    temp_array.pop()
                    temp_array.pop()

    def operate(self, ele, cur, pre, sum_up):
        if ele == '+':
            sum_up += cur
            pre = cur
        elif ele == '-':
            sum_up -= cur
            pre = -cur
        elif ele == '*':
            sum_up = sum_up - pre + pre * cur
            pre = pre * cur
        return sum_up, pre


class SolutionSimple:
    def addOperators(self, num: str, target: int):
        num_array = [int(ele) for ele in list(num)]
        res = []
        temp = []
        hash_result = {}
        self.dfs(num_array, target, 0, 0, res, temp, hash_result)
        return res

    def dfs(self, num_array, target, cur_result, pos, res, temp, hash_result):
        # base case
        if pos == len(num_array):
            if cur_result == target:
                res.append(''.join(temp))
            return
        # general case
        cur = num_array[pos]
        temp.append("+" + str(cur))
        self.dfs(num_array, target, cur_result + cur, pos + 1, res, temp)
        temp.pop()

        temp.append("-" + str(cur))
        self.dfs(num_array, target, cur_result - cur, pos + 1, res, temp)
        temp.pop()

s = SolutionSimple()

strs = "00"
k = 0
print(s.addOperators(strs,k)) # ['0+0', '0-0', '0*0']
strs = "1234"
k = 10
print(s.addOperators(strs,k))
strs = "53615"
k = 2
print(s.addOperators(strs,k)) # ['0+0', '0-0', '0*0']


# strs = "12"
# k = 12
# # print(s.addOperators(strs,k))
# strs = "123"
# k = 6
# print(s.addOperators(strs,k)) #['1+2+3', '1*2*3']
# strs = "232"
# k = 8
# print(s.addOperators(strs,k)) #['2+3*2', '2*3+2']
# strs = "105"
# k = 5
# print(s.addOperators(strs,k)) #['1*0+5', '10-5']
# strs = "00"
# k = 0
# print(s.addOperators(strs,k)) # ['0+0', '0-0', '0*0']
#
# strs = "3456237490"
# k = 9191
# print(s.addOperators(strs,k)) #[]





