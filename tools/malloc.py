#!/usr/bin/env python

import sys
import time

mb = int(sys.argv[1])
sleep = int(sys.argv[2])
out = open(sys.argv[3], 'w')

out.write('will malloc %s MB\n' % mb)

s = 'a' * mb * 1024 * 1024

out.write('done, sleeping for %s seconds\n' % sleep)

time.sleep(sleep)

out.write('done\n')
