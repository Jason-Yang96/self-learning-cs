from multiprocessing import Process
import os

def foo():
    print("child", os.getpid())
    print("parent", os.getppid())

if __name__ == "__main__":
    print("parent process", os.getpid())
    child = Process(target=foo).start()