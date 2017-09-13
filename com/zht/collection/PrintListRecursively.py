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

seq.insert(1, ['a1', ['b2','c2']])

print seq
for i in seq:
    print i

print isinstance(seq, list)


def print_seq(the_seq, indent=False, level=0):
    for list_item in the_seq:
        if isinstance(list_item, list):
            print_seq(list_item, indent, level + 1)
        else:
            tab_str = ''
            if indent:
                tab_str = '\t' * level
            print tab_str, list_item


print_seq(seq, True)
