d = {'a': 1, 'b': 2, 'c': 3}

print d.get('d')
if 'd' in d:
    print d['d']
else:
    print '{} not in d, lets put {} = {}'.format('d', 'd', 4)
    d['d'] = 4

print d
print d.pop('d')
print d.get('d', 'Not Exist')
