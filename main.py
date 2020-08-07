import logging, os
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, JobQueue


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

wake_sleep = ['wake_sleep']

def start(bot, update):
    intro = '''
This bot is a sleep calculator that helps you to calculate the best timings to sleep and wake up, in accordance with the REM Sleep Cycle. 

More information about REM sleep cycles: 
https://www.tuck.com/stages/

GitHub: 
https://github.com/keithwongg/REM-Sleep-Calculator


** Welcome to the Sleep Calculator Bot **

Instructions:

Click on either commands:
1. /wake -  Find out what time to WAKE UP
2. /sleep - Find out what time to SLEEP
'''
    bot.send_message(chat_id=update.message.chat_id, text=intro)    

def wake(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='''Enter Sleep Timing \n 
Note: Timings must be entered in 24 hour format.
e.g 6.00 pm should be entered as 1800.''', reply_markup=ForceReply())
    wake_sleep[0] = 'wake'

def sleep(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='''Enter Wake Up Timing \n 
Note: Timings must be entered in 24 hour format.
e.g 6.00 pm should be entered as 1800.''', reply_markup=ForceReply())
    wake_sleep[0] = 'sleep'

def wake_or_sleep(bot, update):
    if wake_sleep[0] == 'wake':
        # print('wake up choice')
        user_time = update.message.text
        
        # validation handling
        try:
            if int(user_time) > 2400 or int(user_time) < 0 or len(user_time) != 4:
                bot.send_message(chat_id=update.message.chat_id, text = "Invalid Input. Please enter time in 24 hour format, between 0001 and 2400")
                return 0
        except ValueError:
            bot.send_message(chat_id=update.message.chat_id, text = "Invalid Input. Input is not a number. Please enter time in 24 hour format.")
            return 0

        from wake import sleep_calculator
        wake_timings = sleep_calculator(user_time)
        print_text = print_results(wake_timings, 'Wake Up')
        bot.send_message(chat_id=update.message.chat_id, text = print_text)

    elif wake_sleep[0] == 'sleep':
        # print('sleep choice')
        user_time = update.message.text
        # validation handling
        try:
            if int(user_time) > 2400 or int(user_time) < 0 or len(user_time) != 4:
                bot.send_message(chat_id=update.message.chat_id, text = "Invalid Input. Please enter time in 24 hour format, between 0001 and 2400")
                return 0
        except ValueError:
            bot.send_message(chat_id=update.message.chat_id, text = "Invalid Input. Input is not a number. Please enter time in 24 hour format.")
            return 0
            
        from sleep import sleep_calculator
        sleep_timings = sleep_calculator(user_time)
        print_text = print_results(sleep_timings, 'Sleep')
        bot.send_message(chat_id=update.message.chat_id, text = print_text)
    else:
        print('Error Please Try Again')
        return 0


def print_results(sleep_or_wake_timings, sleep_or_wake):
    rem_sleep_timings = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5]
    str_to_return = ''
    for i,time in enumerate(rem_sleep_timings):
        str_to_return += f'{sleep_or_wake} at {sleep_or_wake_timings[i]} and get {time} hours of sleep \n'
    return str_to_return


def main():
    # key = open('apikey.txt', 'r')
    updater = Updater(os.environ['API_KEY'])

    # Dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("wake", wake))
    dp.add_handler(CommandHandler("sleep", sleep))
    dp.add_handler(MessageHandler(Filters.reply, wake_or_sleep))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()