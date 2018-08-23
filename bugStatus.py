#! /usr/bin/env python

import enum

class BugStatus(enum.Enum):

	new = 7
	incomplete = 12
	complete = 10
	invalid = 4
	wontfix = 3
	in_progress = 2


print("*"*60)
print("Bug status name : {}".format(BugStatus.wontfix.name))
print("Bug status value : {}".format(BugStatus.wontfix.value))
print("*"*60)
for status in BugStatus:

	print("{:30} {}".format(status.name, status.value))


print("*"*60)
try:
	print('\n'.join(''+sorted(s.name) for s in BugStatus))
except TypeError as error:
	print('print can\'t sort {}:'.format(error))
	
