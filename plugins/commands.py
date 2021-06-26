from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.command(["start"]) & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
	reply_markup=START_BUTTONS
    )

@Client.on_message(filters.private & filters.command(["help"]) & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
      	disable_web_page_preview=True,
	reply_markup=HELP_BUTTONS
    )

@Client.on_message(filters.private & filters.command(["about"]) & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
	reply_markup=ABOUT_BUTTONS
    )
