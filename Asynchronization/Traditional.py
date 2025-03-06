import time


def f1():
    print("f1 starting...")
    time.sleep(3)
    print("f1 done")
    return 10


def f2():
    print("f2 starting...")
    time.sleep(3)
    print("f2 done")
    return 20


if __name__ == '__main__':
    start_time = time.time()

    x = f1()
    y = f2()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"x: {x}, y: {y}")
    print(f"elapsed_time: {elapsed_time}") # 6s