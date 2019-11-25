# Logger Rate Limiter 记录速率限制器
# 这道题让我们设计一个记录系统每次接受信息并保存时间戳，然后让我们打印出该消息，前提是最近10秒内没有打印出这个消息


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if self.hash.has_key(message):
            if timestamp - self.hash[message] >= 10:
                self.hash[message] = timestamp
                return True
            else:
                return False
        else:
            self.hash[message] = timestamp
            return True

if __name__ == "__main__":
    # a = [-3, -1, 4, 1, 5]
    # k = 2
    s = "-12"
    # t = "ab"
    x = Logger()
    print x.shouldPrintMessage(1,"foo")
    print x.shouldPrintMessage(2,"bar")
    print x.shouldPrintMessage(3,"foo")
    print x.shouldPrintMessage(8,"bar")
    print x.shouldPrintMessage(10,"foo")
    print x.shouldPrintMessage(11,"foo")
