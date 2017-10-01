L = range(100)
print L

# the last 10
print L[-10:]

# copy L
L1 = L[:]
print id(L)
print id(L1)

# fetch every 5 numbers
print L[::5]

# slice of tuple is still tuple
print type((1, 2, 3, 4, 5)[-3:])

print 'abcdef'[1:3] == 'b' + 'c'

print id('bc')
print id('b' + 'c')
print id('abcdef'[1:3])
