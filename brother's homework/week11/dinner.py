import threading
import time


class fork(object):

    def __init__(self, ID):
        self.id = ID
        self.philo = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.philo = user
            self.taken = True
            print(f"[{user}, {self.id}, 1]")
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.philo = -1
            self.taken = False
            print(f"[{user}, {self.id}, 2]")
            self.lock.notifyAll()


class PhilosopherAction (threading.Thread):

    def __init__(self, ID, left_fork, right_fork, semaphore, eat_times):
        threading.Thread.__init__(self)
        self.id = ID
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.semaphore = semaphore
        self.eat_times = eat_times

    def run(self):
        for i in range(self.eat_times):
            self.semaphore.acquire()
            time.sleep(0.1)
            self.left_fork.take(self.id)
            time.sleep(0.1)
            self.right_fork.take(self.id)
            print(f"[{self.id}, 0, 3]")  # eat
            time.sleep(0.1)
            self.right_fork.drop(self.id)
            self.left_fork.drop(self.id)
            self.semaphore.release()
        # print(f"Philosopher:{self.id} finished")


def main():
    num_of_philos = 5
    semaphore = threading.Semaphore(num_of_philos-1)

    forks = [fork(i) for i in range(num_of_philos)]

    eat_times = 1
    # list of philsophers
    philos = [PhilosopherAction(i, forks[i], forks[(i+1) % num_of_philos], semaphore, eat_times)
              for i in range(num_of_philos)]

    for i in range(num_of_philos):
        philos[i].start()


if __name__ == "__main__":
    main()
