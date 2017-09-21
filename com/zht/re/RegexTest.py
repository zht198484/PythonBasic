# \w [A-Za-z0-9] \W [^A-Za-z0-9]
# \d [0-9] \D [^0-9]
# \s [\n\t\r\v\f] \S
# \d{3}-\d{3}-\d{4}  American tel
# \w+@\w+\.com
import re

m = re.match('\w', 'foo')
if m is not None:
    print m.group()
else:
    print '\w not match with foo'

m = re.match('foo', 'seafood')
if m is None:
    print 'foo not match with seafood'
else:
    print m.group()

m = re.search('foo', 'seafood')
if m is None:
    print 'foo not match with seafood'
else:
    print m.group()
