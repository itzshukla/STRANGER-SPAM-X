# © @ITSZSHUKLA
from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("𝗛𝗘𝗟𝗣 𝗔𝗡𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", data="help_back")
    ],
    [
        Button.url("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", "https://t.me/ITSZSHUKLA"),
        Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/mastiwithfriendsxd")
    ],
    [
        Button.url("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", "https://t.me/ITSZ_SHIVANSH"),
        Button.url("𝗥𝗘𝗣𝗢", "https://github.com/itzshukla/STRANGER-SPAM-X/fork")
    ],
    [
        Button.url("𝗝𝗢𝗜𝗡 𝗙𝗢𝗥 𝗦𝗨𝗗𝗢", "https://t.me/STRANGERXWORLD")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        ShuklaBot = await event.client.get_me()
        bot_name = ShuklaBot.first_name
        bot_id = ShuklaBot.id
        TEXT = f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗜 𝗔𝗠 ‣ [{bot_name}](tg://user?id={bot_id})\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ \n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⦿ 24x7 ʀᴜɴ|[sᴛʀᴀɴɢᴇʀ](https://t.me/StrangerAssociation)\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/05522e13c97752efe5e75.png",
            caption=TEXT,
            buttons=START_BUTTON
        )