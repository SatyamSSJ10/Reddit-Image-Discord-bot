# Reddit-Image-Discord-bot
A Discord bot made with AsyncPRAW to fetch images from reddit and post it on your discord server

##Packages
AsyncPRAW, os, Asyncio, wget, mimetypes, discord.py, requests, gc, dotenv, pandas

##Working
Fetches the links in the posts
checks if the link in the post is Image, HTML or any other
downloads if image
checks image size (discord upload limit is 8MB)
if smaller than 8Mb posts on discord channel
delete the image

##To Do List
Multiple subbreddit addition through discord directly
Multiple channel addition through discord directly
Discord Admin only access

