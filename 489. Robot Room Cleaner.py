class Robot:
   def move(self):
       """
       返回往前走能不能走
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       左转向
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       右转向
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       扫当前的
       Clean the current cell.
       :rtype void
       """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = set()
        self.dfs(0, 0, 0, robot, directions, visited)

    def dfs(self, x, y, dir, robot, directions, visited):
        robot.clean()
        visited.add((x, y))
        for i in range(4):
            next_dir = (dir + i) % 4
            next_x = x + directions[next_dir][0]
            next_y = y + directions[next_dir][1]
            if (next_x, next_y) not in visited and robot.move():
                self.dfs(next_x, next_y, next_dir, robot, directions, visited)

            robot.turnRight()

        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
