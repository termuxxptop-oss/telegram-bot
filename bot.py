from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Credenciais do bot
API_ID = 25502322
API_HASH = "87354a210a27b605973e1eeeb5bfabb5"
BOT_TOKEN = "7874346896:AAGhm-Uw4Sk7Bv79fb5bCVQn2a1DYqZ8XBc"

# Links obrigatórios
LINKS = {
    "🍏 WhatsApp": "https://whatsapp.com/channel/0029VbArk5aBVJl7HTKxKw0j",
    "🍎 YouTube": "https://youtube.com/@termuxxp5913?si=DOcHXfz3bL63hLyX",
    "🌊 Telegram Group": "https://t.me/termuxtop2",
    "🍇 Telegram Channel": "https://t.me/bacbovipf"
}

# Canal obrigatório para verificação
REQUIRED_CHANNEL = "@bacbovipf"

# Inicialização do bot
app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    try:
        member = await app.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await message.reply("✅ Acesso liberado! Bem-vindo ao bot 🔥")
        else:
            raise Exception("Não inscrito")
    except:
        buttons = [[InlineKeyboardButton(nome, url=link)] for nome, link in LINKS.items()]
        buttons.append([InlineKeyboardButton("⚠️ Verificar", callback_data="verify")])
        keyboard = InlineKeyboardMarkup(buttons)
        await message.reply(
            "❌ Access Denied!\n\nVocê precisa entrar em **todos os links abaixo** e depois clicar em **Verificar**:",
            reply_markup=keyboard
        )

@app.on_callback_query(filters.regex("verify"))
async def verify(client, callback_query):
    user_id = callback_query.from_user.id
    try:
        member = await app.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await callback_query.message.edit_text("✅ Agora sim, acesso liberado!")
        else:
            await callback_query.answer("❌ Você ainda não entrou em todos os canais!", show_alert=True)
    except:
        await callback_query.answer("⚠️ Erro ao verificar! Tente novamente.", show_alert=True)

app.run()
