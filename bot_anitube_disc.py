from bs4 import BeautifulSoup
import os
import requests
from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv


load_dotenv()
list_anitube = []
TOKEN = os.getenv("TOKEN")

USUARIOS_ID=[813159518514315315]

def get_anitube():
    url = 'https://anitube.news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    anitube_list = []
    
    for item in soup.find_all('div', class_='epiItem'):
        title= item.find('a')['title']
        link = item.find('a')['href']
        anitube_list.append(f"{title}: {link}\n")
    
    return anitube_list 

@tasks.loop(hours=24)
async def enviar_anitube():
    anitube_list = get_anitube()
    if not anitube_list:
        return
    
    mensagem = "🎬 **Novos episódios no Anitube hoje:**\n" + "\n".join(anitube_list)

    for user_id in USUARIOS_ID:
        try:
            user = await bot.fetch_user(user_id)
            if user:
                await user.send(mensagem)
        except Exception as e:
            print(f"Erro ao enviar mensagem para o usuário {user_id}: {e}")

@enviar_anitube.before_loop
async def antes_da_task():
    await bot.wait_until_ready()            

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'bot iniciado como {bot.user}')
    enviar_anitube.start()

@bot.command()
async def anitube(ctx):
    anitube_list = get_anitube()
    if anitube_list:
        response = "\n".join(anitube_list)
        await ctx.send(f"**Últimos lançamentos do Anitube:**\n{response}")
    else:
        await ctx.send("Não foi possível obter os lançamentos do Anitube no momento.")    

bot.run(TOKEN)