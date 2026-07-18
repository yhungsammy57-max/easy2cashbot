from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, WHATSAPP_CHANNEL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join WhatsApp Channel", url=WHATSAPP_CHANNEL)],
        [InlineKeyboardButton("✅ CHECK", callback_data="check")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to EASY2CASHBOT!\n\n"
        "Join our WhatsApp Channel first, then tap CHECK.",
        reply_markup=reply_markup
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "✅ Thanks!\n\nYou can now receive our updates.\n\n"
        "⚠️ Note: Telegram cannot automatically verify WhatsApp Channel membership."
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check, pattern="check"))

app.run_polling()
