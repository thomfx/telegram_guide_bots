
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7390879542:AAEdoyf9rgcgfdiWeSuPfK24Xd4HPZeG01g"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("logo.jpg", "rb") as photo:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption=caption="🔥 *Benvenuto nel bot VIP di Thom!*\n\nAccedi subito a:\n📚 Le guide complete\n💬 Contatto diretto con me",

Accedi subito a:
📚 Le guide complete
💬 Contatto diretto con me",
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💬 Scrivimi", url="https://t.me/ismaafx")],
                [InlineKeyboardButton("📚 Vai alle Guide", url="https://t.me/ismaafx_guide_bot")]
            ])
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
