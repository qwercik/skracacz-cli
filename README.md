# Skracacz CLI
A command line frontend app for "skracacz". It let's you to shorten your link.
## Usage
You have to provide a URL (that you would like to shorten) as the first argument.
```bash
$ skracacz.py http://github.com/qwercik
https://s.komputeryk.pl/GLrDgwtzcm
```

The second argument is optional - you give it when you would like to specify the token (shortcut name).
```bash
$ skracacz.py http://github.com/qwercik mygithub
https://s.komputeryk.pl/mygithub
```
