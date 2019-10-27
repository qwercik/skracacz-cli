#!/usr/bin/env python3

import sys

FRONTEND_URL = 'https://s.komputeryk.pl'
API_URL = 'https://s.komputeryk.pl/api'

def printHelp(file=sys.stdout):
    print('Use:', sys.argv[0], '<url>', '[token]', file=file)
    print('<url> - link you want to shorten', file=file)
    print('[token] - (optional) your shortcut name (e.g. /helloworld)', file=file)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Incorrect usage', file=sys.stderr)
        printHelp(sys.stderr)
    elif sys.argv[1] in ['-h', '--help']:
        printHelp(sys.stdout)
    else:
        url = sys.argv[1]
        data = { 'url': url }

        if len(sys.argv) == 3:
            token = sys.argv[2]
            data = { **data, 'token': token }

        print(data)


if __name__ == '__main__':
    main()
