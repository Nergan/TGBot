import telebot # official documentation --> pypi.org/project/pyTelegramBotAPI/0.3.0
import time

# set proxy [ OPTIONAL ]
if False:
    from telebot import apihelper
    apihelper.proxy = {'https': 'IP/URL'}

# Where to get a token:
# 1) In Telegram, you need to go to @BotFather.
# 2) Write /newbot.
# 3) Enter the invented name of the bot.
# 4) Enter the invented unique token.

# Remove bot:
# 1) In telegram, you need to go to @BotFather.
# 2) Write /deletebot.
# 3) Enter the 'Yes, I am totally sure.'

bot = telebot.TeleBot('YOUR TOKEN') # bot token

# command event
@bot.message_handler(commands=['start', 'help']) # list of monitored commands
def userCmd(cmd):
    
    # send msg
    if False:
        bot.send_message(cmd.chat.id, 'MESSAGE TEXT', parse_mode='html')

    # send img   
    elif False:
        with open('imgPath', 'rb') as img:
            bot.send_photo(cmd.chat.id, img)
    
    # send audio
    elif False:
        with open('audioPath', 'rb') as audio:
            bot.send_audio(cmd.chat.id, audio)
    
    # send voice (extension file .ogg)
    elif False:
        with open('voicePath', 'rb') as voice:
            bot.send_voice(cmd.chat.id, voice)
    
    # send document
    elif False:
        with open('docPath', 'rb') as doc:
            bot.send_document(cmd.chat.id, doc)
    
    # send sticker
    elif False:
        with open('stiPath', 'rb') as sti:
            bot.send_sticker(cmd.chat.id, sti)
    
    # send video
    elif False:
        with open('videoPath', 'rb') as video:
            bot.send_video(cmd.chat.id, video)
    
    # send videonote
    elif False:
        with open('vnotePath', 'rb') as vnote:
            bot.send_video_note(cmd.chat.id, vnote)
            
    # send one-time button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        # buttonCallback is the value sent by the button to the system
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
        
        bot.send_message(cmd.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
    # send url-button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
        
        bot.send_message(cmd.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
        
    # set button on control panel
    elif False:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        for _ in range(2): # button count
            markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
        
        bot.send_message(cmd.chat.id, 'BUTTON CREATED', reply_markup=markup)
        
    # default action    
    else:
        pass

# text event
@bot.message_handler(content_types=['text'])
def userTxt(txt):
    
    # send msg
    if False:
        bot.send_message(txt.chat.id, 'MESSAGE TEXT', parse_mode='html')

    # send img   
    elif False:
        with open('imgPath', 'rb') as image:
            bot.send_photo(txt.chat.id, image)
    
    # send audio
    elif False:
        with open('audioPath', 'rb') as audio:
            bot.send_audio(txt.chat.id, audio)
    
    # send voice (extension file .ogg)
    elif False:
        with open('voicePath', 'rb') as voice:
            bot.send_voice(txt.chat.id, voice)
    
    # send document
    elif False:
        with open('docPath', 'rb') as doc:
            bot.send_document(txt.chat.id, doc)
    
    # send sticker
    elif False:
        with open('stiPath', 'rb') as sti:
            bot.send_sticker(txt.chat.id, sti)
    
    # send video
    elif False:
        with open('videoPath', 'rb') as video:
            bot.send_video(txt.chat.id, video)
    
    # send videonote
    elif False:
        with open('vnotePath', 'rb') as vnote:
            bot.send_video_note(txt.chat.id, vnote)
            
    # send one-time button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        # buttonCallback is the value sent by the button to the system
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
        
        bot.send_message(txt.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
    # send url-button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
        
        bot.send_message(txt.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
        
    # set button on control panel
    elif False:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        for _ in range(2): # button count
            markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
        
        bot.send_message(txt.chat.id, 'BUTTON CREATED', reply_markup=markup)
            
    # default action    
    else:
        pass
    
# sticker event
@bot.message_handler(content_types=['sticker'])
def userSticker(sti):
    
    # send msg
    if False:
        bot.send_message(sti.chat.id, 'MESSAGE TEXT', parse_mode='html')

    # send img   
    elif False:
        with open('imgPath', 'rb') as img:
            bot.send_photo(sti.chat.id, img)
    
    # send audio
    elif False:
        with open('audioPath', 'rb') as audio:
            bot.send_audio(sti.chat.id, audio)
    
    # send voice (extension file .ogg)
    elif False:
        with open('voicePath', 'rb') as voice:
            bot.send_voice(sti.chat.id, voice)
    
    # send document
    elif False:
        with open('docPath', 'rb') as doc:
            bot.send_document(sti.chat.id, doc)
    
    # send sticker
    elif False:
        with open('stiPath', 'rb') as stick:
            bot.send_sticker(sti.chat.id, stick)
    
    # send video
    elif False:
        with open('videoPath', 'rb') as video:
            bot.send_video(sti.chat.id, video)
    
    # send videonote
    elif False:
        with open('vnotePath', 'rb') as vnote:
            bot.send_video_note(sti.chat.id, vnote)
            
    # send one-time button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        # buttonCallback is the value sent by the button to the system
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
        
        bot.send_message(sti.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
    # send url-button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
        
        bot.send_message(sti.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
        
    # set button on control panel
    elif False:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        for _ in range(2): # button count
            markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
        
        bot.send_message(sti.chat.id, 'BUTTON CREATED', reply_markup=markup)
            
    # default action    
    else:
        pass

# pinned message event
@bot.message_handler(content_types=['pinned_message'])
def userPMsg(pmsg):
    
    # send msg
    if False:
        bot.send_message(pmsg.chat.id, 'MESSAGE TEXT', parse_mode='html')

    # send img   
    elif False:
        with open('imgPath', 'rb') as img:
            bot.send_photo(pmsg.chat.id, img)
    
    # send audio
    elif False:
        with open('audioPath', 'rb') as audio:
            bot.send_audio(pmsg.chat.id, audio)
    
    # send voice (extension file .ogg)
    elif False:
        with open('voicePath', 'rb') as voice:
            bot.send_voice(pmsg.chat.id, voice)
    
    # send document
    elif False:
        with open('docPath', 'rb') as doc:
            bot.send_document(pmsg.chat.id, doc)
    
    # send sticker
    elif False:
        with open('stiPath', 'rb') as sti:
            bot.send_sticker(pmsg.chat.id, sti)
    
    # send video
    elif False:
        with open('videoPath', 'rb') as video:
            bot.send_video(pmsg.chat.id, video)
    
    # send videonote
    elif False:
        with open('vnotePath', 'rb') as vnote:
            bot.send_video_note(pmsg.chat.id, vnote)
            
    # send one-time button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        # buttonCallback is the value sent by the button to the system
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
        
        bot.send_message(pmsg.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
    # send url-button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
        
        bot.send_message(pmsg.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
        
    # set button on control panel
    elif False:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        for _ in range(2): # button count
            markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
        
        bot.send_message(pmsg.chat.id, 'BUTTON CREATED', reply_markup=markpmsg)
            
    # default action    
    else:
        pass

# photo event
@bot.message_handler(content_types=['photo'])
def userImg(img):
    
    # send msg
    if False:
        bot.send_message(img.chat.id, 'MESSAGE TEXT', parse_mode='html')

    # send img   
    elif False:
        with open('imgPath', 'rb') as image:
            bot.send_photo(img.chat.id, image)
    
    # send audio
    elif False:
        with open('audioPath', 'rb') as audio:
            bot.send_audio(img.chat.id, audio)
    
    # send voice (extension file .ogg)
    elif False:
        with open('voicePath', 'rb') as voice:
            bot.send_voice(img.chat.id, voice)
    
    # send document
    elif False:
        with open('docPath', 'rb') as doc:
            bot.send_document(img.chat.id, doc)
    
    # send sticker
    elif False:
        with open('stiPath', 'rb') as sti:
            bot.send_sticker(img.chat.id, sti)
    
    # send video
    elif False:
        with open('videoPath', 'rb') as video:
            bot.send_video(img.chat.id, video)
    
    # send videonote
    elif False:
        with open('vnotePath', 'rb') as vnote:
            bot.send_video_note(img.chat.id, vnote)
            
    # send one-time button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        # buttonCallback is the value sent by the button to the system
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
        
        bot.send_message(img.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
    # send url-button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
        
        bot.send_message(img.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
        
    # set button on control panel
    elif False:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        for _ in range(2): # button count
            markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
        
        bot.send_message(img.chat.id, 'BUTTON CREATED', reply_markup=markpmsg)
            
    # default action    
    else:
        pass

# audio event
@bot.message_handler(content_types=['audio'])
def userAudio(aud):
    
    # send msg
    if False:
        bot.send_message(aud.chat.id, 'MESSAGE TEXT', parse_mode='html')

    # send img   
    elif False:
        with open('imgPath', 'rb') as image:
            bot.send_photo(aud.chat.id, image)
    
    # send audio
    elif False:
        with open('audioPath', 'rb') as audio:
            bot.send_audio(aud.chat.id, audio)
    
    # send voice (extension file .ogg)
    elif False:
        with open('voicePath', 'rb') as voice:
            bot.send_voice(aud.chat.id, voice)
    
    # send document
    elif False:
        with open('docPath', 'rb') as doc:
            bot.send_document(aud.chat.id, doc)
    
    # send sticker
    elif False:
        with open('stiPath', 'rb') as sti:
            bot.send_sticker(aud.chat.id, sti)
    
    # send video
    elif False:
        with open('videoPath', 'rb') as video:
            bot.send_video(aud.chat.id, video)
    
    # send videonote
    elif False:
        with open('vnotePath', 'rb') as vnote:
            bot.send_video_note(aud.chat.id, vnote)
            
    # send one-time button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        # buttonCallback is the value sent by the button to the system
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
        
        bot.send_message(aud.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
    # send url-button
    elif False:
        markup = telebot.types.InlineKeyboardMarkup()
    
        for _ in range(2): # button count
            markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
        
        bot.send_message(aud.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
        
    # set button on control panel
    elif False:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        for _ in range(2): # button count
            markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
        
        bot.send_message(aud.chat.id, 'BUTTON CREATED', reply_markup=markpmsg)
            
    # default action    
    else:
        pass

# one-time button click event
@bot.callback_query_handler(func = lambda call: True)
def pressButton(button):
    
    # button.data is a way of accessing the value of a one-time button sent to the system
    # 'buttonCallback' is the value of the message sent by the one-time button to the system
    # access the chat via the variable one-time button to display a message - button.message.chat.id
    
    if button.data == 'buttonCallback':
        
        # send msg
        if False:
            bot.send_message(button.message.chat.id, 'MESSAGE TEXT', parse_mode='html')

        # send img   
        elif False:
            with open('imgPath', 'rb') as image:
                bot.send_photo(aud.chat.id, image)
        
        # send audio
        elif False:
            with open('audioPath', 'rb') as audio:
                bot.send_audio(button.message.chat.id, audio)
        
        # send voice (extension file .ogg)
        elif False:
            with open('voicePath', 'rb') as voice:
                bot.send_voice(button.message.chat.id, voice)
        
        # send document
        elif False:
            with open('docPath', 'rb') as doc:
                bot.send_document(button.message.chat.id, doc)
        
        # send sticker
        elif False:
            with open('stiPath', 'rb') as sti:
                bot.send_sticker(button.message.chat.id, sti)
        
        # send video
        elif False:
            with open('videoPath', 'rb') as video:
                bot.send_video(button.message.chat.id, video)
        
        # send videonote
        elif False:
            with open('vnotePath', 'rb') as vnote:
                bot.send_video_note(button.message.chat.id, vnote)
                
        # send one-time button
        elif False:
            markup = telebot.types.InlineKeyboardMarkup()
        
            # buttonCallback is the value sent by the button to the system
            for _ in range(2): # button count
                markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', callback_data='buttonCallback'))
            
            bot.send_message(button.message.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
                
        # send url-button
        elif False:
            markup = telebot.types.InlineKeyboardMarkup()
        
            for _ in range(2): # button count
                markup.add(telebot.types.InlineKeyboardButton('BUTTON TEXT', url='https://google.com'))
            
            bot.send_message(button.message.chat.id, 'MESSAGE TO BUTTONS', reply_markup=markup)
            
        # set button on control panel
        elif False:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        
            for _ in range(2): # button count
                markup.add(telebot.types.KeyboardButton('BUTTON TEXT'))
            
            bot.send_message(button.message.chat.id, 'BUTTON CREATED', reply_markup=markpmsg)
                
        # default action    
        else:
            pass
         
    else:
        pass
        
# the bot starts and runs while the program is running
end = False
while not end:
    try:
        print('Bot is running')
        bot.infinity_polling()
        end = True
    
    # in case of an error, the bot restarts after a few seconds
    except Exception as ex:
        print(ex)
        time.sleep(15)
