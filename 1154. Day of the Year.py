class Solution:
    def dayOfYear(self, date: str) -> int:
        dictionary_1 = [[1, 31], [2, 29], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31],
                        [11, 30], [12, 31]]
        acc_dictionary_1 = self.acc(dictionary_1)
        dictionary_2 = [[1, 31], [2, 28], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31],
                        [11, 30], [12,31]]
        acc_dictionary_2 = self.acc(dictionary_2)
        # print(acc_dictionary_1, acc_dictionary_2)
        y, m, d = date.split('-')
        res = 0
        if int(y) % 4 == 0:
            if int(m) == 1:
                data_first = 0
            else:
                data_first = acc_dictionary_1[int(m) - 1]
            res = data_first + int(d)
        else:
            if int(m) == 1:
                data_first = 0
            else:
                data_first = acc_dictionary_2[int(m) - 1]
            res = data_first + int(d)
        return res

    def acc(self, dictionary):
        acc_dictionary_1 = {}
        acc_dictionary_1[dictionary[0][0]] = dictionary[0][1]
        acc = dictionary[0][1]
        for i in range(1, len(dictionary)):
            acc += dictionary[i][1]
            acc_dictionary_1[dictionary[i][0]] = acc
        return acc_dictionary_1

s = Solution()
d = "1900-03-25"
print(s.dayOfYear(d))
# d = "2019-01-09"
# print(s.dayOfYear(d))
d = "2019-02-10"
print(s.dayOfYear(d))
d = "2003-03-01"
print(s.dayOfYear(d))
d = "2004-03-01"
print(s.dayOfYear(d))
