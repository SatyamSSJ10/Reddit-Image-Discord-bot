# Reddit-Image-Discord-bot
A Discord bot made with AsyncPRAW to fetch images from reddit and post it on your discord server

## Packages
AsyncPRAW, os, Asyncio, wget, mimetypes, discord.py, requests, gc, dotenv, pandas

## Make .env File 

DISCORD_TOKEN = "Value"

DISCORD_GUILD = "Value"

CHANNEL = "Value"

REDDIT_ID = "Value" ``` your Reddit App ID```

REDDIT_SECRET = "Value" ``` your Reddit App Secret```

SUBREDDIT="Value"

## Deploying

```
python3 imager.py
```


## Working
Fetches the links in the posts.

checks if the link in the post is Image, HTML or any other.

downloads if image.

checks image size (discord upload limit is 8MB).

if smaller than 8Mb posts on discord channel.

delete the image.

## To Do List (Will be updated as soon as I get more Ideas)

Multiple subbreddit addition through discord directly.

Multiple channel addition through discord directly.

Discord Admin only access.

Integrate Sauce Nao API.

