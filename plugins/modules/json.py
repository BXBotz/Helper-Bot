from pyrogram import Client as FayasNoushad
from pyrogram import filters

@FayasNoushad.on_message((filters.group | filters.private) & filters.command(["json"]))
async def group(bot, update):
    json = update.reply_to_message
    with BytesIO(str.encode(str(json))) as json_file:
        json_file.name = "json.text"
        await json.reply_document(
            document=json_file,
            reply_markup=JSON_BUTTON
        )