#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import PyPDF2, sys
merger = PyPDF2.PdfFileMerger()
#could sorted by sorted()
for temp in sys.argv[1:]:
    f = open(temp, 'rb')
    merger.append(f)
    print '%s Done.' % temp
merger.write(open("test_out2.pdf", 'wb'))
# merger.merge(position=0, fileobj=path2)
# >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'jack': 4098, 'guido': 4127}
# >>> dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}
# >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# >>> for k, v in knights.items():
# ...     print(k, v)
# ...
# gallahad the pure
# robin the brave
# >>> questions = ['name', 'quest', 'favorite color']
# >>> answers = ['lancelot', 'the holy grail', 'blue']
# >>> for q, a in zip(questions, answers):
# ...     print('What is your {0}?  It is {1}.'.format(q, a))
# ...
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

# >>> for i in reversed(range(1, 10, 2)):
# ...     print(i)
# >>> import shutil
# >>> shutil.copyfile('data.db', 'archive.db')
# >>> shutil.move('/build/executables', 'installdir')
# >>> import glob
# >>> glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']
# The getopt module processes sys.argv. More powerful and flexible command line processing is provided by the argparse module.
# >>> sys.stderr.write('Warning, log file not found starting a new one\n')
# >>> import re
# >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']
# >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# 'cat in the hat'
# >>> 'tea for too'.replace('too', 'two')
# 'tea for two'
# >>> import math
# >>> math.cos(math.pi / 4)
# 0.70710678118654757
# >>> math.log(1024, 2)
# 10.0
# >>> import random
# >>> random.choice(['apple', 'pear', 'banana'])
# 'apple'
# >>> random.sample(range(100), 10) # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
# >>> random.random() # random float
# 0.17970987693706186
# >>> random.randrange(6) # random integer chosen from range(6)
# 4
# The SciPy project has many other modules for numerical computations.
# >>> from urllib.request import urlopen
# >>> for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
# ... line = line.decode('utf-8') # Decoding the binary data to text.
# ... if 'EST' in line or 'EDT' in line: # look for Eastern Time
# ... print(line)

# Nov. 25, 09:43:32 PM EST
# >>> import smtplib
# >>> server = smtplib.SMTP('localhost')
# >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# ... """To: jcaesar@example.org
# ... From: soothsayer@example.org
# ...
# ... Beware the Ides of March.
# ... """)
# >>> server.quit()
# >>> from datetime import date
# >>> now = date.today()
# >>> now
# datetime.date(2003, 12, 2)
# >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
# >>> # dates support calendar arithmetic
# >>> birthday = date(1964, 7, 31)
# >>> age = now - birthday
# >>> age.days
# 14368
# >>> import zlib
# >>> s = b'witch which has which witches wrist watch'
# >>> len(s)
# 41
# >>> t = zlib.compress(s)
# >>> len(t)
# 37
# >>> zlib.decompress(t)
# b'witch which has which witches wrist watch'
# >>> zlib.crc32(s)
# 226805979
# >>> from timeit import Timer
# >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.57535828626024577
# >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.54962537085770791
# the profile and pstats modules provide tools for identifying time critical sections in larger blocks of code.
