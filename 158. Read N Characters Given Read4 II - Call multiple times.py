class Solution:
    def __init__(self):
        self.pointer = 0
        self.count = 0
        self.temp = [''] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        index = 0
        while index < n:
            if self.pointer == 0: #当前temp是空的或者里面的cha都用完了
                self.count = read4(self.temp) #就掉一次read4
            if self.count == 0: #如果读不出东西了，说明stream用了了，直接break
                break
            while index < n and self.pointer < self.count: #当pointer<count说明temp里的char没都用了，就都用掉
                buf[index] = self.temp[self.pointer]
                index += 1
                self.pointer += 1
            if self.pointer == self.count:
                self.pointer = 0
        return index
