from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    sticker_id = 'your_sticker_id_here'  # Replace with your sticker ID
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sticker_id)

def main():
    updater = Updater(token='your_bot_token_here', use_context=True)
    dispatcher = updater.dispatcher

    # Add a handler for the /start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
