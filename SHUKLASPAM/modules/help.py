# © @ITSZSHUKLA
from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ 𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @AmShashank**"

HELP_BUTTON = [
    [
      Button.inline("𝗦𝗣𝗔𝗠", data="spam"),
      Button.inline("𝗥𝗔𝗜𝗗", data="raid")
    ],
    [
      Button.inline("𝗘𝗫𝗧𝗥𝗔", data="extra")
    ],
    [
      Button.url("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", "https://t.me/ITSZ_SHIVANSH"),
      Button.inline("𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗", data="shukla")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/05522e13c97752efe5e75.png",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ  ᴄᴏᴍᴍᴀɴᴅs:**

🌺 𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **💘ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs💘**
  1) {hl}𝙿𝚒𝚗𝚐
  2) {hl}reb𝚘𝚘𝚝
  3) {hl}𝚂𝚞𝚍𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>  --> Owner Cmd
  4) {hl}𝚕𝚘𝚐𝚜 --> Owner Cmd

💫 𝗘𝗰𝗵𝗼: **🌸ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜsᴇʀ🌸**
  1) {hl}𝚎𝚌𝚑𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚛𝚖𝚎𝚌𝚑𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

❤️‍🔥 𝗟𝗲𝗮𝘃𝗲: **🍁ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ🍁**
  1) {hl}𝚕𝚎𝚊𝚟𝚎 <𝚐𝚛𝚘𝚞𝚙/𝚌𝚑𝚊𝚝 𝚒𝚍>
  2) {hl}𝚕𝚎𝚊𝚟𝚎 : 𝚃𝚢𝚙𝚎 𝚒𝚗 𝚝𝚑𝚛 𝙶𝚛𝚘𝚞𝚘 𝚋𝚘𝚝 𝚠𝚒𝚕𝚕 𝚊𝚞𝚝𝚘 𝚕𝚎𝚊𝚟𝚎 𝚝𝚑𝚊𝚝 𝚐𝚛𝚘𝚞𝚙 


**© @SHASHANKDEV**
"""


raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs:**

💘 𝗥𝗮𝗶𝗱: **🌟ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ🌟**
  1) {hl}𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **✨ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ✨**
  1) {hl}𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  3) {hl}𝚑𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  4) {hl}𝚑𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌺 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **🍁ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚍𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚍𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  3) {hl}𝚍𝚑𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  4) {hl}𝚍𝚑𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌟 𝐋𝐨𝐯𝐞 𝐑𝐚𝐢𝐝: **❤️‍🔥ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ❤️‍🔥**
  1) {hl}𝚖𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚕𝚘𝚟𝚎𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

💖 𝐇𝐢𝐧𝐝𝐢 𝐑𝐚𝐢𝐝: **💫ʜɪɴᴅɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ💫**
  1) {hl}𝚑𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <username>
  2) {hl}𝚑𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝐂𝐑𝐚𝐢𝐝: **🍁ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚌𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚌𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💓 𝐐𝐑𝐚𝐢𝐝: **🍁18+ ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚚𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚚𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>


**© @SHASHANKDEV**💘
"""

shukla_msg = f"""
**» ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:**

💘 𝗚𝗼𝗼𝗱 𝗔𝗳𝘁𝗲𝗿𝗻𝗼𝗼𝗻: **🌟ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ🌟**
  1) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗘𝗺𝗼𝗷𝗶: **✨ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ✨**
  1) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌺 𝗚𝗼𝗼𝗱 𝗠𝗼𝗿𝗻𝗶𝗻𝗴: **🍁ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚐𝚖 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚐𝚖 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌟 𝗚𝗼𝗼𝗱 𝗡𝗶𝗴𝗵𝘁: **❤️‍🔥ɢᴏᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ❤️‍🔥**
  1) {hl}𝚐𝚗 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚐𝚗 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗦𝗵𝗮𝘆𝗿𝗶 𝗥𝗮𝗶𝗱: **💫sʜʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ💫**
  1) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <username>
  2) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝗙𝗹𝗶𝗿𝘁𝗶𝗻𝗴: **🍁ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚏𝚕𝚒𝚛𝚝 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚏𝚕𝚒𝚛𝚝 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝗕𝗶𝗿𝘁𝗵𝗱𝗮𝘆: **🍁ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚋𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚋𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>


**© @SHASHANKDEV**💘
"""

spam_msg = f"""
**» sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs:**

🌺 𝗦𝗽𝗮𝗺: **❤️‍🔥sᴘᴀᴍs ᴀ ᴍᴇssᴀɢᴇ❤️‍🔥**
  1) {hl}𝚂𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚜𝚙𝚊𝚖> (𝚢𝚘𝚞 𝚌𝚊𝚗 𝚛𝚎𝚙𝚕𝚢 𝚊𝚗𝚢 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚒𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚋𝚘𝚝 𝚝𝚘 𝚛𝚎𝚙𝚕𝚢 𝚝𝚑𝚊𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚊𝚗𝚍 𝚍𝚘 𝚜𝚙𝚊𝚖𝚖𝚒𝚗𝚐)
  2) {hl}𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚊𝚗𝚢 𝚖𝚎𝚜𝚜𝚊𝚐𝚎>

💖 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **🍁ᴘᴏʀɴᴏɢʀᴀᴘʜʏ  sᴘᴀᴍ🍁**
  1) {hl}𝙿𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝>

🌸 𝗛𝗮𝗻𝗴: **🌺sᴘᴀᴍs ʜᴀɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀs🌺**
  1) {hl}𝚑𝚊𝚗𝚐 <𝚌𝚘𝚞𝚗𝚝𝚎𝚛>

💖 𝗔𝗯𝘂𝘀𝗲𝗦𝗽𝗮𝗺: **🌺ᴏɴᴇ ᴡᴏʀᴅ ʙɪɢ ɢᴀᴀʟɪ sᴘᴀᴍ🌺**
  1) {hl}𝚊𝚋𝚞𝚜𝚎 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  
** © @SHASHANKDEV**
"""                     


@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("𝗦𝗣𝗔𝗠", data="spam"),
                Button.inline("𝗥𝗔𝗜𝗗", data="raid")
              ],
              [
                Button.inline("𝗘𝗫𝗧𝗥𝗔", data="extra")
              ],
              [
                Button.url("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", "https://t.me/ITSZ_SHIVANSH"),
                Button.inline("𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗", data="shukla")
              ]
            ]
          )
    else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)
        
        
@X1.on(events.CallbackQuery(pattern=r"shukla"))
@X2.on(events.CallbackQuery(pattern=r"shukla"))
@X3.on(events.CallbackQuery(pattern=r"shukla"))
@X4.on(events.CallbackQuery(pattern=r"shukla"))
@X5.on(events.CallbackQuery(pattern=r"shukla"))
@X6.on(events.CallbackQuery(pattern=r"shukla"))
@X7.on(events.CallbackQuery(pattern=r"shukla"))
@X8.on(events.CallbackQuery(pattern=r"shukla"))
@X9.on(events.CallbackQuery(pattern=r"shukla"))
@X10.on(events.CallbackQuery(pattern=r"shukla"))
async def help_shukla(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(shukla_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("𝗣ᴀʜʟᴇ 𝗝ᴀᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ ⚡️𝐒𝐇𝐈𝐕𝐀𝐍𝐒𝐇⚡️ 𝗞ᴏ 𝗪ᴏ 𝗧ᴜᴍʜᴇ 𝗦ᴜᴅᴏ 𝗗ᴇ 𝗗ᴇɢᴀ", cache_time=0, alert=True)