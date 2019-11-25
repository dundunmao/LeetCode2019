class StringIterator:

    def __init__(self, compressedString: str):
        self.string_array = []
        i = 0
        char = ''
        num = 0
        start = 0
        while i < len(compressedString):
            if compressedString[i].isalpha():
                char = compressedString[i]
                i += 1
                start = i
            while i < len(compressedString) and compressedString[i].isdigit():
                i += 1
            num = int(compressedString[start: i])
            for j in range(num):
                self.string_array.append(char)
        self.pointer = 0

    def next(self) -> str:
        if self.pointer < len(self.string_array):
            cur = self.string_array[self.pointer]
            self.pointer += 1
            return cur
        else:
            return ' '

    def hasNext(self) -> bool:
        if self.pointer < len(self.string_array):
            return True
        else:
            return False

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

########不超时的

class StringIterator1:

    def __init__(self, compressedString: str):
        self.string = compressedString
        self.pointer = 0
        self.num = 0
        self.char = ' '

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:  # 是char出现的位置
            self.char = self.string[self.pointer]
            self.pointer += 1
            start = self.pointer
            while self.pointer < len(self.string) and self.string[self.pointer].isdigit():
                self.pointer += 1
            self.num = int(self.string[start: self.pointer])
        self.num -= 1
        return self.char

    def hasNext(self) -> bool:
        if self.pointer < len(self.string) or self.num != 0:
            return True
        else:
            return False

# Your StringIterator object will be instantiated and called as such:
compressedString = 'L1e2t1C1o1d1e1'
obj = StringIterator1(compressedString)
param_1 = obj.next()
param_2 = obj.hasNext()
