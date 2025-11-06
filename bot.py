import discord
number = 0
score = 0
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    global number
    global score
    number = number
    score = score
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    global number
    global score
    number = number
    score = score
    if message.author == client.user:
        return
    if message.content.startswith('$TEST'):
        number = 0
        await message.channel.send("Bot çalışıyor")
        return
    if number == 0:
        await message.channel.send("Kaç tane ampül kullanıyorsunuz? A)1 B)1 ile 3 arasında C)3 ile 5 arasında D) 5'den fazla")
        number = number + 1
    if number == 1 and message.content.startswith('$A'):
        score = score + 40
        number = number + 1
    elif number == 1 and message.content.startswith('$B'):
        score = score + 30
        number = number + 1
    elif number == 1 and message.content.startswith('$C'):
        score = score + 20
        number = number + 1
    elif number == 1 and message.content.startswith('$D'):
        score = score + 10
        number = number + 1
    elif number == 2:
        await message.channel.send("Nasıl bir diyetiniz var? A)Vegan B)Vejetaryen C)Karışık D)Sadece et")
        number = number + 1
    elif number == 3 and message.content.startswith('$A'):
        score = score + 40
        number = number + 1
    elif number == 3 and message.content.startswith('$B'):
        score = score + 30
        number = number + 1
    elif number == 3 and message.content.startswith('$C'):
        score = score + 20
        number = number + 1
    elif number == 3 and message.content.startswith('$D'):
        score = score + 10
        number = number + 1
    elif number == 4:
        await message.channel.send("Çamaşır makinenizin enerji etiketine göre verimliliği kaçtır? A)A+++ veya A++ B)A+ veya A C)B veya C D)D veya daha az")
        number = number + 1
    elif number == 5 and message.content.startswith('$A'):
        score = score + 40
        number = number + 1
    elif number == 5 and message.content.startswith('$B'):
        score = score + 30
        number = number + 1
    elif number == 5 and message.content.startswith('$C'):
        score = score + 20
        number = number + 1
    elif number == 5 and message.content.startswith('$D'):
        score = score + 10
        number = number + 1
    elif number == 6:
        await message.channel.send("Kaç tane klimanız veya kalorifer peteğiniz var? A)1 B)2 C)3 D)4 veya daha fazla")
        number = number + 1
    elif number == 7 and message.content.startswith('$A'):
        score = score + 40
        number = number + 1
    elif number == 7 and message.content.startswith('$B'):
        score = score + 30
        number = number + 1
    elif number == 7 and message.content.startswith('$C'):
        score = score + 20
        number = number + 1
    elif number == 7 and message.content.startswith('$D'):
        score = score + 10
        number = number + 1
    elif number == 8:
        await message.channel.send("Evinizin nerelerinde izolasyon var? A)Her yerinde B)Çoğu odalarda C)Bazı odalarda D)İzolasyon yok")
        number = number + 1
    elif number == 9 and message.content.startswith('$A'):
        score = score + 40
        number = number + 1
    elif number == 9 and message.content.startswith('$B'):
        score = score + 30
        number = number + 1
    elif number == 9 and message.content.startswith('$C'):
        score = score + 20
        number = number + 1
    elif number == 9 and message.content.startswith('$D'):
        score = score + 10
        number = number + 1
    elif number < 10:
        await message.channel.send("Lütfen doğru seçeneği seçiniz")
    elif score > 190:
        await message.channel.send("Tebrikler, bütün soruları cevapladınız!")
        await message.channel.send("Skorunuz:")
        await message.channel.send(score)
        message.channel.send("Bu durumda verebileceğimiz bir öneri yok.")
    elif score > 150:
        await message.channel.send("Tebrikler, bütün soruları cevapladınız!")
        await message.channel.send("Skorunuz:")
        await message.channel.send(score)
        await message.channel.send("Gördüğümüz kadarıyla iklime önem veriyorsunuz. Biz size kullandığınız ampül sayısını biraz azaltmanızı, diyetinizi biraz değiştirmenizi, çamaşır makinenizi biraz daha verimli bir tanesi ile değiştirmenizi, klima veya kalorifer sayınızı biraz azaltmanız veya evinizin izolasyonu olmayan yerlerini izole etmenizi öneriyoruz.")
    elif score > 110:
        await message.channel.send("Tebrikler, bütün soruları cevapladınız!")
        await message.channel.send("Skorunuz:")
        await message.channel.send(score)
        await message.channel.send("Gördüğümüz kadarıyla iklime önem veriyorsunuz. Biz size kullandığınız ampül sayısını azaltmanızı, diyetinizi değiştirmenizi, çamaşır makinenizi daha verimli bir tanesi ile değiştirmenizi, klima veya kalorifer sayınızı azaltmanız veya evinizin izolasyonu olmayan yerlerini izole etmenizi öneriyoruz.")
    elif score > 70:
        await message.channel.send("Tebrikler, bütün soruları cevapladınız!")
        await message.channel.send("Skorunuz:")
        await message.channel.send(score)
        await message.channel.send("Gördüğümüz kadarıyla iklime önem veriyorsunuz. Biz size kullandığınız ampül sayısını biraz fazla azaltmanızı, diyetinizi biraz fazla değiştirmenizi, çamaşır makinenizi çok daha verimli bir tanesi ile değiştirmenizi, klima veya kalorifer sayınızı çok azaltmanız veya evinizin izolasyonu olmayan yerlerini izole etmenizi öneriyoruz.")
    else:
        await message.channel.send("Tebrikler, bütün soruları cevapladınız!")
        await message.channel.send("Skorunuz:")
        await message.channel.send(score)
        await message.channel.send("Biz size kullandığınız ampül sayısını bayağı azaltmanızı, diyetinizi bayağı değiştirmenizi, çamaşır makinenizi çok daha verimli bir tanesi ile değiştirmenizi, klima veya kalorifer sayınızı bayağı azaltmanız, evinizin izolasyonu olmayan yerlerini izole etmeniz veya ağaç dikmenizi öneriyoruz.")

client.run("you bot token here")
