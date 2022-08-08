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
    webhook.send(", ".join(str(x) for x in numbers), username = "Lottery Webhook")
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)