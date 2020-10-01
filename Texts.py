import random, schedule, time
from twilio.rest import Client


GOOD_MORNING_QUOTES = [
    "good morning :)", 
    "gm homie",
    "gm"
]

cellphone = "any number - certify it first through twilio"
twilio_number = "twilio api num"
twilio_account = "key"
twilio_token = "token"

def send_message(quotes_list = GOOD_MORNING_QUOTES):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, (len(quotes_list)-1))]

    client.messages.create(body = quote, from_=twilio_number, to= cellphone)



schedule.every().day.at("00:00").do(send_message, GOOD_MORNING_QUOTES)

while True:
    schedule.run_pending()
    time.sleep(2)