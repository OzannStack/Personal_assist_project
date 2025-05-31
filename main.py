import tkinter as tk
from Assistent.core import greet_user, open_app, open_browser, show_data, weather_api, change_location
from utils.voice import speak

def handle_notes():
    speak("Membuka catatan")
    show_data()

def handle_open_app():
    speak("Membuka aplikasi")
    open_app()

def handle_open_browser():
    speak("Membuka browser")
    open_browser()

def main():
    window = tk.Tk()
    window.title("Personal AI Assistant")
    window.geometry("500x400")
    window.config(bg="#f0f0f0")
    
    # Greeting
    greeting = greet_user()
    speak(greeting)

    label = tk.Label(window, text=greeting + "\nApa yang kamu inginkan tuan?", font=("Arial", 12), bg="#f0f0f0")
    label.pack(pady=20)

    #Weather
    label1 = tk.Label(window, text=weather_api(), font=("Arial", 12), bg="#f0f0f0")
    label1.pack(pady=10)

    # Buttons
    btn_notes = tk.Button(window, text="📒 Notes", width=20, command=handle_notes)
    btn_notes.pack(pady=5)

    btn_notes = tk.Button(window, text="📒 Notes", width=20, command=change_location)
    btn_notes.pack(pady=5)

    btn_open_app = tk.Button(window, text="🖥️ Open App", width=20, command=handle_open_app)
    btn_open_app.pack(pady=5)

    btn_browser = tk.Button(window, text="🌐 Open Browser", width=20, command=handle_open_browser)
    btn_browser.pack(pady=5)

    btn_exit = tk.Button(window, text="❌ Exit", width=20, command=window.quit)
    btn_exit.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    main()
