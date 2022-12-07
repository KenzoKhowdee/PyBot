# PyBot
Simple Discord Chat bot that sends messages based on chat commands
# How to Create a Discord Bot
1. Go to the Developer Portal https://discord.com/developers/applications
2. Click create New Application.
3. Fill in requested information.
4. Create a Bot clicking the bot tab and then Add Bot.
5. You can now fill information for your bot.
# Getting the Bot in your Server
1. Go to the OAuth2 tab and define the bots Scopes.
2. Go the Bot Permissions page and select the desired permissions.
3. Copy the URL and paste it into your browers.
# Reference
https://discordpy.readthedocs.io/en/stable/discord.html
# dotenv Integration
Github does not let you upload .env files. This means you will have to create your own.
This bot requires a .env file to store your token. If you do not want to use a .env file you can just create a TOKEN variable and 
give it a string with your token in it. This is not recommended as it is not secure.
1. You need to make sure that you install the dotenv library
2. Then you will need to create a .env file in the root directory as your PyBot. 
3. The best way is to just write ".env" using the new file feature in VSC.
4. Alternativly you can create a file with just the .env extension in anyway you feel.
5. In this file you will need to write - TOKEN = "your bot token" .
# dotenv Documentation
documentation - https://pypi.org/project/python-dotenv/
