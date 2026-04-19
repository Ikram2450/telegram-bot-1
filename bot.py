import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("ERROR: BOT_TOKEN not found")
    exit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """🎉 Welcome to Robot!

Please send your phone number starting with the country code.
(Example: +880xxxxxxxxxxx)

/cap send to check capacity"""

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")

app.run_polling()
