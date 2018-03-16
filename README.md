# auto_emoji

This is fairly simple script which attempts to automatically add an emoji to a message on Discord. Which user's message gets which emoji on which server is determined by the "user_list.txt". User and emoji ID are required for this to work.

Getting user/server ID
https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-

Emojis should be stored within the user_list.txt file in the following format:
USERID SERVERID emoji_name:111222333444555666

It's also possible to add an emoji using unicode, but could not get the python script to import the each unicode string as-is

A prompt for capturing user credentials would likely make this more secure. Alternatively, import them as an environment variable (not sure how secure this is), or store them in a separate file as a class, as demonstrated here (not very secure) 
