import discord
from discord.ext import commands
from config import TOKEN  # Importa el token desde config.py

# Configura el prefijo del bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Evento cuando el bot esté listo
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando de saludo
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"¡Hola, {ctx.author.name}! 👋")

# Comando para obtener información del servidor
@bot.command(name="serverinfo")
async def serverinfo(ctx):
    server = ctx.guild
    embed = discord.Embed(
        title=f"Información de {server.name}",
        description=f"Propietario: {server.owner}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Miembros", value=server.member_count)
    embed.add_field(name="ID del Servidor", value=server.id)
    embed.set_thumbnail(url=server.icon.url if server.icon else "")
    await ctx.send(embed=embed)

# Comando de limpieza de mensajes
@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)  # Incluye el comando
    await ctx.send(f"Se eliminaron {amount} mensajes. 🗑", delete_after=3)

# Manejo de errores en los comandos
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permiso para usar este comando. ❌")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltan argumentos para este comando. ⚠️")
    else:
        await ctx.send("Ocurrió un error. 🚨")

# Inicia el bot
bot.run(TOKEN)