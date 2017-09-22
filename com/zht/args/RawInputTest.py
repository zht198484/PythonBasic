from sys import argv

script, user_name = argv

prompt = '> '

print 'hi, %s, welcome to %s world' % (user_name, script)
print 'Are you a boy'
gender = raw_input(prompt)

print 'The answer to your gender is %r!' % gender
