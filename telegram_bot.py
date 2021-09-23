import os

from telebot import TeleBot
from tensorflow import keras

from .utils import preprocess_image

if __name__ == "__main__":

    TOKEN = os.environ["TOKEN"]
    bot = TeleBot(TOKEN)

    model = keras.models.load_model("model")

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
        logits = model(img)
        cls = logits.numpy()[0].argmax()

        bot.send_message(message.chat.id, cls)

    bot.polling()
