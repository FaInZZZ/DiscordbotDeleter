import discord

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

#Change target user id
TARGET_DELETE_USER_ID = 526795010583035914
#User with !shutdown command
TARGET_SHUTDOWN_USER_ID = 747886601027322058

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == TARGET_DELETE_USER_ID: 
        try:
            await message.delete()                               #Change this for ouput text
            await message.channel.send(f"{message.author.mention} Talar Fö Myki (Detection)")
        except discord.Forbidden:
            print("no permission")
        except discord.NotFound:
            print("not found.")
        except discord.HTTPException as e:
            print(f"error: {e}")

    if message.content.startswith('!shutdown'):
        if message.author.id == TARGET_SHUTDOWN_USER_ID:
            await message.channel.send("Shutting down")
            await client.close()

#Change Discord bot toekn
client.run('MTIxNzc4NzY2MDIwMzIwMDUxMg.Gfis8g.NaqYhEPIh7sLfxMb8f044BQvzGmhIsZaw2xeEE')
