from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8117500006:AAEJTiGlh9So6xT-ESF5q54HBWKvHNlZE_E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("logo.jpg", "rb") as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Benvenuto nel bot VIP di Thom!\n\nAccedi subito a:\n- Le guide complete\n- Contatto diretto con me.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Scrivimi", url="https://t.me/Thom_fx12")],
                [InlineKeyboardButton("Vai alle Guide", url="https://t.me/Thom_guide_bot")]
            ])
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
