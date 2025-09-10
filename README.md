# 🚀 Telegram Bot com Pyrogram

Este projeto é um bot do Telegram que libera o acesso somente para usuários que entrarem em canais/grupos específicos.  
Feito em **Python + Pyrogram** e pronto para rodar no **Railway**.

---

## 📦 Arquivos incluídos
- `bot.py` → Código principal do bot
- `requirements.txt` → Dependências necessárias
- `Procfile` → Arquivo para iniciar o bot automaticamente no Railway

---

## 🔧 Configuração

### 1. Criar API do Telegram
1. Acesse [https://my.telegram.org](https://my.telegram.org)
2. Vá em **API development tools**
3. Crie uma aplicação
4. Pegue o **API_ID** e o **API_HASH**

### 2. Criar bot no BotFather
1. Abra o Telegram e fale com [@BotFather](https://t.me/BotFather)
2. Use o comando `/newbot`
3. Copie o **BOT_TOKEN**

### 3. Configurar variáveis no Railway
No painel do seu projeto no Railway → **Settings → Variables**, adicione:

- `API_ID` → seu api_id (ex: 123456)
- `API_HASH` → seu api_hash (ex: abcd1234efgh5678)
- `BOT_TOKEN` → token do BotFather (ex: 123456:ABC-xyz...)

---

## 🚀 Deploy no Railway

1. Suba esses arquivos no GitHub (`bot.py`, `requirements.txt`, `Procfile`, `README.md`)
2. No Railway, clique em **New Project → Deploy from GitHub repo**
3. Selecione o repositório com o bot
4. Railway vai instalar as dependências e iniciar o bot automaticamente 🎉

---

## ▶️ Rodar localmente (opcional)

Se quiser rodar no PC/Termux:

```bash
pip install -r requirements.txt
python bot.py
```

---

## ✅ Funcionalidades
- Verificação de inscrição em canal/links obrigatórios
- Botão "Verificar" automático
- Bloqueio de acesso para não inscritos
