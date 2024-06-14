from config import token

import telebot
from PIL import Image, ImageOps
import io
import os
from random import choice

bot = telebot.TeleBot(token)

# Список интересных фактов на русском
fun_facts = [
    "Мёд никогда не портится. Археологи нашли горшки с мёдом в древнеегипетских гробницах, которым более 3000 лет, и мёд всё ещё был съедобен.",
    "Бананы – это ягоды, а клубника – нет.",
    "Во Вселенной больше звёзд, чем песчинок на всех пляжах мира.",
    "У осьминогов три сердца.",
    "Бабочки пробуют пищу ногами.",
    "День на Венере длится дольше, чем год на Венере.",
    "Какашки вомбатов имеют форму кубиков.",
    "У коал отпечатки пальцев почти неотличимы от человеческих.",
    "Группа фламинго называется 'фламбоянс'.",
    "Морские выдры держатся за руки во время сна, чтобы не разойтись по течению."
]

# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Получаем информацию о фотографии с наивысшим разрешением
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    # Создаем объект изображения из байтов
    image = Image.open(io.BytesIO(downloaded_file))
    
    # Инвертируем цвета изображения
    inverted_image = ImageOps.invert(image)
    
    # Сохраняем обработанное изображение временно
    temp_image_path = "temp_image.jpg"
    inverted_image.save(temp_image_path)
    
    # Отправляем обработанное изображение назад пользователю
    with open(temp_image_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)
    
    # Удаляем временный файл изображения
    os.remove(temp_image_path)

# Обработчик стикеров
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_message(message.chat.id, "Классный стикер!")

# Обработчик GIF-файлов
@bot.message_handler(content_types=['animation'])
def handle_gif(message):
    bot.send_message(message.chat.id, "Классный GIF!")

# Обработчик команд '/start' и '/hi'
@bot.message_handler(commands=['hi', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
дрова я бот по жожо и я могу выбрать станд для тиба напещь /stand_for_pvp чтоб начать и /info для инфы на англискам и есть /fun_fact и можно отправлать стикерь\
""")

# Обработчик команды '/info'
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, """\
hi am a jojo bot i can pick you a stand to pvp on in any game like yba and more for feedback text to nissakan1@gamil.com if you want me to add more stands""")

# Обработчик команды '/stand_for_pvp'
@bot.message_handler(commands=['stand_for_pvp'])
def coin_handler(message):
    coin = choice(["Anubis ", "King Crimson", "star platinum", "The World ", "stone free", "Whitesnake", "Red Hot Chili Pepper", "Crazy Diamond", "Killer Queen", "Gold Experience", "Silver Chariot", "Hermit Purple", "The Hando", "Purple Haze", "cream", "Hierophant Green", "Magician's Red", "White Album", "Aerosmith", "Six Pistols", "Beach Boy", "Mr. President", "Sticky Fingers", "soft & wet", "kcr", "ger", "sptw", "kqbd", "scary monster", "d4c", "twoh"])
    bot.reply_to(message, coin)

# Обработчик команды '/fun_fact'
@bot.message_handler(commands=['fun_fact'])
def fun_fact_handler(message):
    fact = choice(fun_facts)
    bot.send_message(message.chat.id, fact)

# Запуск бота с бесконечным опросом
bot.infinity_polling()



