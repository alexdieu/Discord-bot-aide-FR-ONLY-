
import discord
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot
from random import randint
from discord.ext import commands
from platform import python_version
import os
import platform

BOT_PREFIX = ('PREFIXE_DU_BOT')
TOKEN = 'TOKEN_DU_BOT'
OWNERS = [123456789, 123456789]
BLACKLIST = []
client = Bot(command_prefix=BOT_PREFIX)

async def status_task():
	while True:
		await client.change_presence(activity=discord.Game("avec vous!"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("avec ALEXDIEU !"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("VOTRE_PREFIXE_DE_BOT Aide"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("avec des humains !"))
		await asyncio.sleep(10)

@client.event
async def on_ready():
	client.loop.create_task(status_task())
	print('Enregistré en tant que ' + client.user.name)
	print("Discord.py la version de l'API:", discord.__version__)
	print("Version de Python:", platform.python_version())
	print("Qui fonctionne sous:", platform.system(), platform.release(), "(" + os.name + ")")
	print('-------------------')

@client.command(name='info', pass_context=True)
async def info(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		e = discord.Embed(description='ALEXDIEU prog info ', color=0x00FF00)
		e.set_author(name="Informations sur le bot")
		e.add_field(name="Créateur:", value="ALEXDIEU", inline=True)
		e.add_field(name="Version de Python:", value="{0}".format(python_version()), inline=True)
		e.add_field(name="Préfixe:", value="VOTRE_PREFIXE_ICI ", inline=False)
		e.set_footer(text="Demandé par  {0}".format(context.message.author))
		await context.message.channel.send(embed=e)

@client.command(name='infosurleserveur', pass_context=True)
async def serverinfo(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		server = context.message.guild
		roles = [x.name for x in server.roles]
		role_length = len(roles)
		if role_length > 50:
			roles = roles[:50]
			roles.append('>>>> Montre les[50/%s] Roles' % len(roles))
		roles = ', '.join(roles)
		channelz = len(server.channels)
		time = str(server.created_at)
		time = time.split(' ')
		time = time[0]
		embed = discord.Embed(description='%s ' % (str(server)), title='**Nom du serveur:**', color=0x00FF00)
		embed.set_thumbnail(url=server.icon_url)
		embed.add_field(name='__PROPRIETAIRE__', value=str(server.owner) + '\n' + str(server.owner.id))
		embed.add_field(name='__ID DU SERVEUR__', value=str(server.id))
		embed.add_field(name='__NB DE MEMBRES__', value=str(server.member_count))
		embed.add_field(name='__SALONS VOCAUX/TEXTUELS__', value=str(channelz))
		embed.add_field(name='__Roles (%s)__' % str(role_length), value=roles)
		embed.set_footer(text='Créé à : %s' % time)
		await context.message.channel.send(embed=embed)

@client.command(name='ping', pass_context=True)
async def ping(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(color=0x00FF00)
		embed.set_footer(text='requete pong par {0}'.format(context.message.author))
		embed.add_field(name='Pong!', value=':ping_pong:', inline=True)
		await context.message.channel.send(embed=embed)

@client.command(name='invite', pass_context=True)
async def invite(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('Je vous ai envoyé un message en MP !')
		await context.message.channel.send('Invitez moi en cliquant ici: https://discordapp.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot&permissions=8')


@client.command(name='server', pass_context=True)
async def server(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('Je vous ai envoyé un message en MP !')
		await context.message.channel.send('Vous pouvez joindre mon serveur ici ! : https://discord.gg/Rm84JTm merci!')

@client.command(name='sondage', pass_context=True)
async def poll(context, *args):
	mesg = ' '.join(args)
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		embed = discord.Embed(title='Nous avons un sondage !', description='{0}'.format(mesg), color=0x00FF00)
		embed.set_footer(text='Sondage créé par : {0} • Réagissez pour voter!'.format(context.message.author))
		embed_message = await context.message.channel.send(embed=embed)
		await embed_message.add_reaction( '👍')
		await embed_message.add_reaction('👎')
		await embed_message.add_reaction('🤷')

@client.command(name='Oui?', pass_context=True)
async def eight_ball(context, *args):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		answers = ['C est Certain.', 'C est ainsi.', 'Vous pouvez compter sur elle.', 'Sans aucun doute.',
				   'Oui - certainement.', 'Comme je le vois, oui.', 'Très probablement', 'Ca semble bon.', 'OUI.',
				   'Les signes pointent vers le oui.', 'Redemandez plus tard', 'Mieux vaut ne pas vous dire maintenant.', 
				   'Ne peut pas prédire maintenant.', 'Concentrez-vous et demandez à nouveau plus tard', 'Ne comptez pas dessus.', 'Ma réponse est non',
				   'Mes sources disent non.', 'Ca sent pas bon', 'JE SAIS PAS MOI']
		embed = discord.Embed(title='**Ma réponse:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=0x00FF00)
		embed.set_footer(text='Question demandé par: {0} • Demandez la votre maintenant !'.format(context.message.author))
		await context.message.channel.send(embed=embed)

@client.command(name='bitcoin',pass_context=True)
async def bitcoin(context):
	url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
	async with aiohttp.ClientSession() as session:  
		raw_response = await session.get(url)
		response = await raw_response.text()
		response = json.loads(response)
		embed = discord.Embed(title=':Source d info : Info',
							  description='Le prix du bitcoin en US dollard actuellment: $' + response['bpi']['USD']['rate'], color=0x00FF00)
		await context.message.channel.send(embed=embed)


@client.command(name='eteindre', pass_context=True)
async def shutdown(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.id in OWNERS:
			embed = discord.Embed(title='Exctinction des feux !', description='Je m eteins ... A plus DANS L BUS ! :wave:', color=0x00FF00)
			await context.message.channel.send(embed=embed)
			await client.logout()
			await client.close()
		else:
			embed = discord.Embed(title='ERREUR!', description='Vous n avez pas la permission d utiliser cette commande',
								  color=0x00FF00)
			await context.message.channel.send(embed=embed)


@client.command(name='dire', pass_context=True)
async def echo(context, *, content):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.id in OWNERS:
			await context.message.delete()
			await context.message.channel.send(content)
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)

@client.command(name='ancrer', pass_context=True)
async def embed(context, *args):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.id in OWNERS:
			mesg = ' '.join(args)
			embed = discord.Embed(description=mesg, color=0x00FF00)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)


@client.command(name='kicker', pass_context=True)
async def kick(context, member: discord.Member, *args):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)

		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.kick_members:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='ERREUR', description='UTILISATEUR A DES PERMS ADMIN.', color=0x00FF00)
				await context.message.channel.send(embed=embed)
			else:
				mesg = ' '.join(args)
				embed = discord.Embed(title='Utilisateur a été kické', description='**{0}** a été kické par **{1}**!'.format(member,
																												context.message.author),
									  color=0x00FF00)
				embed.add_field(name='Raison:', value=mesg)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.send('Vous avez été averti par  **{0}**!  '.format(context.message.author) + 'RAISON: {0}'.format(mesg))
				await member.kick()
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)

@client.command(name='renomme', pass_context=True)
async def nick(context, member: discord.Member, *, name : str):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if name.lower() == "!reset":
				name = None
			embed = discord.Embed(title='SURNOM changé !', description='**{0}** votre nouveau surnom est **{1}**!'.format(member, name), color=0x00FF00)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await member.change_nickname(name)
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)

@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *args):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if member.guild_permissions.administrator:
				eembed = discord.Embed(title='ERREUR', description='UTILISATEUR A DES PERMS ADMIN.', color=0x00FF00)
				await context.message.channel.send(embed=embed)
			else:
				mesg = ' '.join(args)
				embed = discord.Embed(title='Utilisateur Banni!', description='**{0}** à été banni par **{1}**!'.format(member,
																												context.message.author),
									  color=0x00FF00)
				embed.add_field(name='RAISON:', value=mesg)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.send('Vous avez été banni par **{0}**!'.format(
					context.message.author) + 'RAISON : {0}'.format(mesg))
				await member.ban()
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)


@client.command(name='deban', pass_context=True)
async def unban(context, user: discord.Member):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			embed = discord.Embed(title='Utilisateur débanni!',
								  description='**{0}** à été débanni par **{1}**!'.format(user, context.message.author),
								  color=0x00FF00)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await user.send('Vous avez été débanni par **{0}**!  '.format(context.message.author) + 'RAISON: Ban révoqué')
			await user.unban()
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)


@client.command(name='avertir ', pass_context=True)
async def warn(context, member: discord.Member, *args):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			mesg = ' '.join(args)
			embed = discord.Embed(title='Utilisateur averti !',
								  description='**{0}** a été averti par **{1}**!'.format(member, context.message.author),
								  color=0x00FF00)
			embed.add_field(name='Raison:', value=mesg)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await member.send('Vous avez été averti par **{0}**!  '.format(
				context.message.author) + 'Raison: {0}'.format(mesg))
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)


@client.command(name='nettoyage', pass_context=True)
async def purge(context, number):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			number = int(number)
			await context.message.channel.purge(limit=number)
			embed = discord.Embed(title='Chat nettoyé!',
								  description='**{0}** a nettoyé **{1}** messages!'.format(context.message.author,
																						 number), color=0x00FF00)
			message = await context.message.channel.send(embed=embed)
			await asyncio.sleep(3)
			await message.delete()
		else:
			embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
			await context.message.channel.send(embed=embed)

@client.command(name='listenoire', pass_context=True)
async def blacklist(context, mode : str, user : discord.User = None):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.id in OWNERS:
			if (mode.lower() == "ajouter"):
				userID = user.id
				try:
					BLACKLIST.append(userID)
					embed = discord.Embed(title="Utilisateur Blacklisté", description='**{0}** a été ajouté a la liste noire '.format(user.name), color=0x00FF00)
					embed.set_footer(text='Il y a maintenant {0} utilisateurs dans la liste noire !'.format(len(BLACKLIST)))
					await context.message.channel.send(embed=embed)
				except:
					embed = discord.Embed(title=":x: ERREUR!", description="Un erreur inconnue se produit quand j'ajoute  **{0}** à la blackliste.".format(user.name), color=0xFF0000)
					await context.message.channel.send(embed=embed)
			elif (mode.lower() == "supp"):
				userID = user.id
				try:
					BLACKLIST.remove(userID)
					embed = discord.Embed(title="Utilisateur déblacklisté",
										  description='**{0}** a été supprimé de la blackliste '.format(
											  user.name), color=0x00FF00)
					embed.set_footer(text='Il y a maintenant {0} utilisateurs dans la liste noire !'.format(len(BLACKLIST)))
					await context.message.channel.send(embed=embed)
				except:
					embed = discord.Embed(title=":x: ERREUR!",
										  description="Un erreur inconnue se produit quand j'ajoute  **{0}** à la blackliste.\nÊtes vous sur que l'utilisateur est blacklisté ??".format(
											  user.name), color=0xFF0000)
					await context.message.channel.send(embed=embed)
			elif (mode.lower() == "liste"):
				embed = discord.Embed(title="Il y a actuellement {0} IDs blacklistés ".format(len(BLACKLIST)),
									  description="{0}".format(BLACKLIST),
									  color=0x00FF00)
				await context.message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title='ERREUR', description='VOUS N\'AVEZ PAS LA PERMISSION POUR CETTE COMMANDE .',
								  color=0xFF0000)
			await context.message.channel.send(embed=embed)

client.remove_command('AIDE')

@client.command(name='AIDE', description='AIDE POUR VOUS !', brief='A L\'AIDE !!!', pass_context=True)
async def help(context):
	if context.message.author.id in BLACKLIST:
		embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Bot', description='Liste des commandes :', color=0x00FF00)
		embed.add_field(name='Invite - Invite le bot', value='Usage: VOTRE_PREFIXE_ICI invite', inline=False)
		embed.add_field(name='Server - Rejoignez mon serveur', value='Usage: VOTRE_PREFIXE_ICI server', inline=False)
		embed.add_field(name='sondage - Crée un sondage pour les utilisateurs', value='Usage: VOTRE_PREFIXE_ICI sondage <idea>', inline=False)
		embed.add_field(name='Oui? - réponds a vos questions', value='Usage: VOTRE_PREFIXE_ICI Oui? <question>', inline=False)
		embed.add_field(name='Bitcoin - Montre la valeur du bitcoincoin en US dollard ', value='Usage: VOTRE_PREFIXE_ICI bitcoin', inline=False)
		embed.add_field(name='Info - Donne des infos sur le bot', value='Usage: VOTRE_PREFIXE_ICI info', inline=False)
		embed.add_field(name='eteindre - éteint le bot [PROPRIETAIRE]', value='Usage: VOTRE_PREFIXE_ICI eteindre', inline=False)
		embed.add_field(name='dire - J\'envoie un message de votre choix [PROPRIO]', value='Usage: VOTRE_PREFIXE_ICI dire <message>', inline=False)
		embed.add_field(name='ancrer - j\'envoie un message encré de votre choix [PROPRIO]', value='Usage: VOTRE_PREFIXE_ICI ancrer <message>', inline=False)
		embed.add_field(name='kicker - Kick un utilisateur', value='Usage: VOTRE_PREFIXE_ICI kicker <utilisateur> <raison>', inline=False)
		embed.add_field(name='ban - Ban un utilisateur ', value='Usage: VOTRE_PREFIXE_ICI ban <utilisateur> <raison>', inline=False)
		embed.add_field(name='avertir - averti un utilisateur en MP', value='Usage: VOTRE_PREFIXE_ICI avertir <utilisateur> <raison>', inline=False)
		embed.add_field(name='deban - Débanne un utilisateur', value='Usage: VOTRE_PREFIXE_ICI deban <utilisateur>', inline=False)
		embed.add_field(name='nettoyage - enleve un NB de messages ', value='Usage: VOTRE_PREFIXE_ICI nettoyage <nb>', inline=False)
		embed.add_field(name='AIDE - Montre ce menu', value='Usage: VOTRE_PREFIXE_ICI AIDE', inline=False)
		await context.message.channel.send(embed=embed)

@client.event
async def on_command_error(context, error):
	if isinstance(error, commands.CommandOnCooldown):
		await context.message.delete()
		embed = discord.Embed(title="ERREUR", description='Cette commande ne peut etre executé que dans  %.2fs ' % error.retry_after, color=0x00FF00)
		message = await context.message.channel.send(embed=embed)
		await asyncio.sleep(5)
		await message.delete()
	raise error

@blacklist.error
async def blacklist_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI listenoire', description='**Description::** Empeche un utilisateur d\'utiliser le bot \n **Usage:** YOUR_PREFIX_HERE blacklist [ajouter/supp/liste] [utilisateur] \n **Example:** YOUR_PREFIX_HERE listenoire ajouter @RandomUser', color=0x00FF00)
	await context.message.channel.send(embed=embed)

@ban.error
async def ban_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI ban', description='**Description:** ban un joueur \n **Usage:** VOTRE_PREFIXE_ICI ban [utilisateur] [raison] \n **Example:** VOTRE_PREFIXE_ICI ban @RandomUser SORS D\'ICI!', color=0x00FF00)
	await context.message.channel.send(embed=embed)

@poll.error
async def poll_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI sondage', description='**Description:** Crée un sondage pour voter ! \n **Usage:** VOTRE_PREFIXE_ICI sondage [idée] \n **Example:** VOTRE_PREFIXE_ICI sondage BAN TOUT LE MONDE!', color=0x00FF00)
	await context.message.channel.send(embed=embed)

@eight_ball.error
async def eight_ball_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI Oui?', description='**Description:** AYEZ DES REPONSES A VOS QUESTIONS \n **Usage:** VOTRE_PREFIXE_ICI Oui? [question] \n **Example:** VOTRE_PREFIXE_ICI Oui? Êtes vous banni d\'un jeu?', color=0x00FF00)
	await context.message.channel.send(embed=embed)

@echo.error
async def say_error(context, error):
	embed = discord.Embed(title='**Commande:** YOUR_PREFIX_HERE say', description='**Description:** je dis ce que vous dites \n **Usage:** VOTRE_PREFIXE_ICI dire [message] \n **Example:** VOTRE_PREFIXE_ICI dire JVAIS TE BAN!!', color=0x00FF00)
	await context.message.channel.send(embed=embed)


@embed.error
async def embed_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI ancrer',
						  description='**Description:** je dis ce que vous dites avec un msg ancré \n **Usage:** VOTRE_PREFIXE_ICI ancrer [message] \n **Example:** VOTRE_PREFIXE_ICI ancrer CEUX QUI LISENT CA SONT BANNI!!', color=0x00FF00)
	await context.message.channel.send(embed=embed)


@kick.error
async def kick_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI kicker',
						  description='**Description:** Kick un utilisateur \n **Usage:** VOTRE_PREFIXE_ICI kick [utilisateur] [raison] \n **Example:** VOTRE_PREFIXE_ICI @RandomUser REJOINS quand tu sera plus malin que moi !', color=0x00FF00)
	await context.message.channel.send(embed=embed)


@unban.error
async def unban_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI deban',
						  description='**Description:** debans un utilisateur \n **Usage:** VOTRE_PREFIXE_ICI deban [utilisateur] \n **Example:** VOTRE_PREFIXE_ICI deban @RandomUser', color=0x00FF00)
	await context.message.channel.send(embed=embed)

@warn.error
async def warn_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI avertir',
						  description='**Description:** averti un utilisateur \n **Usage:** VOTRE_PREFIXE_ICI avertir [utilisateur] [raison] \n **Example:** VOTRE_PREFIXE_ICI avertir @RandomUser STOP SPAM OU BAN!', color=0x00FF00)
	await context.message.channel.send(embed=embed)


@purge.error
async def purge_error(context, error):
	embed = discord.Embed(title='**Commande:** VOTRE_PREFIXE_ICI nettoyage',
						  description='**Description:** nettoie des msg \n **Usage:** VOTRE_PREFIXE_ICI nettoyage [nb de messages] \n **Example:** VOTRE_PREFIXE_ICI nettoyage 20', color=0x00FF00)
	await context.message.channel.send(embed=embed)

client.run(TOKEN)
