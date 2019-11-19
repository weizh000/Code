import sys

for argv in sys.argv[1:]:
    print('ID:{} Name:{}'.format(*argv.split(':')))
