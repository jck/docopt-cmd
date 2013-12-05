"""Do somethings

Usage:
    example.py [-vfr] do (a|b)

Options:
    -v --verbose    Be verbose.
    -f --force      Force.
    -r --random     Huh?.
"""
from docopt import docopt
from docopt_cmd import cmd

def main():
    args = docopt(__doc__)
    #print(args)

    cmd.dispatch(args)

#explicitly specify spec and options to pass as arguments
@cmd('do a', force='--force')
def something(force):
    print('doing a')
    print(force)

#or use magic
@cmd
def do_b(random):
    print 'doing b'
    print random

if __name__ == '__main__':
    main()
