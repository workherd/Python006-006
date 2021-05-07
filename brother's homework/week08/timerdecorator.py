
import time


class NiceTimer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        begin = time.perf_counter()
        ret = self.func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{self.func.__name__} ran {end-begin:0.4f} seconds')
        return ret


@NiceTimer
def hello_world(who):
    time.sleep(4)
    print(f"hello world, {who}")


if __name__ == '__main__':
    hello_world("Python")
