class DoubleLink:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.tail = DoubleLink(homepage)
        self.head = self.tail
        self.tail.next = self.head
        self.head.pre = self.tail

    def visit(self, url: str) -> None:
        prev = self.head

        if self.head.next:
            dump = self.head.next
        else:
            dump = None

        self.head = DoubleLink(url)
        self.head.pre = prev
        prev.next = self.head

        if dump:
            dump.pre = None

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.pre:
            self.head = self.head.pre
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.val

    # Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)