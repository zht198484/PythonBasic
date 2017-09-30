L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g

for item in g:
    print item


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3


o = odd()
for i in o:
    print i


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


fb6 = fib(6)
for i in fb6:
    print i
