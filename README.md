# 🤖 SIORA – Smart Intelligent Operational Reactive Assistant

Your futuristic, voice-activated Python AI — capable of controlling your apps, fetching real-time info, chatting like a human, and making life hands-free.

> “Hey SIORA, what’s the capital of Brazil?” – it answers instantly.

---

## 🌟 Features

- 🔊 Voice command interface
- 🌐 Open websites like **Google**, **YouTube**, and more
- 🔍 Search queries directly on Google or YouTube
- 🌦️ Get real-time weather updates
- 🧠 Launch applications like **VS Code** and **PyCharm**
- 🎵 Music playback from a local folder
- 💬 **Chat with AI** using natural language (powered by **Cohere**)
- 🛠️ Fully customizable with environment variables

---

## 🛠️ Installation

> 💡 This project uses Python 3.8+ and works on Windows, Mac, or Linux.

1. **Clone the repo:**

```bash
git clone https://github.com/ashlogics/SIORA.git
cd SIORA
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Rename the example env file to `.env` to configure your variables:**

```bash
mv .env.example .env   # On Windows PowerShell: rename-item .env.example .env
```

5. **Edit the `.env` file:**

```env
VSCODE_PATH=C:\\\\Users\\\\YourName\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\Code.exe
PYCHARM_PATH=C:\\\\Program Files\\\\JetBrains\\\\PyCharm Community Edition 2023.1\\\\bin\\\\pycharm64.exe
WEATHER_API=your_openweather_api_key
CITY=California
MUSIC_DIR_PATH=C:\\\\Users\\\\YourName\\\\Music
COHERE_API_KEY=your_cohere_api_key
```

---

## 🚀 How to Run

```bash
python siora.py
```

SIORA will start listening for your commands. Try saying:

- `"Open YouTube"`
- `"Search in Google about Python tutorials"`
- `"What’s the weather today?"`
- `"Open VS Code"`
- `"Siora play music"`
- `"Siora, what is quantum computing?"`

---

## 💬 Chatbot Integration

SIORA includes a built-in AI chatbot powered by **Cohere’s large language model**. You can ask general knowledge questions, have conversations, or get assistance in a natural, human-like way.

> Just speak as you would to a smart assistant. If the query doesn't match any command, SIORA intelligently responds using Cohere's NLP engine.

---

## 🧠 Powered By

- `speech_recognition`
- `pyttsx3`
- `requests`
- `wikipedia`
- `webbrowser`
- `dotenv`
- `cohere` 🧠

> Special thanks to [Cohere](https://cohere.com) for powering the AI chatbot experience!

---

## 🧪 Example Commands

| 🎙️ Command                      | 🧠 What SIORA Does                               |
|-------------------------------|--------------------------------------------------|
| Open YouTube                  | Launches youtube.com in your browser             |
| Search in Google about AI     | Opens Google with search results for "AI"        |
| What’s the weather?           | Tells the weather in your set `CITY`             |
| Open VS Code                  | Opens the editor at your `VSCODE_PATH`           |
| Play music                    | Plays music from your `MUSIC_DIR_PATH`           |
| What is the capital of Japan? | Responds using Cohere’s natural language model   |

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🧑‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

> 👨‍💻 Created with ❤️ by [Ashmit](https://github.com/ashlogics).

