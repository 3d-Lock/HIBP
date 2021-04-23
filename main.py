# With this little simple python script you can check whether your password is in a data leak from haveibeenpwned.com
#
# You can get the required password lists here: https://haveibeenpwned.com/Passwords

import sys
import hashlib

pwd = sys.argv[1]
message_digest = hashlib.sha1()
message_digest.update((bytes(pwd, encoding='utf-8')))
to_check = message_digest.hexdigest().upper()

leaked = False
with open('sha1_hashes.txt') as file:
    for line in file:
        if to_check in line:
            print(f'Your password has been leaked {line.split(":"[1].strip())}'
                  f'time')
            leaked = True
            break
        if not leaked:
            print('Your password has not yet been leaked')