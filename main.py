import logging
import random

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5938990232:AAEoXvQhLyNtA3YmPJ5VrTxI_LGROA06kv8'

david_bowie_photos = {
    0: "https://media.newyorker.com/photos/631a6d059f86a85a3001e5f1/1:1/w_1806,h_1806,c_limit/220919_r41018.jpg",
    1: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2016%2F01%2Fdavid-bowie-1974.jpg",
    2: "https://pyxis.nymag.com/v1/imgs/2aa/e15/4c17ea093407990a4681e6d52f8ed19d30-22-david-bowie-2.2x.w710.jpg",
    3: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2016%2F01%2Fdavid-bowie-1965.jpg",
    4: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2016%2F01%2Fdavid-bowie-1971.jpg&q=60",
    5: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2016%2F01%2Fdavid-bowie-1974.jpg&q=60",
    6: "https://api.time.com/wp-content/uploads/2016/12/david-bowie-station-to-station-thin-white-duke-3-8-1_26.jpg",
    7: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2016%2F01%2Fdavid-bowie-1983.jpg&q=60",
    8: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2016%2F01%2Fdavid-bowie-1987.jpg&q=60",
    9: "https://www.galerieprints.com/wp-content/uploads/2020/01/Bowie-eyes-open-1.jpg",
    10: "https://i.pinimg.com/originals/02/25/65/0225658eb8fbe3708ef8d98a586fc02d.jpg"
}

david_bowie_captions = {
    0: "",
    1: "",
    2: "",
    3: "Еще совершенно молодой Дэвид Джонc. На этом фото ему 18. Он выпускает свой первый дебютный альбом.",
    4: "После выпуска Hunky Dory",
    5: "В туре Diamond Dogs, завершающий глэм эру",
    6: "В образе Thin White Duke. В последствии вся готик сцена будет вдохновляться им.",
    7: "Боуи после релиза двух мега-хитовых альбомов Scary Monsters и Let's Dance. Теперь он в роле поп-звезды.",
    8: "Тур после альбома Never Let me Down",
    9: "Зигги покоряет Америку",
    10: "Персонаж Зигги Стардаста, пришелец рок-звезда с ангдрогинной внешностью покоряет всю Европу"
}

culture_code_photos = {
    0: "https://akamai.sscdn.co/uploadfile/letras/fotos/0/9/3/b/093b9f9e35281efb9d86a1e33790947a.jpg",
    1: "https://upload.wikimedia.org/wikipedia/ru/thumb/a/a6/LedZeppelin1969Promo.JPEG/280px-LedZeppelin1969Promo.JPEG",
    2: "https://karsh.org/wordpress/wp-content/uploads/2016/10/Yousuf-Karsh-Ernest-Hemingway-1957-1558x1960.jpg",
    3: "https://upload.wikimedia.org/wikipedia/commons/1/10/H._P._Lovecraft%2C_June_1934.jpg",
    4: "https://www.rollingstone.com/wp-content/uploads/2018/06/rs-velvet-underground-nico-dc294bbb-3534-4a18-ba6a-4336a5699648.jpg",
    5: "https://upload.wikimedia.org/wikipedia/commons/5/54/Daniil_Kharms.jpg"
}

culture_code_captions = {
    0: "Группа Pink Floyd благодаря которым люди по всему миру знают, что такое дисперсия света.",
    1: "Хулиганы рок музыки великие и ужасные Led Zeppelin.",
    2: "Эрнест Хемингуэй",
    3: "Говард Лавкрафт",
    4: "The Velvet Underground",
    5: "Даниил Хармс"
}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply(
        "Привет! Этот бот галерея)\r\n\r\n\/david_bowie - За свою полувековую титаническую карьеру Дэвид Боуи успел перебрать множество образов — андрогинный глэм пришелец Зигги, меланхоличный экзистенциалист 70-х, виртуоз поп музыки 80-х и т.д. Этой командой вы сможете увидеть случайный отрывок из жизни самого влиятельного музыканта мира. \r\n\r\n\/culture_code - Эта команда выдает случайный культурный код. В основном то, что когда-то нравилось автору канала.")


@dp.message_handler(commands=['david_bowie'])
async def send_david_bowie(message: types.Message):
    index = random.randint(0, len(david_bowie_photos) - 1)
    await message.reply_photo(photo=david_bowie_photos[index], caption=david_bowie_captions[index])


@dp.message_handler(commands=['culture_code'])
async def send_culture_code(message: types.Message):
    index = random.randint(0, len(culture_code_photos) - 1)
    await message.reply_photo(photo=culture_code_photos[index], caption=culture_code_captions[index])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
