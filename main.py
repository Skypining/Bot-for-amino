#Library import
#Импорт библиотек
import amsync
from amsync.obj import Message
from amsync import Community, MakeImage, Color, Message, File, ProgressBar, Embed
import random
import fuzzywuzzy
from fuzzywuzzy import fuzz, process
import numpy as np
from gtts import gTTS


user = amsync.User()
bot = amsync.Bot('email', 'passworld', prefix='!')# write email and passworld for your bot account. Логин и пароль для входа в аккаунт бота
list = np.array( ['Приветик', 'Бонжур', 'Салют','Здраствуй','Салютик','Хаюшки',"Кусб","Hi","Мяу","hello","Хелоу"], str)

#Оповещение когда бот отключается 
#close_socket
@bot.on()
async def close():
    print('Bot close')


#ready
@bot.on()
async def ready():
    print('Ready')


@bot.on()
async def message(m: Message):
    print(f'Log# | {m.nickname} | {m.text} | {m.chat}')


#Приветствие
#Greeting
@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Привет")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")

@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Хола")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")

@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Здраствуй")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")

@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Добрый день")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")

@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Бонжур")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")

@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Всем привет")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")

@bot.on()
async def message(m: Message):
    rsp = m.text
    if ((fuzz.ratio(rsp, "Мяу")) > 70) and m.uid != bot.id:
        await bot.send(f"{random.choice(list)}, {m.nickname}!")


#bot_commands

#love_command
#you can use user special put for user
#Можно поставить специальний текст для кого либо
@bot.add()
async def love(m: Message):
    if m.uid != bot.id:
        u1 = m.mentioned_users[0]
        nck1 = (await user.search(u1))[0].nickname
        nckid1 = (await user.search(u1))[0].id
        u2 = m.mentioned_users[1]
        nck2 = (await user.search(u2))[0].nickname
        nckid2 = (await user.search(u2))[0].id
        if nckid1 == '2680cedd-dba7-4fc7-8d83-9222fe556f45' or nckid2 == '2680cedd-dba7-4fc7-8d83-9222fe556f45':
            await bot.send("")
        else:
            await bot.send(f"Вероятность любви между {nck1} и {nck2} равна {random.randint(0,100)}%")


#help command
@bot.add()
async def help(m: Message):
    if m.uid != bot.id:
        await bot.send("[BC][📄]Информация о боте\n!ui - Информация о себе.\n!vcru [text] - Записывает голосовое по сообщению.\n!vcen - То же самое что !vcru, но на английском\n!vcuk - То же самое что !vcen, но на украинском\n!love [@ник] [@ник] - Вероятность любви.\n!chats - Вывод главных чатов для общения.\n\n!adpanel - Админ панель(Только для админов)\n!работаешь - Проверка не уснул ли бот =)")

#text to speech(English)
#Текст в голосовое сообщение
@bot.add()
async def vcen(m: Message):
    myobj = gTTS(text=m.text, lang='en', slow=False)
    myobj.save("gsen.mp3")
    if m.uid != bot.id:
        await bot.send(files='gsen.mp3')
        

#text to speech(Russian)
#Текст в голосовое сообщение
@bot.add()
async def vcru(m: Message):
    myobj = gTTS(text=m.text, lang='ru', slow=False)
    myobj.save("gsru.mp3")
    if m.uid != bot.id:
        await bot.send(files='gsru.mp3')


#text to speech(France)
#Текст в голосовое сообщение
@bot.add()
async def vcfr(m: Message):
    myobj = gTTS(text=m.text, lang='fr', slow=False)
    myobj.save("gsfr.mp3")
    if m.uid != bot.id:
        await bot.send(files='gsfr.mp3')


#text to speech(Ukrainian)
#Текст в голосовое сообщение
@bot.add()
async def vcuk(m: Message):
    myobj = gTTS(text=m.text, lang='uk', slow=False)
    myobj.save("gsuk.mp3")
    if m.uid != bot.id:
        await bot.send(files='gsuk.mp3')


#bot status check
@bot.add()
async def работаешь(m: Message):
    if m.uid != bot.id:
        await bot.send("Увы, но работаю...")


#simple find command
@bot.add()
async def find(m: Message):
    if m.uid != bot.id:
        await bot.send(f"https://google.gik-team.com/?q={m.text}")


#other chats info
@bot.add()
async def chats(m: Message):
    if m.uid != bot.id:
        await bot.send("")#


#В разработке
#In development
@bot.add()
async def adpanel(m: Message):
    if m.uid != bot.id:
        await bot.send("[BC][💻]Админ панель\n!night — Пожелать участникам спокойной ночи.\n!morn — Пожелать доброго утро участникам.\n!chatId — Узнать айди данного чата, в котором вы находитесь.\n!save — Сохранить чат.\n!loadsave — Загрузить сохранëнный чат.\n!online, !offline — Изменить статус боту.")


#В разработке
#In development
@bot.add()
async def rank(m: Message):
    im = MakeImage.open('te.png')
    im.resize((934, 282))
    ico = await File.get(m.icon)

    icon = MakeImage.from_bytes(ico)
    if MakeImage.type(ico) == 'gif':
        icon = icon.to_img()

    icon.resize((165, 165))
    icon.circular_thumbnail()
    icon.add_border(2, Color.BLACK)

    pg = ProgressBar((620, 35), 15, color=Color.CYAN, bg_color=Color.GRAY)
    pg.update(10)
    pg.add_border(2, Color.BLACK)
    rep = (await user.search(m.uid))[0].reputation

    im.text('Reputation', 'center', (135, -45), ('lato.light.ttf', 24))
    im.text(f'{rep}', 'center', (205, -59), ('lato.medium.ttf', 52))
    lev = (await user.search(m.uid))[0].level

    im.text('LEVEL', 'center', (300, -46), ('lato.light.ttf', 26), Color.CYAN)
    im.text(f'{lev}', 'center', (360, -59), ('lato.medium.ttf', 54), Color.CYAN)

    im.text(m.nickname, 'center', (-120, 15), ('lato.medium.ttf', 32))

    im.text('5', 'right', (-170, 15), ('lato.medium.ttf', 26))
    im.text('/ 100 XP', 'right', (-55, 15), ('lato.medium.ttf', 26), Color.GRAY)
    
    im.paste(icon, 'left', (50, 0))
    im.paste(pg, 'center', (115, 60))
    await bot.send(files=im.bytes)


#Chat_backup


#Приветсвие при входе в чат нового пользователя
#Greeting when somebody join to chat
@bot.on()
async def join_chat(m: Message):
    await bot.send(f"Здраствуй, @{m.nickname}!\nДобро пожаловать в наш чат!\n Не забудь ознакомится с его правилами, удачи!")

#Info about user
#Информация о пользователе
@bot.add()
async def ui(m: Message):
    u1 = (await user.search(m.uid))[0].level
    u2 = (await user.search(m.uid))[0].role
    u3 = (await user.search(m.uid))[0].created_time
    u4 = (await user.search(m.uid))[0].followers_count
    u5 = (await user.search(m.uid))[0].comments_count
    u6 = (await user.search(m.uid))[0].blogs_count
    u7 = (await user.search(m.uid))[0].reputation
    await bot.send(f'\n[BC]Info about user: {m.nickname}👀 \n[😎]level: {u1} \n[🚀]Role: {u2}\n[🥳]Reputation: {u7}\n[🤩]Followers: {u4}\n[📄]blogs count: {u6}\n[⚡]Comments count: {u5}\n[🕝]Date of entry into the community: {u3}')


#айди пользователя
#user_id
@bot.add()
async def id(m: Message):
    if m.uid != bot.id:
        idu = m.mentioned_users[0]
        id1 =  (await user.search(idu))[0].id
        await bot.send(f"id: {id1}")








bot.run()