import os

print os.getcwd()

os.chdir("../../../")

print os.getcwd()

odd_list = []
even_list = []
if os.path.exists("111.txt"):
    with open("111.txt") as lines:
        for line in lines:
            print line
            split = line.split(',')
            print type(split)
            print len(split)
            try:
                if line.find(',') > 0:
                    (part0, part1) = line.replace(' ', '').split(',', 1)
                    print 'part0 = ', part0, ',part1 = ', part1
                    if int(part0) % 2 == 0:
                        even_list.append(part1)
                    else:
                        odd_list.append(part1)
            except ValueError as e:
                print e
                print 'Unable to use comma  to split {} due to error {} '.format(line, str(e))

print odd_list
print even_list

with open('odd.txt', 'w') as odd_file, open('even.txt', 'w') as even_file:
    for odd in odd_list:
        odd_file.write(odd)
    for even in even_list:
        even_file.write(even)

try:
    odd_file = open('odd.txt', 'r')
    # print the first line
    print odd_file.readline()
    # print the remaining lines
    print odd_file.readlines()
    even_file = open('even.txt', 'r')
    print even_file.readline()
    print even_file.readlines()
except IOError as err:
    print str(err)
finally:
    if 'odd_file' in locals():
        odd_file.close()
    if 'even_file' in locals():
        even_file.close()
