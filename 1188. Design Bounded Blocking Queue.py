import collections
import threading


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.pushing = threading.Semaphore(capacity) #threading.Semaphore(x)同时运行x个thread进入资源
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()

        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire() # use a Lock so only a single thread can modify the actual queue at once.

        self.queue.append(element)

        self.editing.release()
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()

        res = self.queue.popleft()

        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.queue)


from collections import deque
from threading import Lock


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en = Lock()
        self.de = Lock()
        self.q = deque()
        self.capacity = capacity
        self.de.acquire()

    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.q.append(element)
        if len(self.q) < self.capacity:
            self.en.release()
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        val = self.q.popleft()
        if len(self.q):
            self.de.release()
        if val and self.en.locked():
            self.en.release()
        return val

    def size(self) -> int:
        return len(self.q)
