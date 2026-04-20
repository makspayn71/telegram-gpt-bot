from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    response = client.responses.create(
        model="gpt-4.1",
        input=text
    )

    answer = response.output_text
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(os.environ["8688885611:AAFTAk83oj7PQKDrxzanpJu8ZDLgi_ZR-ek"]).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
