import logging
from uuid import uuid4

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from _collections import defaultdict

import mysql.connector


# Utiliy function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K - 1, type))


# Logging:
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
LESSONNAME, LESSONDAY, LESSONTIME, LESSONDES = range(4)


# Command on start:
def start(update, context):
    update.message.reply_text("Hello there! I'm TBD and I'll help you with your school schedule!\nLet's start"
                              "with adding some lesson to your schedule.")


# Start of add_lesson main function states: NAME, DAY, TIME, DESCRIPTION:
def add_lesson(update, context):
    update.message.reply_text('What\'s the lesson name?')
    return LESSONNAME


def lessonname(update, context):
    reply_week = [['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun']]
    user = update.message.from_user
    key = str(uuid4())
    tmp_name = update.message.text
    context.user_data[key] = tmp_name
    logger.info("Name of %s: %s", user.title, tmp_name)
    update.message.reply_text('Now we know how to call it! Let\'s set a date')
    reply_markup = ReplyKeyboardMarkup(reply_week, one_time_keyboard=True)
    return LESSONDAY


def lessonday(update, context):
    user = update.message.from_user


def lessontime(update, context):
    print()


def lessondes(update, context):
    print()


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

    dp.add_handler(CommandHandler("start", start))

    # Here add the commands:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_lesson)],

        states={
            LESSONNAME: [MessageHandler(Filters.text, lessonname)],
            LESSONDAY: [MessageHandler(Filters.regex('^(Mon|Tue|Wen|Thu|Fri|Sat|Sun)$'), lessonday)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    dp.add_error_handler(error)

    # Bot Start:
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
