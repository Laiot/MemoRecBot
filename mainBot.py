import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Logging:
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Command Handlers:

# Command on start:
def start(update, context):
    update.message.reply_text("Hello there! I'm TBD and I'll help you with your school schedule!\nLet's start"
                              "with adding some lesson to your schedule.")


# Add lesson to schedule:
def add_lesson(update, context):
    print()


# Remove lesson from schedule:
def rem_lesson(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active lesson.')
        return


# Show lessons to see:
def show_lessons(update, context):
    print()


# Manages errors
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Main:
def main():
    updater = Updater("1116601888:AAElt3W9Iw7Dav6TFmHId9ihZ9HT6qdoyZo", use_context=True)
    dp = updater.dispatcher

    # Here add the commands:
    dp.add_handler(CommandHandler("start", start))

    dp.add_error_handler(error)

    # Bot Start:
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()