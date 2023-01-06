import logging
import random
import csv
from csv import writer
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import config as cfg

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class Csv_Handle:
    # def __init__(self):
    #     self.answer = ""
        
    def get_answer(self):
        with open("answers.csv") as csvdatei:
            csv_reader_object = csv.reader(csvdatei, delimiter=',')
            answers = []
            for row in csv_reader_object:
                answers.append(row)
            answer = random.choice(answers)
            csvdatei.close()
            return answer
        
    def add_entry(self, entry):
        with open("answers.csv", 'a', newline='') as f_object:
            writer_object = writer(f_object)
            list_data = [entry]
            writer_object.writerow(list_data)
            f_object.close()
            
def blaaa(s):
    ret = ""
    i = True  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret                           
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args).upper()
    bla_return = blaaa(text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bla_return)
    

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
########################

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    csv_data = Csv_Handle()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(csv_data.get_answer()))
#########################

# async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     text_caps = ' '.join(context.args).upper()
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#########################

async def blabla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    bla_return = blaaa(text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bla_return)

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entry = ""
    for item in context.args:
        entry = entry + item  + " " 
    csv_data = Csv_Handle()
    csv_data.add_entry(entry)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="added " + entry)
##########################
    
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message()
    
if __name__ == '__main__':
    application = ApplicationBuilder().token(cfg.TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    add_handler = CommandHandler('add', add)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    bla_handler = CommandHandler('blabla', blabla)
    
    application.add_handler(start_handler)
    application.add_handler(add_handler)
    application.add_handler(echo_handler)
    application.add_handler(bla_handler)
    
    application.run_polling()