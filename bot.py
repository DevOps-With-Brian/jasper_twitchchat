from twitchio.ext import commands
import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=os.getenv('TOKEN'), client_id=os.getenv('CLIENT_ID'),prefix=os.getenv('BOT_PREFIX'), initial_channels=[os.getenv('CHANNEL')])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        print(message)

        if "@jasperchat" in message.content:
            print("We would then process this with rasa...")
            print(message.author.name)
            print(message.content)
            print(message.channel)
            jasper_url = os.getenv('RASA_URL')
            headers = {
                'Content-Type': 'application/json',
            }

            json_data = {
                'sender': message.author.name,
                'message': message.content,
            }

            print(json_data)

            response = requests.post(jasper_url, headers=headers, json=json_data)
            parsed = json.loads(response.content)
            print(parsed)
            jasper_response = parsed[0]['text']
            print(jasper_response)
            # Send response from Jasper
            chan = bot.get_channel(message.channel.name)
            self.loop.create_task(chan.send(jasper_response))
            
       
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)


    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        print(ctx.author.name)
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='jasper')
    async def jasper(self, ctx: commands.Context,*,message):
        print(ctx.author.name)
        print(ctx.__dict__)
        print(message)
        jasper_url = os.getenv('RASA_URL')
        headers = {
            'Content-Type': 'application/json',
        }

        json_data = {
            'sender': ctx.author.name,
            'message': message,
        }

        print(json_data)

        response = requests.post(jasper_url, headers=headers, json=json_data)
        parsed = json.loads(response.content)
        print(parsed)
        jasper_response = parsed[0]['text']
        print(jasper_response)
        # Send response from Jasper
        await ctx.send(jasper_response)


bot = Bot()
bot.run()