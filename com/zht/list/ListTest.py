seq = ['a', 'b', 'c']
print seq

# not recommend to insert different type
seq.insert(1, 1)
print seq

seq.append('d')
for i in seq:
    print i

print type(seq[0])
print type(seq[1])

seq.insert(1, ['a1', 'b1'])

print seq
for i in seq:
    print i

print isinstance(seq, list)


def print_seq(the_seq):
    for i in the_seq:
        if isinstance(i, list):
            print_seq(i)
        else:
            print i

print_seq(seq);