# bot.py
import os
import asyncio
import asyncpraw
import wget
import mimetypes
import pandas as pd
import discord
import requests
import gc
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')
REDDIT_ID = os.getenv('REDDIT_ID')
REDDIT_SECRET = os.getenv('REDDIT_SECRET')
CHANNEL = os.getenv('CHANNEL')
client = discord.Client()

#gets the link type
def tipe(link, strict=True):
    link_type, _ = mimetypes.guess_type(link)
    if link_type is None and strict:
        link_type = "text/html"
    '''
    if link_type is None and strict:
        u = urllib.request.urlopen(link)
        link_type = u.info().gettype() # or using: u.headers.gettype() 
    '''
    return link_type

#downloads the Image from link
def down(z, str):
    r = wget.download(z, str)

#Deletes the file from system    
def remove_file(str1):
    if os.path.exists(str1):
        os.remove(str1)
    else:
        print("The file does not exist") 

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(id=int(CHANNEL))
    
    reddit = asyncpraw.Reddit (client_id=REDDIT_ID,		         # your client id
							client_secret=REDDIT_SECRET,	             # your client secret
							user_agent="Mozilla",	                 # your user agent
                            check_for_async=False)
    
    subreddit = await reddit.subreddit("hentai")
    
    async for submission in subreddit.stream.submissions():                       
        if ( tipe(submission.url) != "text/html"):  #Sorts out the wrong image extentions                                                     
            print(submission.url)
            down(submission.url,"x.jpg")    #download the image
            print('Image Successfully Downloaded', submission.url)
            size = os.path.getsize("x.jpg")
            if size >= 8000000:
                remove_file("x.jpg")
            else:
                await channel.send(file=discord.File('x.jpg'))       #Sending File Message ETC.
                remove_file("x.jpg")
            await asyncio.sleep(0)
            del submission  #Removing garbage values
            gc.collect()    #Removing garbage values
client.run(TOKEN)
