from threading import Lock


class H2O:
    def __init__(self):
        self.o = Lock()
        self.h1 = Lock()
        self.h2 = Lock()
        self.counter_h = False

        self.h2.acquire()
        self.o.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        if not self.counter_h:
            self.h1.acquire()
        else:
            self.h2.acquire()
        releaseHydrogen()
        self.counter_h = self.counter_h ^ True
        if not self.counter_h:
            self.o.release()
        else:
            self.h2.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.acquire()
        releaseOxygen()
        self.h1.release()



from threading import Semaphore
from threading import Barrier

class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar_assembling = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        with self.sem_h:
            self.bar_assembling.wait()

            releaseHydrogen()



    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        with self.sem_o:
            self.bar_assembling.wait()

            releaseOxygen()
