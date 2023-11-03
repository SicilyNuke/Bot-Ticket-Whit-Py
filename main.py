import discord
from discord.ext import commands
from discord import app_commands
from discord import ButtonStyle , ui
from discord.ui import Button





bot = commands.Bot(command_prefix="Your Prefix", intents=discord.Intents().all())


@bot.event
async def on_ready():
    print(f"Bot is on whit name: {bot.user.name}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Your Status"))
    await bot.tree.sync()












staff = "<@&Your Ticket Role Supporter>"

@bot.command()
async def ticket(ctx):




    ticket_button = Button(style=ButtonStyle.green, label="You Selection",emoji="✅")
    ticket_view = discord.ui.View(timeout=None)
    ticket_view.add_item(ticket_button)
    s_button = Button(style=ButtonStyle.blurple, label="You Selection", emoji="🎈")
    s_view = discord.ui.View(timeout=None)
    s_view.add_item(s_button)
    ticket_embed = discord.Embed(title="Tickets", description="Click a category to open a Ticket",)
    ticket_message = await ctx.send(embed=ticket_embed, view=ticket_view)
    ticket_message = await ctx.send(view=s_view)














    close_button = ui.Button(label="Close ticket", emoji="🔒", style=ButtonStyle.red)

    async def close_callback(interaction: discord.Interaction):

       await interaction.channel.delete()



    close_button.callback = close_callback 
    close_view = ui.View(timeout=None)
    close_view.add_item(close_button)



    claim_button = ui.Button(label="Claim", style=ButtonStyle.green)

    async def claim_callback(interaction: discord.Interaction):
      embed = discord.Embed(description=f"Ticket Claimed by {interaction.user.mention}")
      await interaction.response.send_message(embed=embed)

    claim_button.callback = claim_callback
    claim_view = ui.View(timeout=None)
    claim_view.add_item(claim_button)







    async def asdasd(i: discord.Interaction):
        category = discord.utils.get(ctx.guild.categories, name="Ticket")
        if not category:
            category = await ctx.guild.create_category(name="Ticket")

        ticket_channel = await category.create_text_channel(name=f"The channel name when the ticket opens{i.user.name}")
        await ticket_channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await ticket_channel.set_permissions(i.user, read_messages=True)


        await i.response.send_message(f"Ticket creato: {ticket_channel.mention}",ephemeral=True)

        await ticket_channel.send(f"{i.user.mention}, Thank you for opening the ticket, describe your problem and wait for us {staff} to reply!" , view=close_view)
        await ticket_channel.send(view=claim_view)

    ticket_button.callback = asdasd


    async def pp(i: discord.Interaction):
        category = discord.utils.get(ctx.guild.categories, name="Ticket")
        if not category:
            category = await ctx.guild.create_category(name="Ticket")

        ticket_channel = await category.create_text_channel(name=f"The channel name when the ticket opens{i.user.name}")
        await ticket_channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await ticket_channel.set_permissions(i.user, read_messages=True)


        await i.response.send_message(f"Ticket creato: {ticket_channel.mention}",ephemeral=True)

        await ticket_channel.send(f"{i.user.mention},  Thank you for opening the ticket, describe your problem and wait for us {staff} to reply!" , view=close_view)
        await ticket_channel.send(view=claim_view)




    s_button.callback = pp



















bot.run("Your Bot Token")
