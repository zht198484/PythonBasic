class A1(object):
    def __init__(self):
        print 'Enter A'
        print 'Leave A'


class B1(A1):
    def __init__(self):
        print 'Enter B'
        super(B1, self).__init__()
        print 'Leave B'


class C1(A1):
    def __init__(self):
        print("Enter C")
        super(C1, self).__init__()
        print("Leave C")


class D1(A1):
    def __init__(self):
        print("Enter D")
        super(D1, self).__init__()
        print("Leave D")


# super always and may only be used in __init__ method
# try your best to avoid using multiple inheritance
class E1(B1, C1, D1):
    def __init__(self):
        print("Enter E")
        super(E1, self).__init__()
        print("Leave E")


print E1.mro()
E1()
