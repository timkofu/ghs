import os

if os.getenv('CI'):
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')
