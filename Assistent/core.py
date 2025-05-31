from datetime import datetime
import pytz
import json
import os
import webbrowser
from utils.voice import speak
import tkinter as tk
from tkinter import messagebox
import requests

#Pilihan

def open_app():
    print(f"1. Notepad\n2. File Explorer")
    choice = int(input("Masukkan Pilihan"))
    if choice == 1 :
        data = "notepad"
    else :
        data = "file explorer"
    os_app(data)
#Os open app
def os_app(app) :
    os.system(F"Start {app}")
#Sapa User
def greet_user():
    lokal = datetime.now().hour #Local Time
    TimeZone = pytz.timezone('Asia/Jakarta') # Untuk jakarta
    hour = datetime.now(TimeZone).hour
    
    #Memulai Gate sapa
    if hour < 12 and hour > 6:
        greeting = "Selamat Pagi"
    elif hour < 14 and hour > 11:
        greeting = "Selamat Sore"
    elif hour < 18 and hour > 13:
        greeting = "Selamat Sore"
    else:
        greeting = "Selamat Malam"
    print(greeting)
    return greeting
def weather_api(filepath = 'data/config.json'):
    try:
        with open('data/config.json', 'r') as file:
            config = json.load(file)  # bukan `data`, biar jelas ini config
    except FileNotFoundError:
        config = {}

    # Ambil API Key dan Kota dari config.json
    Api_key = config.get("Api_key", "")
    url = f"http://api.weatherapi.com/v1/current.json?key={Api_key}&q=beijing&aqi=no"
    response = requests.get(url)
    data1 = response.json()

    # Pastikan 'current' ada dalam response
    teks = f"beijing : \n {data1['current']['temp_c']} °C"
    return teks

#Menyimpan Data
def save_data(filepath = 'data/notes.json'): 
    save_win = tk.Toplevel()
    save_win.geometry("400x300")
    save_win.title("Tambah Catatan")
    #Membaca Data Json
    try :
        with open(filepath, 'r') as file :
            data = json.load(file)
    except FileNotFoundError:
        data = []
    #Memulai menambahkan Data
    Label2 = tk.Label(save_win, text='Catatan Baru',font=("Arial",12),bg="#f0f0f0")
    Label2.pack(pady=20)
    catatan_baru = tk.StringVar()
    entry = tk.Entry(save_win,textvariable = catatan_baru, font=('calibre',10,'normal'))
    entry.pack(pady=5)
    
    #Tombol Simpan
    def simpan_data():
        catatan_new = catatan_baru.get()
        if catatan_new:
            data.append({"tanggal" : datetime.now().strftime("%d-%m-%Y"), "catatan" : catatan_new})
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=2)
            save_win.destroy()  # tutup jendela setelah simpan
        refresh_note()

    tk.Button(save_win, text="Simpan", command=simpan_data).pack(pady=20)
def refresh_note(notes_frame):
    for widget in notes_frame.winfo_children():
        widget.destroy()
    try:
        with open('data/notes.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        tk.Label(notes_frame, text="Belum ada catatan.").pack()
        return
    for i, note in enumerate(data, start=1):
        teks = f"{i}. {note['catatan']} Date : {note['tanggal']}"
        tk.Label(notes_frame, text=teks, anchor='w', justify='left').pack(fill='x')

def save_data(refresh_note, notes_frame, filepath='data/notes.json'):
    save_win = tk.Toplevel()
    save_win.geometry("400x300")
    save_win.title("Tambah Catatan")

    # Baca data
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Form input
    tk.Label(save_win, text='Catatan Baru', font=("Arial", 12)).pack(pady=10)
    catatan_baru = tk.StringVar()
    entry = tk.Entry(save_win, textvariable=catatan_baru, font=('calibre', 10, 'normal'))
    entry.pack(pady=10)

    def simpan_data():
        catatan_new = catatan_baru.get()
        if catatan_new:
            data.append({
                "tanggal": datetime.now().strftime("%d-%m-%Y"),
                "catatan": catatan_new
            })
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=2)
            save_win.destroy()
            refresh_note(notes_frame)  # Refresh frame utama

    tk.Button(save_win, text="Simpan", command=simpan_data).pack(pady=20)

def show_data(filepath='data/notes.json'):
    win = tk.Toplevel()
    win.title("Daftar Catatan")
    win.geometry("700x600")

    label1 = tk.Label(win, text="\nApa yang kamu inginkan tuan?", font=("Arial", 12), bg="#f0f0f0")
    label1.pack(pady=10)

    # Frame untuk daftar catatan
    notes_frame = tk.Frame(win)
    notes_frame.pack(padx=20, pady=20)

    # Tampilkan catatan
    refresh_note(notes_frame)

    # Tombol
    tk.Button(win, text="🖥️ Add Data", width=20, command=lambda: save_data(refresh_note, notes_frame)).pack(pady=5)
    tk.Button(win, text="📒 Modify Data", width=20, command=lambda: show_modify_popup(refresh_note, notes_frame)).pack(pady=5)
    tk.Button(win, text="🌐 Delete Data", width=20, command=lambda: show_delete_popup(refresh_note,notes_frame)).pack(pady=5)
    tk.Button(win, text="❌ Exit", width=20, command=win.destroy).pack(pady=20)

    win.mainloop()
#Menghapus Data
def show_delete_popup(refresh_note, notes_frame, filepath='data/notes.json'):
    delete_win = tk.Toplevel()
    delete_win.geometry("300x150")
    delete_win.title("Hapus Catatan")

    tk.Label(delete_win, text="Nomor catatan yang ingin dihapus:").pack(pady=10)
    nomor = tk.StringVar()
    tk.Entry(delete_win, textvariable=nomor).pack()

    def hapus():
        try:
            number = int(nomor.get())
            with open(filepath, 'r') as file:
                data = json.load(file)
            if 1 <= number <= len(data):
                deleted = data.pop(number - 1)
                with open(filepath, 'w') as file:
                    json.dump(data, file, indent=2)
                tk.messagebox.showinfo("Sukses", f"'{deleted['catatan']}' telah dihapus.")
                delete_win.destroy()
                refresh_note(notes_frame)
            else:
                tk.messagebox.showerror("Error", "Nomor tidak valid.")
        except:
            tk.messagebox.showerror("Error", "Masukkan angka yang valid.")

    tk.Button(delete_win, text="Hapus", command=hapus).pack(pady=10)
#Modifikasi Data
def show_modify_popup(refresh_note, notes_frame, filepath='data/notes.json'):
    modify_win = tk.Toplevel()
    modify_win.geometry("400x300")
    modify_win.title("Modifikasi Catatan")

    tk.Label(modify_win, text="Masukkan nomor catatan yang ingin diubah:").pack(pady=10)
    nomor = tk.StringVar()
    tk.Entry(modify_win, textvariable=nomor).pack()

    edit_field = tk.Text(modify_win, height=5, width=40)
    edit_field.pack(pady=10)

    def tampilkan_catatan():
        try:
            index = int(nomor.get()) - 1
            with open(filepath, 'r') as file:
                data = json.load(file)
            if 0 <= index < len(data):
                edit_field.delete('1.0', tk.END)
                edit_field.insert(tk.END, data[index]['catatan'])
            else:
                messagebox.showerror("Error", "Nomor tidak valid.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    def simpan_perubahan():
        try:
            index = int(nomor.get()) - 1
            new_text = edit_field.get('1.0', tk.END).strip()
            with open(filepath, 'r') as file:
                data = json.load(file)
            if 0 <= index < len(data):
                data[index]['catatan'] = new_text
                with open(filepath, 'w') as file:
                    json.dump(data, file, indent=2)
                messagebox.showinfo("Berhasil", "Catatan berhasil diperbarui.")
                modify_win.destroy()
                refresh_note(notes_frame)
            else:
                messagebox.showerror("Error", "Nomor tidak valid.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan: {e}")

    tk.Button(modify_win, text="Tampilkan", command=tampilkan_catatan).pack(pady=5)
    tk.Button(modify_win, text="Simpan Perubahan", command=simpan_perubahan).pack(pady=5)
def open_browser() :
    text = input("Masukkan Url : ")
    webbrowser.open(text)
    hasil = text[4:-3]
    print(f"Membuka url {text}")
    speak(f"Membuka {hasil}")