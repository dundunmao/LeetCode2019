class Solution:
    def compress(self, chars):
        # base case
        start = None
        count = 1
        res = []
        for i in range(len(chars)):
            if chars[i] != start:
                if count > 1:
                    res.append(str(count))
                res.append(chars[i])
                start = chars[i]
                count = 1
            else:
                count += 1
        if count > 1:
            res.append(str(count))
        chars = res
        return len(chars)


class Solution1:
    def compress(self, chars) -> int:
        # base case
        start = chars[0]
        count = 1
        record_place = 1
        # general case
        for i in range(1, len(chars)):
            if chars[i] != start:
                record_place = self.add_count(count, record_place, chars)
                chars[record_place] = chars[i]
                record_place += 1
                count = 1
                start = chars[i]
            else:
                count += 1
        # g -> f
        record_place = self.add_count(count, record_place, chars)
        return record_place

    def add_count(self, count, record_place, chars):
        if count > 1:
            for k in range(len(str(count))):
                chars[record_place] = str(count)[k]
                record_place += 1
        return record_place


# fake base case


class Solution:
    def compress(self, chars) -> int:
        # base case
        start = None
        count = 1
        record_place = 0
        # general case
        for i in range(0, len(chars)):
            if chars[i] != start:
                record_place = self.add_count(count, record_place, chars)
                chars[record_place] = chars[i]
                record_place += 1
                count = 1
                start = chars[i]
            else:
                count += 1
        # g -> f
        record_place = self.add_count(count, record_place, chars)
        return record_place

    def add_count(self, count, record_place, chars):
        if count > 1:
            for k in range(len(str(count))):
                chars[record_place] = str(count)[k]
                record_place += 1
        return record_place

s = Solution1()
a = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(s.compress(a))
