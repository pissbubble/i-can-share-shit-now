import discord
from discord.ext import menus
from datetime import datetime

class Utils:
    
    def __init__(self):
        self.main_channel = 685963444062519524

    #constructs an embed using kwargs to get named parameters for its components and sets custom defaults for missing arguments.
    def construct_emb(**inputEmb):

        today = datetime.today()
        year = today.year

        emb = discord.Embed(title= inputEmb.get("title", "default title")  , url= inputEmb.get("url"), description= inputEmb.get("desc"), colour= inputEmb.get("color", discord.Color.from_rgb(140, 32, 48)))
        emb.set_footer(text= inputEmb.get("footer", f"Copyright © {year} P!ngStudios, inc. All Rights Reserved"))

        for field in inputEmb.get("fields", [{"name":"field1", "value":"placeholder value", "inline":False}]):
            emb.add_field(name = field["name"], value = field["value"], inline = field["inline"])
        
        return emb