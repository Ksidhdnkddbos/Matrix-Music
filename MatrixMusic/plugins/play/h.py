import asyncio


import random
from MatrixMusic import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID
from pyrogram import filters

txt = [

            f"؏ـيوٍڼ ماتركس 😻🫶",


             "ﻧ؏ـ۾ 🥺❤",
            

            "هہذآ آڛـﻤــي 🫶😻",
            
            
            f"ضـوꪆ ماتريكس،💗🧸!َ''))",
            
            
            "نعٓم يـﺣـبـعـﻣـري،🥺🧡🌸!َ''))",
            
            
             "ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]
txt1 = [

            f"**؏ـيوٍڼ ماتركس 😻🫶 يا مطوريي**",


             f"**ﻧ؏ـم يامطوريي**",
            

            f"**امرني يا مطوري الحبيب**",
            
            
           
            
            
 
            
            

        ]



        


@app.on_message(command(["بوت"]))


async def cutt(client: Client, message: Message):
     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(


         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       
     
        
