class Solution:
    def read(self, buf, n):
        temp = [''] * 4 ##新开一个空间，让buf4往里面读数
        index = 0
        while True:
            count = read4(temp)
            size = min(count, n - index) # 看还够不够都放进buf里取的
            for i in range(size): #对于读进来的数把buf里存入buf4里的数
                buf[index] = temp[i]
                index += 1  #这里的idx记的是在我自己的内存里存到第几位了
            if index == n or count < 4: # 如果file读完了, 或者到达buf到头了，就return
                return index
