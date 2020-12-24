import time
import threading

fin = 0

def func1():
    while True:
        print("func1")
        time.sleep(1)
        if fin == 1:
            break


def func2():
    while True:
        print("func2")
        time.sleep(1)
        if fin == 1:
            break

def func3():
    while True:
        fin = input()
        if fin == 1:
            fin = 1
            fin = 0
            break


if __name__ == "__main__":
    thread_1 = threading.Thread(target=func1)
    thread_2 = threading.Thread(target=func2)

    thread_1.start()
    thread_2.start()
