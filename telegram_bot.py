import os

from telebot import TeleBot

if __name__ == "__main__":
    TOKEN = os.environ["TOKEN"]
    bot = TeleBot(TOKEN)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        msg = "Привет, я чат-бот, который классифицирует изображения как число от 0 до 9 :)"
        bot.send_message(message.chat.id, msg)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        msg = "Отправь мне изображение, чтобы я мог классифицировать его :)"
        bot.send_message(message.chat.id, msg)

    # @bot.message_handler(content_types=["photo"])
    # def send_image(message):
    #     fileID = message.photo[-1].file_id
    #     file = bot.get_file(fileID)
    #     downloaded_file = bot.download_file(file.file_path)

    #     arr = Image.open(io.BytesIO(downloaded_file))
    #     arr = np.array(arr)
    #     caption = apply_model_to_image(arr)

    #     translations = translator.translate(caption, dest="ru", src="en")
    #     ru_caption = translations.text

    #     bot.send_message(message.chat.id, "{}\n{}".format(caption, ru_caption))

    bot.polling()
