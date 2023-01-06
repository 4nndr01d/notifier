import os

from celery import shared_task
import telebot


@shared_task()
def send_notifications_to_channels_task(text):
    token = os.environ.get('TG_TOKEN')
    channel_name = os.environ.get('TG_CHANNEL_NAME')

    bot = telebot.TeleBot(token)
    bot.config['api_key'] = token
    bot.send_message(channel_name, text)
