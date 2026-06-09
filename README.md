# 🎙️ Nasama 1.0 — Assistente Virtual

Assistente virtual desenvolvida em Python com reconhecimento e síntese de voz,
capaz de executar tarefas por comando de voz.

> O nome **Nasama** é uma homenagem aos meus 3 pets: **Na**ni, **Sa**ndy e **Ma**ya. 🐾

> Projeto desenvolvido durante o curso **OneBitCode Python**, com funcionalidades extras adicionadas como envio de e-mails por voz, agenda de contatos, interface gráfica, busca de notícias em 5 sites diferentes e temperatura por cidade.

---

## 📸 Interface

| Dark | Light |
|---|---|
| ![dark](screenshots/dark.png) | ![light](screenshots/light.png) |

---

## 🚀 Funcionalidades
- ⏰ Informa a hora atual por voz
- 📧 Envia e-mails por comando de voz
- 🔊 Responde em português com síntese de voz
- 🖥️ Interface gráfica com tema dark/light
- 🎵 Animação no círculo ao falar
- 💬 Histórico de conversa na tela
- 📰 Notícias de 5 fontes RSS (Google News, G1, BBC, UOL, Folha)
- 💰 Cotação de moedas (Dólar, Euro, Bitcoin)
- 🌡️ Temperatura atual por cidade
- 💻 Desliga e cancela desligamento do computador por voz

---

## 🛠️ Tecnologias utilizadas
| Tecnologia | Finalidade |
|---|---|
| gTTS | Síntese de voz (Text-to-Speech) |
| SpeechRecognition | Reconhecimento de voz |
| Google Speech API | Transcrição de áudio em português |
| smtplib / ssl | Envio de e-mails |
| customtkinter | Interface gráfica moderna |
| pygame | Reprodução de áudio |
| Pillow | Manipulação de imagens |
| requests | Consumo de APIs externas |
| BeautifulSoup4 | Leitura de feeds RSS |
| lxml | Parser XML para RSS |
| OpenWeatherMap API | Temperatura e clima por cidade |
| python-dotenv | Variáveis de ambiente |

---

## 📁 Estrutura do Projeto
```
nasama/
│
├── files/
│   ├── senha            # não incluso — senha de app do Gmail
│   └── contatos.json    # não incluso — agenda de contatos
│
├── screenshots/
│   ├── dark.png         # interface tema dark
│   └── light.png        # interface tema light
│
├── .env.example
├── funcoes_email.py     # funções de envio de e-mail por voz
├── funcoes_so.py        # funções do sistema operacional
├── funcoes_noticias.py  # notícias de 5 fontes RSS
├── funcoes_cotacao.py   # cotação de moedas
├── funcoes_clima.py     # temperatura por cidade
├── interface.py         # interface gráfica
├── nasama.py            # arquivo principal
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/ThiagoRamos16/Nasama-1.0.git
cd Nasama-1.0
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
> Bibliotecas instaladas: `gTTS`, `pygame`, `SpeechRecognition`, `customtkinter`, `Pillow`, `requests`, `beautifulsoup4`, `lxml`, `python-dotenv`

### 3. Senha do Gmail
Crie o arquivo `files/senha` com sua senha de aplicativo do Gmail.

Para gerar uma senha de aplicativo:

1. Ative a verificação em duas etapas na sua conta Google.
2. Acesse a página de gerenciamento de senhas de aplicativo:
   https://myaccount.google.com/apppasswords
3. Gere uma nova senha de aplicativo.
4. Copie a senha gerada.
5. Salve a senha no arquivo `files/senha`.

### 4. Agenda de contatos
Crie o arquivo `files/contatos.json` com seus contatos:
```json
{
    "exemplo": "exemplo@gmail.com",
    "exemplo2": "exemplo2@gmail.com"
}
```

### 5. Chave da API de Clima
1. Crie uma conta gratuita em [openweathermap.org](https://openweathermap.org) e
2. Gere uma chave de API
3. Crie um arquivo `.env` na raiz do projeto utilizando o `.env.example` como modelo
4. Adicione sua chave ao arquivo `.env`.

Exemplo:

```env
OPENWEATHER_API_KEY=sua_chave_aqui
```

## 6. Execute o Projeto

⚠️ Recomendado: Python 3.12

Versões mais recentes podem apresentar incompatibilidades com algumas dependências relacionadas ao reconhecimento de voz.

Windows
py -3.12 nasama.py
Linux / MacOS
python nasama.py

```bash
# Windows com múltiplas versões Python
py -3.12 nasama.py

# Outros sistemas
python nasama.py
```

---

## 🗣️ Comandos disponíveis
| Comando | Ação |
|---|---|
| *"horas"* | Informa a hora atual |
| *"enviar e-mail"* | Inicia o fluxo de envio de e-mail por voz |
| *"notícias"* | Pergunta a fonte e lê as 3 últimas notícias |
| *"cotação do dólar"* | Informa a cotação do Dólar |
| *"cotação do euro"* | Informa a cotação do Euro |
| *"cotação do bitcoin"* | Informa a cotação do Bitcoin |
| *"clima"* ou *"temperatura"* | Pergunta a cidade e informa o clima atual |
| *"desligar computador em uma hora"* | Agenda desligamento em 1 hora |
| *"desligar computador em meia hora"* | Agenda desligamento em 30 minutos |
| *"cancelar desligamento"* | Cancela o desligamento agendado |
| *"fechar assistente"* | Encerra a Nasama |

---

## ⚠️ Segurança
Os arquivos abaixo não são enviados para o repositório:

files/senha
files/contatos.json
.env

Utilize sempre uma senha de aplicativo do Gmail e nunca sua senha principal.

---

## 👨‍💻 Autor
**Thiago Ramos da Silva**
[linkedin.com/in/thiagoramosdasilva](https://www.linkedin.com/in/thiagoramosdasilva)
