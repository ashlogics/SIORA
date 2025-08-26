# 🤖 SIORA – Smart Intelligent Operational Reactive Assistant

Your futuristic, voice-activated Python AI — capable of controlling your apps, fetching real-time info, and making life hands-free.

> “Hey SIORA, open YouTube” – and it's done.

---

## 🌟 Features

- 🔊 Voice command interface
- 🌐 Open websites like **Google**, **YouTube**, and more
- 🔍 Search queries directly on Google or YouTube
- 🌦️ Get real-time weather updates
- 🧠 Launch applications like **VS Code** and **PyCharm**
- 🎵 Music playback from a local folder
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

4. **Rename the example env file to .env to configure your variables:**
```bash
mv .env.example .env   # On Windows PowerShell: rename-item .env.example .env
```

5. **Editing the .env:**
- On Linux/Mac:

  - Using `nano`:
  
    ```bash
    nano .env
    ```
    
    - Edit the variables as needed.
    - Press `Ctrl + O` to save, then `Enter` to confirm.
    - Press `Ctrl + X` to exit.

- On Windows (PowerShell):

  - Using `notepad`:
  
    ```powershell
    notepad .env
    ```
    
    This opens `.env` in Notepad. Edit and save as usual.

---

## ⚙️ Environment Variables Setup

To customize SIORA, create a `.env` file in the project root with the following variables, **ENTER YOUR OWN VALUES**:

```env
VSCODE_PATH="C:\\\\Users\\\\YourName\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\Code.exe"
PYCHARM_PATH="C:\\\\Program Files\\\\JetBrains\\\\PyCharm Community Edition 2023.1\\\\bin\\\\pycharm64.exe"
WEATHER_API="your_openweather_api_key"
CITY="New York"
MUSIC_DIR_PATH="C:\\\\Users\\\\YourName\\\\Music"
```

> ✅ Make sure all paths use **double backslashes** (`\\\\`) on Windows or `/` on Unix-based systems.

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
- `"Siora Play music"`

---

## 🧠 Powered By

- `speech_recognition`
- `pyttsx3`
- `requests`
- `webbrowser`
- `dotenv`
- `os`

---

## 🧪 Example Commands

| 🎙️ Command | 🧠 What SIORA Does |
|------------|---------------------|
| Open YouTube | Launches youtube.com in your browser |
| Search in google about AI | Opens Google with search results for "AI" |
| What’s the weather? | Tells the weather in your set `CITY` |
| Open VS Code | Opens the editor at your `VSCODE_PATH` |
| Play music | Plays music from your `MUSIC_DIR_PATH` |

---

## 🧑‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

> 👨‍💻 Created with ❤️ by [Ashmit](https://github.com/ashlogics).
