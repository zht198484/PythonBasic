from time import sleep, ctime


def func1():
    print 'start func1 at : ', ctime()
    sleep(4)
    print 'func1 is done at : ', ctime()


def func2():
    print 'start func2 at : ', ctime()
    sleep(2)
    print 'func2 is done at : ', ctime()


func1()
func2()
