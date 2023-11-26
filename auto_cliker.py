import tkinter as tk
import threading
import time
from pynput import keyboard
import pyautogui

class AutoClicker:
    def __init__(self, interval=5, hotkey_start="o", hotkey_stop="p"):
        self.interval = interval
        self.running = False
        self.hotkey_start = hotkey_start.lower()
        self.hotkey_stop = hotkey_stop.lower()

    def start_clicking(self):
        self.running = True
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

    def stop_clicking(self):
        self.running = False

def start_auto_clicker():
    auto_clicker_thread = threading.Thread(target=auto_clicker.start_clicking)
    auto_clicker_thread.start()
    status_var.set("Running")

def stop_auto_clicker():
    auto_clicker.stop_clicking()
    status_var.set("Stopped")

def on_key_release(key):
    if key.char == auto_clicker.hotkey_start:
        start_auto_clicker()
    elif key.char == auto_clicker.hotkey_stop:
        stop_auto_clicker()

# Создаем графический интерфейс с двумя кнопками - "Start" и "Stop"
root = tk.Tk()
root.title("AutoClicker")

auto_clicker = AutoClicker()

start_button = tk.Button(root, text=f"Start AutoClicker (Hotkey: {auto_clicker.hotkey_start.upper()})", command=start_auto_clicker)
start_button.pack()

stop_button = tk.Button(root, text=f"Stop AutoClicker (Hotkey: {auto_clicker.hotkey_stop.upper()})", command=stop_auto_clicker)
stop_button.pack()

# Добавляем обработчик клавиш с использованием библиотеки pynput
with keyboard.Listener(on_release=on_key_release) as listener:
    # Добавляем метку для отображения состояния автокликера
    status_var = tk.StringVar()
    status_var.set("Stopped")
    status_label = tk.Label(root, textvariable=status_var)
    status_label.pack()

    root.mainloop()

    # Останавливаем прослушивание клавиш после закрытия окна
    listener.stop()
    listener.join()
