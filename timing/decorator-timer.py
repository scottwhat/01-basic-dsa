import time


def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1

        print(f'{func.__name__} ran in'
              f'{t2} seconds')

    return wrapper


@tictoc
def do_this():
    time.sleep(1.3)
    print('function do_this executed')


do_this()
