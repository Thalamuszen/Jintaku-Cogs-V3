import discord
from redbot.core import Config, checks, commands
from redbot.core.utils.menus import menu, commands, DEFAULT_CONTROLS
import asyncio
import logging

from .boorucore import BooruCore

class Boorualias:

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True, add_reactions=True)
    async def neko(self, ctx, *, tag=""):
        """Neko images"""

        tag_default = " neko"
        tag += tag_default
        boards = ["dan", "gel", "kon", "yan", "safe", "nekos_nsfw_neko", "nekos_sfw_neko"]

        await self.generic_alias_booru(ctx, boards, tag)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True, add_reactions=True)
    async def yaoi(self, ctx, *, tag=""):
        """Yaoi images"""

        tag_default = " yaoi"
        tag += tag_default
        boards = ["dan", "gel", "kon", "yan", "safe", "gay"]

        await self.generic_alias_booru(ctx, boards, tag)
        
    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True, add_reactions=True)
    async def yuri(self, ctx, *, tag=""):
        """Yuri images"""

        tag_default = " yuri"
        tag += tag_default
        boards = ["dan", "gel", "kon", "yan", "safe", "gay"]
        
        await self.generic_alias_booru(ctx, boards, tag)
