class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 1
        if len(self.stack) == 0:
            new_node = Node(price, days)
            self.stack.append(new_node)
        else:

            while len(self.stack) > 0 and self.stack[-1].price <= price:
                days += self.stack.pop().days
            new_node = Node(price, days)
            self.stack.append(new_node)
        return days


class Node:

    def __init__(self, price, days):
        self.price = price
        self.days = days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
##########简化
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 1
        if len(self.stack) != 0:
            while len(self.stack) > 0 and self.stack[-1].price <= price:
                days += self.stack.pop().days
        new_node = Node(price, days)
        self.stack.append(new_node)
        return days
