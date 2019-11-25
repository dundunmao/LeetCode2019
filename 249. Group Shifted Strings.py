class Solution:
    def groupStrings(self, strings):
        str_to_diff = {}
        single = []
        for ele in strings:
            if len(ele) == 0:
                single.append(ele)
                continue
            ele_key = []
            for i in range(0, len(ele) - 1):
                diff = ord(ele[i + 1]) - ord(ele[i])
                if diff < 0:
                    diff += 26
                if diff < 10:
                    ele_key.append('0')
                    ele_key.append(str(diff))
                else:
                    ele_key.append(str(diff))
            k = ''.join(ele_key)
            if k in str_to_diff:
                str_to_diff[k].append(ele)
            else:
                str_to_diff[k] = [ele]
        if not single:
            return [ele for ele in str_to_diff.values()]
        return [ele for ele in str_to_diff.values()].extend(single)
if __name__ == '__main__':
    s = Solution()
    x = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(s.groupStrings(x))
