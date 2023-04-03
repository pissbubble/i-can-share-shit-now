import discord

from discord.ext import commands
from utils import Utils as u



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "help", hidden = True)
    async def help(self, ctx, cmd = None):
        # The cmd parameter is optional and defaults to None if not specified

        if cmd == None:
            # If no command is specified, generate a list of all available commands grouped by cog

            cdict = []

            for cog in self.bot.cogs:
                #loop over all the loaded cogs in the bot

                val = ",".join(f"`{command}`" for command in self.bot.get_cog(cog).get_commands() if not command.hidden)
                # Get a comma-separated list of non-hidden command names for the current cog

                if val == "":
                    # If there are no non-hidden commands for this cog, skip it
                    continue
                else:
                    # Otherwise, add the cog/command pair to the list
                    cdict.append({"name": f"{cog}:", "value": val, "inline": False})

            emb = u.construct_emb(title = "__*Help*__", desc = "Here's a list of all the commands I can do.", fields = cdict, footer = f"type \"{ctx.prefix}help <command name>\" for more info on a command!", color = ctx.author.color)
             # Create an embed with the list of available commands, a title, a description, and a footer with instructions for getting more information about a specific command
            await ctx.channel.send(embed = emb)
        
        else:
            # If a command is specified, attempt to get information about it

            try:
                command = self.bot.get_command(cmd)
                # Get the command object from the bot using the specified command name

                if not command.hidden:
                    # If the command is not hidden, generate an embed with its name, help message, and usage information (if available)

                    if command.help != None and command.usage != None:
                        emb = u.construct_emb(title = f"__*{command.name.capitalize()}*__", desc = command.help, fields = [{"name": "Usage:", "value": f"```\n{ctx.prefix}{command.usage}\n```", "inline": False}], color = ctx.author.color)
                        await ctx.channel.send(embed = emb)

                    else:
                        await ctx.channel.send(f"Oops, `{ctx.prefix}{command.name}` doesn't have a help message yet, please be patient as it's being worked on.")
                        # If the command does not have a help message or usage information, reply with an error message

                else:
                    await ctx.channel.send(f"Please only ask for help on commands that are listed in the `{ctx.prefix}help` menu. The rest of the commands don't have a help message.")
                    # If the command is hidden, reply with an error message politely explaining to the user that they are being idiotic,
                    # and that they should never, under any circumstances, stray from the given options. 

            except AttributeError:
                await ctx.channel.send(f"Sorry, I don't have a `{cmd}` command. Please input a valid command, or, if you like this message a lot, keep trying, I don't give a shit, frankly.")
                # If the specified command does not exist, reply with a message indicating that this is the case,
                # and that they can repeat themselves indefinitely if they feel so inclined


async def setup(bot):
    await bot.add_cog(Help(bot))
