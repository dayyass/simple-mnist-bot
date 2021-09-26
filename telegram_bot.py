import os

from telebot import TeleBot
from tensorflow import keras

from utils import inference, preprocess_image


def get_bot():
    bot = TeleBot(os.environ["TOKEN"])
    return bot


def get_model(path):
    model = keras.models.load_model(path)
    return model


if __name__ == "__main__":

    # get telegram bot
    bot = get_bot()

    # get keras model
    model = get_model(path="model")

    @bot.message_handler(commands=["start"])
    def start_message(message):
        msg = "Привет, я чат-бот, который классифицирует изображения как число от 0 до 9 :)"
        bot.send_message(message.chat.id, msg)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        msg = "Отправь мне изображение, чтобы я мог классифицировать его :)"
        bot.send_message(message.chat.id, msg)

    @bot.message_handler(content_types=["photo"])
    def send_image(message):

        fileID = message.photo[-1].file_id
        file = bot.get_file(fileID)
        downloaded_file = bot.download_file(file.file_path)

        img = preprocess_image(downloaded_file)
        cls = inference(model, img)

        msg = f"На фотографии изображено число {cls}"
        bot.send_message(message.chat.id, msg)

    bot.polling()
