"""
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

openai_api_key = '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'
bot_token = '6864686536:AAF4eZtm7LUkgKAQkz-BI1uKtxt-R_Ntkh8'

def help_command(update, context):
    # Implement the help message  

def start_command(update, context):
    # Implement the start response
    
def handle_message(update, context):
    message = update.message.text
    chat_id = update.message.chat_id
    user = update.message.from_user
    first_name = user.first_name

# Implement conversation history and OpenAI response   
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('name', name_command))
dispatcher.add_handler(CommandHandler('desc', desc_command))
dispatcher.add_handler(CommandHandler('website', website_command))
dispatcher.add_handler(CommandHandler('contact', contact_command))
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))
updater.start_polling() 
"""
#-----------------------------------------------------------------------------
import logging
import callgpt4  #내가 만든 bot 등장
from telegram import __version__ as TG_VER
token = "telegram token 넣어주세요"


try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0) 

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"안녕 {user.mention_html()}!, 나는 chatgpt 고구마 봇이야",
        reply_markup=ForceReply(selective=True),
    )


async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """gpt모듈을 호출하는것."""
    print (update.message.text)
    await update.message.reply_text("......") #bot이 응답을 준비하는동한 메세지로 ......을 보냄
    userPrompt = update.message.text
    gptresult = callgpt4.help(userPrompt)
    await update.message.reply_text(gptresult) #bot의 답변을 메세지로 보냄

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gpt))
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()