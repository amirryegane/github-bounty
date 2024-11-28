import telebot  

bot = telebot.TeleBot("7894662985:AAHGUelOBLN8o_80y-GBUY1GSVlwf2DmIaM")
auto_reply = "im busy plz try again"

is_offline = True

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "salam babe!")

@bot.message_handler(commands=['scrap'])
def scraper(message):
    import requests
    from bs4 import BeautifulSoup
	
    url = "https://github.com/arkadiyt/bounty-targets/commit/4e14c9ef847f6be6f3a925bda7ec14f9cc86b7b9"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text , 'html.parser')
    web_tag1 = soup.find_all('span' , class_ = 'pl-pds')
    web_tag2 = soup.find_all('span' , class_ = 'pl-v')
    web_tag3 = soup.find_all('span' , class_ = 'pl-v')
    web_tag4 = soup.find_all('span' , class_ = 'pl-en')
    for tag1, tag2, tag3, tag4 in zip(web_tag1, web_tag2, web_tag3, web_tag4):
        result = f"{tag1.text}: {tag2.text}:: {tag3.text}, {tag4.text}"
        print(result)
        bot.reply_to(message, {result})

bot.infinity_polling()
