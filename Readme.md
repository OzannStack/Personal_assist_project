# 🧠 Personal Assistant - Python GUI

A simple personal assistant built with Python's `tkinter` GUI library. It helps you manage personal notes and check live weather using the [WeatherAPI](https://www.weatherapi.com/).

## ✨ Features

- 📝 Add, view, modify, and delete personal notes
- 🌤️ Display current weather by city (customizable)
- 🗂️ JSON-based local data storage
- 🪄 Simple, clean user interface

---

## 🛠️ Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)

Install dependencies:
```bash
pip install requests, datetime, pytz, json, webbrowser
from utils.voice import speak
import tkinter as tk
from tkinter import messagebox
```
## 📁 Project Structure
```bash
Personal_AI_Assistant/
├── main.py                # Entry point
├── Assistent/
│   ├── core.py            # Weather & Notes logic
├── data/
│   ├── notes.json         # Notes storage
│   └── config.json        # Configuration (API key & City)
├── README.md
```
## ⚙️ Configuration
```bash
{
  "Api_key": "YOUR_API_KEY",
  "City": "Beijing"
}
```
## 🚀 How to Run
```bash
python main.py
```
## 💡 To Do
- Add voice assistant integration

- Add support for time-based reminders

- Support more cities/weather features

## 🙋‍♂️ Author
Created with ❤️ by OzannStack

```bash
---

Jika kamu ingin saya bantu menyesuaikan bagian tertentu seperti penjelasan kode `main.py` atau `core.py`, atau menambahkan badge CI atau screenshot, cukup beri tahu ya.
```



