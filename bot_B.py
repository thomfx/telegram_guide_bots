
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7540647627:AAGQvaKllMnuhnkkim5hLu75ZL5wa04hzZ4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Guida 1 (In arrivo)", callback_data="guida1")],
        [InlineKeyboardButton("📗 Guida 2", url="https://www.canva.com/design/DAGrGTzNfp8/VajYNfAnFRrjl7t7m6S3Iw/edit?utm_content=DAGrGTzNfp8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")],
        [InlineKeyboardButton("📙 Guida 3", url="https://www.canva.com/design/DAGrYJLsMjY/_O_N87yenPRMlpqewCePAQ/edit?utm_content=DAGrYJLsMjY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")],
        [InlineKeyboardButton("📒 Guida 4", url="https://www.canva.com/design/DAGrQCwCXno/WdeWBtnMWCewWMk_pp7XZw/edit?utm_content=DAGrQCwCXno&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")],
        [InlineKeyboardButton("💬 Scrivimi", url="https://t.me/ismaafx")],
        [InlineKeyboardButton("🔙 Torna al Bot Principale", url="https://t.me/ismaafx_vip_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📚 *Centro Guide VIP*

Scegli una guida da aprire o contattami direttamente 👇", parse_mode='Markdown', reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "guida1":
        await query.edit_message_text("🚧 La *Guida 1* è in arrivo, resta aggiornato!", parse_mode='Markdown')

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_callback))
app.run_polling()
