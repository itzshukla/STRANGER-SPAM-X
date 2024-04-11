from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f"⚡️ ​𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗦𝗣𝗔𝗠 𝙃𝗘𝗟𝗣 𝙈𝗘𝗡𝗨 ⚡️\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @SHIVANSHDEVS**"


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                               "https://telegra.ph/file/05522e13c97752efe5e75.png",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("⚡️ ꜱᴘᴀᴍ ⚡️", data="spam"),
            Button.inline("⚡️ ʀᴀɪᴅ ⚡️", data="raid"),
           ],
           [
            Button.inline("⚡️ ᴇxᴛʀᴀ ⚡️", data="extra"),
           ],
           [    
            Button.url("⚡️ ᴄʜᴀɴɴᴇʟ ⚡️", "https://t.me/SHIVANSH474"),
            Button.url("⚡️ sᴜᴘᴘᴏʀᴛ ⚡️", "https://t.me/MASTIWITHFRIENDSXD")
           ],
           ],
           )


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

𝗘𝗰𝗵𝗼: ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

𝗟𝗲𝗮𝘃𝗲: ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**© @SHIVANSHDEVS**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝐌𝐑𝐚𝐢𝐝: ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝐒𝐑𝐚𝐢𝐝: ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝐂𝐑𝐚𝐢𝐝: ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**© @SHIVANSHDEVS**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.
  1) {hl}pspam <count>

𝗛𝗮𝗻𝗴: ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.
  1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)


** © @SHIVANSHDEVS**
"""                     
           
           
@MK1.on(events.CallbackQuery(pattern=r"help_back"))
@MK2.on(events.CallbackQuery(pattern=r"help_back"))
@MK3.on(events.CallbackQuery(pattern=r"help_back"))
@MK4.on(events.CallbackQuery(pattern=r"help_back"))
@MK5.on(events.CallbackQuery(pattern=r"help_back"))
@MK6.on(events.CallbackQuery(pattern=r"help_back"))
@MK7.on(events.CallbackQuery(pattern=r"help_back"))
@MK8.on(events.CallbackQuery(pattern=r"help_back"))
@MK9.on(events.CallbackQuery(pattern=r"help_back"))
@MK10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("⚡️ ꜱᴘᴀᴍ ⚡️", data="spam"),
            Button.inline("⚡️ ʀᴀɪᴅ ⚡️", data="raid"),
           ],
           [
            Button.inline("⚡️ ᴇxᴛʀᴀ ⚡️", data="extra"),
           ],
           [
            Button.url("⚡️ ᴄʜᴀɴɴᴇʟ ⚡️", "https://t.me/SHIVANSH474"),
            Button.url("⚡️ sᴜᴘᴘᴏʀᴛ ⚡️", "https://t.me/MASTIWITHFRIENDSXD")
           ],
           ],
        )           
   else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"spam"))
@MK2.on(events.CallbackQuery(pattern=r"spam"))
@MK3.on(events.CallbackQuery(pattern=r"spam"))
@MK4.on(events.CallbackQuery(pattern=r"spam"))
@MK5.on(events.CallbackQuery(pattern=r"spam"))
@MK6.on(events.CallbackQuery(pattern=r"spam"))
@MK7.on(events.CallbackQuery(pattern=r"spam"))
@MK8.on(events.CallbackQuery(pattern=r"spam"))
@MK9.on(events.CallbackQuery(pattern=r"spam"))
@MK10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(spam_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            ) 
   else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"raid"))
@MK2.on(events.CallbackQuery(pattern=r"raid"))
@MK3.on(events.CallbackQuery(pattern=r"raid"))
@MK4.on(events.CallbackQuery(pattern=r"raid"))
@MK5.on(events.CallbackQuery(pattern=r"raid"))
@MK6.on(events.CallbackQuery(pattern=r"raid"))
@MK7.on(events.CallbackQuery(pattern=r"raid"))
@MK8.on(events.CallbackQuery(pattern=r"raid"))
@MK9.on(events.CallbackQuery(pattern=r"raid"))
@MK10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )  
     else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
   else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)
