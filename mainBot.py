import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

# Logging:
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
LESSONNAME, DATE, LOCATION, BIO = range(4)

# Command Handlers:

# Command on start:
def start(update, context):
    update.message.reply_text("Hello there! I'm TBD and I'll help you with your school schedule!\nLet's start"
                              "with adding some lesson to your schedule.")


# Add lesson to schedule:
def add_lesson(update, context):
    print()


def lessonname(update, context):
    user = update.message.from_user
    logger.info("Name of %s: %s", user.title, update.message.text)
    update.message.reply_text('Now we know how to call it! Let\'s set a date')
    return DATE

# Remove lesson from schedule:
def rem_lesson(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active lesson.')
        return


# Show lessons to see:
def show_lessons(update, context):
    print()


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


# Manages errors
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Main:
def main():
    updater = Updater("1116601888:AAElt3W9Iw7Dav6TFmHId9ihZ9HT6qdoyZo", use_context=True)
    dp = updater.dispatcher

    # Here add the commands:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LESSONNAME: [MessageHandler(Filters.text, lessonname)]

        },

        fallbacks=[CommandHandler('cancel'), cancel]
    )
    dp.add_handler(CommandHandler("start", start))



    dp.add_error_handler(error)

    # Bot Start:
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()