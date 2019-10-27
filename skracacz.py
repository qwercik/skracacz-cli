#!/usr/bin/env python3

import sys
import re
import requests

FRONTEND_URL = 'https://s.komputeryk.pl'
API_URL = 'https://s.komputeryk.pl/api'

EXIT_SUCCESS = 0
EXIT_INCORRECT_USAGE = 1
EXIT_INVALID_URL = 2
EXIT_INVALID_TOKEN = 3
EXIT_REQUEST_ERROR = 4

def printHelp(file=sys.stdout):
    print('Use:', sys.argv[0], '<url>', '[token]', file=file)
    print('<url> - link you want to shorten', file=file)
    print('[token] - (optional) your shortcut name (e.g. /helloworld)', file=file)

def urlValid(url):
    return re.match(r'^((https?:\/\/)?(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})$', url)

def tokenValid(token):
    return re.match(r'^[A-Za-z0-9]+$', token)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Incorrect usage', file=sys.stderr)
        printHelp(sys.stderr)
        sys.exit(EXIT_INCORRECT_USAGE)
    elif sys.argv[1] in ['-h', '--help']:
        printHelp(sys.stdout)
        sys.exit(EXIT_SUCCESS)
        
    url = sys.argv[1]
    data = { 'url': url }
    
    if not urlValid(url):
        print('Invalid URL', file=sys.stderr)
        sys.exit(EXIT_INVALID_URL)
    
    if len(sys.argv) == 3:
        token = sys.argv[2]

        if not tokenValid(token):
            print('Invalid token', file=sys.stderr)
            sys.exit(EXIT_INVALID_TOKEN)

        data = { **data, 'token': token }

    try:
        response = requests.post(API_URL + '/aliases', json=data)
        response_data = response.json()

        if response.status_code == 400:
            print(response_data['message'])
            sys.exit(EXIT_REQUEST_ERROR)
        
        print(FRONTEND_URL + '/' + response_data['token'])
    except:
        print('Error with communicating with server')

if __name__ == '__main__':
    main()
