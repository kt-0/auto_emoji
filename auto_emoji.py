#!/usr/bin/env python3.6

import discord, asyncio, os, re
from assets.creds import Credentials

client = discord.Client()

# if file doesn't exist, create it
if not os.path.isfile("assets/user_list.txt"):
	users = []

# if file exists, read from it
else:
	with open("assets/user_list.txt", "r") as f:

		fn = (lambda x: x.split())
		# create nested dictionary like {user_id: {server_id: emoji_id}}
		users = {fn(item)[0]:{fn(item)[1]:fn(item)[2]} for item in f.read().splitlines()}


@client.event
async def on_ready():
 	print('Logged in as: ', client.user.name)
 	print('------')

@client.event
async def on_message(message):

	server_id = getattr(message.server, 'id', 'None')
	
	# filters out private messages
	if server_id != 'None':
		if (users.get(message.author.id, {}).get(message.server.id)):
			await client.add_reaction(message, users[message.author.id][message.server.id])

client.run(Credentials.email, Credentials.password)
