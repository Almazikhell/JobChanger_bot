import telebot
from telebot import types
from config import TOKEN
from telebot.types import Message
import json
import logging
from kb import generate_markup, generate_tags

bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.DEBUG)


def json_read() -> dict: # Чтение json
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def json_write(data: dict) -> None: # Запись в json
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data,file, ensure_ascii=False,indent=4)


@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    data = json_read()
    if str(message.chat.id) not in data["users"]:
        data["users"][str(message.chat.id)] = {"url":{},"tags":[],"form":[]}
        json_write(data)
    bot.send_message(message.chat.id, "Здравствуйте.")

@bot.message_handler(commands=["get_tags"])
def handle_get_tags(message: Message):
    data = json_read()



@bot.message_handler(commands=["new_form"])
def handle_new_form(message: Message):
    data = json_read()
    bot.send_message(message.chat.id, f"Введите ваше имя.")
    bot.register_next_step_handler_by_chat_id(message.chat.id, your_name)

def your_name(message: Message):
    text = message.text
    bot.send_message(message.chat.id, "Напишите ваш возраст.")
    bot.register_next_step_handler_by_chat_id(message.chat.id, your_age)
def your_age(message: Message):
    text = message.text
    bot.send_message(message.chat.id,"Напишите о себе.")
    bot.register_next_step_handler_by_chat_id(message.chat.id, your_bio)

def your_bio(message: Message):
    text = message.text
    bot.send_message(message.chat.id, "Прикрепите примеры своих работ.")
    bot.register_next_step_handler_by_chat_id(message.chat.id, your_examples)

def your_examples(message: Message):
    text = message.text
    bot.send_message(message.chat.id, "Создание анкеты завершено.")

bot.polling()