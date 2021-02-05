import time
from contextlib import contextmanager


class TimeIt:
    def __init__(self):
        self.calculated_time = 0

    def __enter__(self):
        self.calculated_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self)
        self.calculated_time = 0

    def __str__(self):
        if self.calculated_time:
            return f"Elapsed time: {time.time() - self.calculated_time} sec"

        return "Timer has stopped"


@contextmanager
def also_time_it():
    try:
        calculated_time = time.time()
        yield calculated_time
    finally:
        print(f"Elapsed time: {time.time() - calculated_time} sec")


def main():

    with TimeIt() as time_it:
        time.sleep(1)

    with also_time_it() as time_it2:
        time.sleep(1)


if __name__ == '__main__':
    main()
