# auto_emoji

## Note: recommend using Python 3.6.x (latest) -- discord library requires some finagling on Python 3.7.x

This is fairly simple script which attempts to automatically add an emoji to a message on Discord. Which user's message gets which emoji on which server is determined by the "user_list.txt". User and emoji ID are required for this to work.

Getting user/server ID
https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-

Emojis should be stored within the user_list.txt file in the following format:
USERID SERVERID emoji_name:111222333444555666

It's also possible to add an emoji using unicode, but could not get the python script to import the each unicode string as-is

A prompt for capturing user credentials would likely make this more secure. Alternatively, import them as an environment variable (not sure how secure this is), or store them in a separate file as a class, as demonstrated here (not very secure) 

## To have this run periodically in the background via crontab:

from terminal:
    
    crontab -e
    
press 'i' for insert mode, and enter the following

    * * * * * /usr/local/bin/python3.6 /Users/user/Documents/auto_emoji.py >> ~/cron.log 2>&1
    
`* * * * *` represents the cron schedule: `minutes hours day(of the month) months day(of the week)` -- see [crontab.guru](https://crontab.guru/) for crontab tips/examples 

the next piece `/usr/local/bin/python3.6` represents the Python3.6 'executable' path, and `/Users/user/Documents/auto_emoji.py` is where ever the Python script is saved

`>> ~/cron.log 2>&1` specifies to send all output (STDERR and STDOUT) to cron.log, instead of an email (recommend)

Finally, make sure to give the python file itself executable permissions:

`chmod +x <python file>`

