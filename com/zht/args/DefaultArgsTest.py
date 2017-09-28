def newfoo(arg1, arg2, *nkw, **kw):
    print 'arg1:', arg1
    print 'arg2:', arg2
    for eachNkw in nkw:
        print 'additional non-keyword arg:', eachNkw
    for eachKw in kw.keys():
        print 'additional keyword arg: %s=%s' % (eachKw, kw[eachKw])


newfoo('a', 'b', 'c', d='dValue', e='eValue')
