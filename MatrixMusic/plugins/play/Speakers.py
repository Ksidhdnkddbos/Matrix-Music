from pyrogram import filters, Client
from MatrixMusic import app
import asyncio
from typing import Optional
from random import randint
from pyrogram.types import Message, ChatPrivileges
from strings.filters import command
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from MatrixMusic.utils.database import *
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from MatrixMusic.core.call import Zelzaly 
from MatrixMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

@app.on_message(filters.regex("المتكلمين"))
async def strcall(client, message):
    assistant = await group_assistant(Zelzaly,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./strings/call.mp3"), stream_type=StreamType().pulse_stream)
        text="↯︙الاعضاء المتواجدين في المكالمة المرئية :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="⦗ يتكلم ⦘"
            else:
                mut="⦗ لا يتكلم ⦘"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}:{user.mention}↬{mut}\n"
        text += f"\n↯︙عدد الاشخاص في المكالمة المرئية ↬ ⦗ {len(participants)} ⦘"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"لم يتم العثور على دردشة فيديو نشطة.\nيرجى بدء دردشة فيديو في مجموعتك/قناتك والمحاولة مرة أخرى.")
    except TelegramServerError:
        await message.reply(f"ارسل مرة اخرى يوجد خطأ في احد سيرفرات التليكرام")

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"**لم يتم العثور على مكالمة جماعية** {err_msg}")
    return False

@app.on_message(filters.regex("^تشغيل المكالمة$"))
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "جاري تشغيل المكالمه المرئية")
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("تم تشغيل المكالمة\n#MatrixTeAm")
    except ChatAdminRequired:
      try:    
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
            ),
        )
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
        )                              
        await msg.edit_text("تم تشغيل المكالمة\n#MatrixTeAm")
      except:
         await msg.edit_text("خلي البوت معاه صلاحية اضافة مشرفين والتحكم ف المحادثه الصوتيه او ارفع المساعد مشرف وجرب")
@app.on_message(filters.regex("^ايقاف المكالمة$"))
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "تم ايقاف المكالمة\n#MatrixTeAm")
    try:
        if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", group call already ended")
           )
        ):  
           return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("تم ايقاف المكالمة\n#MatrixTeAm")
    except Exception as e:
      if "GROUPCALL_FORBIDDEN" in str(e):
       try:    
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
             ),
         )
         if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", group call already ended")
           )
         ):  
           return
         await assistant.invoke(DiscardGroupCall(call=group_call))
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
         )                              
         await msg.edit_text("تم ايقاف المكالمة\n#MatrixTeAm")
       except:
         await msg.edit_text("خلي البوت معاه صلاحية اضافة مشرفين والتحكم ف المحادثه الصوتيه او ارفع المساعد مشرف وجرب")
