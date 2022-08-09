from lottery.controller import LotteryController
import schedule
import time
import requests
from discord import Webhook, RequestsWebhookAdapter
import configparser

def job():
    dc = LotteryController()
    numbers = dc.draw_numbers()
    config = configparser.ConfigParser()
    config.read('tokens.cfg')
    id = config.get('WEBHOOK', 'id')
    token = config.get('WEBHOOK', 'token')
    webhook = Webhook.partial(id, token, adapter=RequestsWebhookAdapter())
    #webhook.send("1,2,3,4,5,6", username="Lottery Webhook")
    webhook.send(",".join(str(x) for x in numbers), username = "Lottery Webhook")

schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)