import requests as requests

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
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello" :
                send_message(get_chat_id(update),'Hello welcome , its me Edith ')
            else :
                send_message(get_chat_id(update),'sorry command cannot be recognized :(')
            update_id += 1
            

main()

