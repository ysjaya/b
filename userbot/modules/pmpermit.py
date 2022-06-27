from userbot.helpers.SQL.pmstuff import givepermit, checkpermit, blockuser, getwarns, allallowed, allblocked, inwarns, addwarns
from pyrogram import Client, filters
from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError
from config import *
from config import CMD_HANDLER as cmd
from config import PM_AUTO_BAN
from userbot import TEMP_SETTINGS

from .help import *


DEF_UNAPPROVED_MSG = f" 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 🔱 \n\n"
DEF_UNAPPROVED_MSG += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
DEF_UNAPPROVED_MSG += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
DEF_UNAPPROVED_MSG += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
DEF_UNAPPROVED_MSG += f"► Rᴇᴘᴏ : [Deploy On Bot](https:) \n"
DEF_UNAPPROVED_MSG += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/ygabutkan) \n"
DEF_UNAPPROVED_MSG += f"► Mutualan : [Jᴏɪɴ.](https://t.me/euphoricfams) \n"
DEF_UNAPPROVED_MSG += f"⍟ 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙲𝙷𝙰𝚃 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙺𝙴𝙽𝚃𝙾𝙳⍟\n⍟ 𝙶𝚄𝙰 𝙰𝙺𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𝙱𝙻𝙾𝙺𝙸𝚁 𝙺𝙰𝙻𝙾 𝙻𝚄 𝚂𝙿𝙰𝙼⍟\n⍟ 𝙹𝙰𝙳𝙸 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙰𝙸 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙽𝙴𝚁𝙸𝙼𝙰 𝙿𝙴𝚂𝙰𝙽 𝙻𝚄⍟\n"
DEF_UNAPPROVED_MSG += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"

#(
    
 #   "╔════════════════════╗\n"
#    "     ⛑ 𝗔𝗧𝗧𝗘𝗡𝗧𝗜𝗢𝗡 𝗣𝗟𝗘𝗔𝗦𝗘 ⛑\n"
 #   "╚════════════════════╝\n"
 #   "**ROOM CHAT || BAYUSERBOT**\n"
 #   "━━━━━━━━━━━━━━━━━━━━\n"
  #  "⍟ 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙲𝙷𝙰𝚃 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙺𝙴𝙽𝚃𝙾𝙳⍟\n⍟ 𝙶𝚄𝙰 𝙰𝙺𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𝙱𝙻𝙾𝙺𝙸𝚁 𝙺𝙰𝙻𝙾 𝙻𝚄 𝚂𝙿𝙰𝙼⍟\n⍟ 𝙹𝙰𝙳𝙸 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙰𝙸 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙽𝙴𝚁𝙸𝙼𝙰 𝙿𝙴𝚂𝙰𝙽 𝙻𝚄⍟\n"
 #   "┏━━━━━━━━━━━━━━━━━━━\n"
 #   "┣[• PESAN OTOMATIS\n"
 #   "┣[• BY BAYUSERBOT\n"
 #   "┗━━━━━━━━━━━━━━━━━━━"
#)
    



@Client.on_message(
    ~filters.me & filters.private & ~filters.bot & filters.incoming, group=69
)
async def alive(client: Client, e: Message):
  message = e
  if checkpermit(message.chat.id):
        print("sql is cringe here")
        return
  else:
    print("gotit")
    addwarns(message.chat.id)
    gw= getwarns(message.chat.id)
    teriu= message.from_user
    teriun= teriu.id
    teriuni= str(teriun)
    teriunia="aprv_"+teriuni
    teriunid="decine_"+teriuni
    ids = 0
  if isinstance(gw , str):
      sb= await client.get_me()
      un= LOG_GROUP
  else:
      keyboard= InlineKeyboardMarkup([  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Approve",
                        callback_data=teriunia
                    ),
                    InlineKeyboardButton(
                        "Decline",
                        callback_data=teriunid
                    ),
                ])
      await message.reply_photo(photo=ALIVE_LOGO, caption=DEF_UNAPPROVED_MSG)
      if gw==3:
        await message.reply_text("You have crossed your warns so die")
        await client.block_user(message.from_user.id)
        blockuser(message.from_user.id)
        return


@Client.on_message(filters.command(["ok", "a", "approve"], ["."]) & filters.me & filters.private)
async def refet(client: Client, message: Message):
    givepermit(message.chat.id)
    await message.edit_text("the user has been approved!!")
    
     
@Client.on_message(filters.command(["tolak", "t", "dapprove", "disapprove", "dp"], ["."]) & filters.me & filters.private)
async def refes(client: Client, message: Message):
    await message.edit_text("the user has been blocked!!")
    blockuser(message.chat.id)
    await client.block_user(message.chat.id)
    
@Client.on_message(filters.command(["allpermitted", "approvedlist"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allallowed()
  strr ="Following are the users allowed"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["allblocked"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allblocked()
  strr ="Following are the users blocked"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["nonpermitted"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = inwarns()
  strr ="Following are the users not allowed"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

add_command_help(
    "pmpermit",
    [
        [
            f"{cmd}ok atau {cmd}a",
            "Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            f"{cmd}tolak atau {cmd}t",
            "Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
    ],
)
