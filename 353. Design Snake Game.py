from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """

        self.snake = deque()
        self.snake.append([0, 0])
        self.snake_set = set()
        self.snake_set.add((0, 0))
        self.score = 0
        self.food = deque()
        for ele in food:
            self.food.append(ele)
        self.width = width
        self.height = height
        self.directions = {"U": [-1, 0], "L": [0, -1], "R": [0, 1], "D": [1, 0]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[0]
        dx = self.directions[direction][0]
        dy = self.directions[direction][1]
        new_head = [head[0] + dx, head[1] + dy]
        new_head_tuple = (head[0] + dx, head[1] + dy)
        # out of boundary
        if new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width:
            return -1

        # eat food
        if len(self.food) > 0 and self.food[0] == new_head:
            self.score += 1
            self.food.popleft()
        else: # 如果不吃，尾巴就要删掉，如果吃，尾巴不动
            tail = self.snake.pop()
            self.snake_set.remove((tail[0], tail[1]))

        # add head 最后加头，因为尾巴删掉后，头正好占了尾巴的位置是允许的
        if new_head_tuple in self.snake_set:
            return -1

        self.snake.appendleft(new_head)
        self.snake_set.add(new_head_tuple)
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

width = 3
height = 2
food = [[1, 2], [0, 1]]
snake = SnakeGame(width, height, food)
print(snake.move("R"))
print(snake.move("D"))
print(snake.move("R"))
print(snake.move("U"))
print(snake.move("L"))
print(snake.move("U"))
