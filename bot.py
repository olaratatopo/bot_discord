import discord
import random
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "CRUZ"
    
def tirada_dado():
    dado = random.randint(1,6)
    if dado == 1:
        return "Salio 1"
    elif dado == 2:
        return "Salio 2"
    elif dado == 3:
        return "Salio 3"
    elif dado == 4:
        return "Salio 4"
    elif dado == 5:
        return "Salio 5"
    elif dado == 6:
        return "Salio 6"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$dado'):
        await message.channel.send(tirada_dado())
    else:
        await message.channel.send(message.content)

client.run("")