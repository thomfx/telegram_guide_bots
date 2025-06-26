from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8117500006:AAEJTiGlh9So6xT-ESF5q54HBWKvHNlZE_E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("logo.jpg", "rb") as photo:
        await context.bot.send_photo(
    chat_id=update.effective_chat.id,
    photo=photo,
    caption=caption,
    parse_mode="HTLM"
            caption = """📈 <b>Benvenuto nel mio bot VIP!</b>

Sono molto contento che da questo momento potrai approcciarti con noi nel mondo del trading, spero che tu possa trovarti bene in questo percorso.

Da questo momento in avanti ti accompagneremo segnale dopo segnale in tutte le operazioni che faremo insieme.
Tutto quello che devi fare è seguire le istruzioni, copiare i segnali e imparare strada facendo.

⚠️ <b>DISCLAIMER:</b>

Ci teniamo a fare delle raccomandazioni per viverci al meglio questa esperienza assieme.
Prima di prendere qualsiasi decisione di investimento (come in tutte le sue forme) hai bisogno di conoscere i rischi che possono conseguirne.
L'amministratore e i membri di questo Bot non sono in nessun modo responsabili di eventuali perdite che possono arrivare dall'uso di informazioni contenuti in questo percorso.

<b><u>CI TENIAMO AD ESSERE TRASPARENTI:</u></b>
Motivo per la quale vogliamo ricordarti che tutti i sistemi di Trading comportano dei rischi,
Non ci sono strategie che matematicamente garantiscano risultati concreti, ma questo non significa che non si possa essere profittevoli.

Proprio per questo ci siamo noi, cercheremo di fare un buon <i>ottimo</i> insieme, come quello che è già stato fatto con tanti altri clienti soddisfatti del nostro servizio gratuito. 😉❗️

Opera <b>sempre</b> con consapevolezza e responsabilità, vedrai che raggiungeremo grandi risultati assieme!

Qui sotto troverai tutte le nozioni che ti serviranno per iniziare questo percorso, con l'aggiunta del mio contatto.
Ti seguirò passo passo per qualsiasi cosa ti possa servire. ⬇️"""
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Scrivimi", url="https://t.me/Thom_fx12")],
                [InlineKeyboardButton("Vai alle Guide", url="https://t.me/Thom_guide_bot")]
            ])
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
