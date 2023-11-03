import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func(0, 0.1, .1)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t