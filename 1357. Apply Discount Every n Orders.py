class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = dict(zip(products, prices))
        self.counter = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        """
        :param product:
        :param amount:
        :return:
        """
        self.counter += 1
        purchase = dict(zip(product, amount))
        result = 0
        for key in product:
            result += self.products[key] * purchase[key]
        if self.counter % self.n == 0:
            result *= (1 - self.discount / float(100))
        return result

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)