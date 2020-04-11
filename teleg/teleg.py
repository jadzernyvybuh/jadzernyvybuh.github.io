import telebot
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)



# main variables

TOKEN = "1120903746:AAEqlzOT0E9YsCKr0N7-er3JbgS94YztTfQ"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('about us', 'donations')
    bot.send_message(message.chat.id, 'hello! here you can record or leave your voice!', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "about us":
        bot.send_message(chat_id,
                         'we are a collection of proactive people who believe in the future and the development of AI '
                         '. your voices that you leave here will  help the creators of voice assistans, synyhesizers. '
                         'who knows, maybe in a year we will tell our amazing story in YOUR VOICE')
    elif text == "donations":
        bot.send_message(chat_id, 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2JVSCG6WL7XBW')
    else:
        bot.send_message(message.chat.id, "just send me your voice")
        print(message)

@bot.message_handler(content_types=['voice', 'audio'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "thank's a lot, you also can send me more voices!")
    print('+1')


                                                                                                                
    # Create GoogleDrive instance with authenticated GoogleAuth instance.                                       
    #drive = GoogleDrive(gauth)
                                                                                                                
    # Create GoogleDriveFile instance with title 'Hello.txt'.                                                   
    #file1 = drive.CreateFile({'title': 'Hello.txt'})
    file1.Upload() # Upload the file.                                                                           
    print('title: %s, id: %s' % (file1['title'], file1['id']))                                                  
    # title: Hello.txt, id: {{FILE_ID}}                                                                         
                                                                                                                






bot.polling()

# View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "bot"):
      fileID = file['id']

file1 = drive.CreateFile({"mimeType": "image", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
file1.SetContentFile("small_file.csv")
file1.Upload() # Upload the file.
print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))  
































