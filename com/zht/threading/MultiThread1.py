import thread
from time import sleep, ctime


def func1():
    print 'start func1 at : ', ctime()
    sleep(4)
    print 'func1 is done at : ', ctime()


def func2():
    print 'start func2 at : ', ctime()
    sleep(2)
    print 'func2 is done at : ', ctime()


thread.start_new_thread(func1, ())
thread.start_new_thread(func2, ())
sleep(6)
