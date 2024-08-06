#! python3
# pw.py - an insecure password locker program.

PASSWORDS = {'email': '1234554321', 'steam': '1234554321', 'lol': '1234554321'}

import sys, pyperclip # type: ignore
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
 pyperclip.copy(PASSWORDS[account])
 print('Password for ' + account + ' copied to clipboard.')
else:
 print('There is no account named ' + account)
