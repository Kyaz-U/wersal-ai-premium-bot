import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from predict_model import predict_next_value

menu = ReplyKeyboardMarkup(
    keyboard=[
        ["▶️ Signal olish"],
        ["ℹ️ Yordam", "⚙️ Sozlamalar"]
    ],
    resize_keyboard=True
)

# Foydalanuvchi menyusi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum, Wersal AI botiga xush kelibsiz!\nKerakli bo‘limni tanlang:",
        reply_markup=menu
    )

# Xabarlar uchun handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "▶️ Signal olish":
        result = predict_next_value("aviator_1win", [1.59, 1.58, 1.32, 63.96, 6.89, 1.56, 4.48, 2.20, 2.14, 17.47])
        await update.message.reply_text(f"Aviator 1win uchun bashorat: {result}x")

    elif text == "ℹ️ Yordam":
        await update.message.reply_text("Yordam uchun: @UlugbekYusupov ga murojaat qiling.")

    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text("Sozlamalar hali mavjud emas. Tez orada yangilanadi.")

    else:
        await update.message.reply_text("Iltimos, menyudagi tugmalardan birini tanlang.")

# Botni ishga tushurish
if __name__ == '__main__':
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
