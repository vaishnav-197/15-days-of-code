import requests as requests
from covid import Covid
import json
covid = Covid()

url = "https://api.telegram.org/bot1200959445:AAH5rwX_74Z5H6Zdac9u0W-T3T5vV77voVU/"




# create func that get chat id
def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id

# function to get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

# function to get last update
def last_update(req):
    response = requests.get( req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result)-1
    return result[total_updates]


# function to send message to user
def send_message(chat_id , message_text) :
    params = {"chat_id" : chat_id, "text":message_text}
    response = requests.post( url+ "sendMessage" , data=params)
    return response

# Main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hii" or get_message_text(update).lower() == "hello" or get_message_text(update).lower() == "/start" :
                send_message(get_chat_id(update),'Hello welcome , its me Edith ,\n How  do you want me to help you \n 1.Motivation \n 2.Covid details \n 3.Stay tuned for more features.....\n Do you need Help then press "help"')
            
            elif  get_message_text(update).lower() == "help":
                send_message(get_chat_id(update)," \n Edith-Help\n For motivation ✨ try \n 1. Motivation\n 2. I need motivation \n\n For Covid-19 Details ")
            
            
            elif  get_message_text(update).lower() == "motivation " or get_message_text(update).lower() == "i need motivation"  or  get_message_text(update).lower() == "1":
                mot = requests.get("https://quotes.rest/quote/random?language=en&limit=1")
                mot = mot.json()
                send_message(get_chat_id(update),mot['contents']['quotes'][0]['quote'])
                send_message(get_chat_id(update)," end motivation What do you want me to do for you\n  1.Motivation \n 2.Covid details \n 3.Stay tuned for more features.....\n: Do you need Help")
            
            
            
            
            elif get_message_text(update).lower() == "Covid details" or  get_message_text(update).lower() == "2" :
                send_message(get_chat_id(update),"\n Covid-19 Details 🏥 \n  Choose from the following Details \n  Global Details\n  Search By Country ")
                
                
            elif get_message_text(update).lower() == "global details" :
                    reqcovid = requests.get("https://api.covid19api.com/summary")
                    responsecovid = reqcovid.json()
                    st=''
                    for i in responsecovid['Global'] :
                        st+= i + " : " +"\n"+ str(responsecovid['Global'][i]) 
                    
                    send_message(get_chat_id(update),"\n Covid-19 Global  Details 🏥 \n  " + st)
            elif get_message_text(update).lower() == "country details" :
                    send_message(get_chat_id(update),"\n  Enter the country name")
                    country = get_message_text(update).lower()
                    print(country)
                    country=covid.get_status_by_country_name(str(country))
                    send_message(get_chat_id(update)," Country Id: " + country["id"])
                    send_message(get_chat_id(update)," Country : " + country["country"])
                    send_message(get_chat_id(update)," confirmed : " + country["confirmed"])
                    send_message(get_chat_id(update)," active : " + country["active"])
                    send_message(get_chat_id(update)," deaths : " + country["deaths"])
                    send_message(get_chat_id(update)," recovered : " + country["recovered"])



                
                   
                    
            
            
            
            else :
                send_message(get_chat_id(update),'sorry command cannot be recognized ☹️ ☹️')
            update_id += 1
            

main()

