import os

print os.getcwd()

os.chdir("../../../")

print os.getcwd()

if os.path.exists("111.txt"):
    with open("111.txt") as lines:
        for line in lines:
            print line
            split = line.split(',')
            print type(split)
            print len(split)
            try:
                if line.find(',') > 0:
                    (part0, part1) = line.split(',', 1)
                    print 'part0 = ', part0, ',part1 = ', part1
            except ValueError as e:
                print e
                print 'Unable to use comma  to split {} due to error {} '.format(line, str(e))
