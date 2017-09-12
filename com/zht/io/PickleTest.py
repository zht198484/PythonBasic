import os
import pickle

print os.getcwd()
os.chdir('../../../')
print os.getcwd()

data = []
try:
    with open('111.txt') as f:
        data = f.readlines()
except IOError as err:
    print 'Fail to read from 111.txt ', str(err)

print data

try:
    with open('111.pickle', 'wb') as fp:
        print 'Dump {} to 111.pickle'.format(data)
        pickle.dump(data, fp)
except IOError as err:
    print 'Fail to open 111.pickle in wb mode', str(err)
except pickle.PickleError as err:
    print 'Fail to dump {} to 111.pickle'.format(data)

try:
    with open('111.pickle', 'rb') as fp:
        print 'Load data from {}'.format(fp)
        load = pickle.load(fp)
        print load
except IOError as err:
    print 'Fail to open 111.pickle in rb mode', str(err)
except pickle.PickleError as err:
    print 'Fail to load data from 111.pickle'
