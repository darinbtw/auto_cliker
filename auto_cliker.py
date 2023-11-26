import tkinter as tk
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener as KeyboardListener, KeyCode
import threading
import time

class AutoClicker:
    def __init__(self, interval=0.20, hotkey_start="9", hotkey_stop="0"):
        self.interval = interval
        self.running = False
        self.hotkey_start = KeyCode.from_char(hotkey_start)
        self.hotkey_stop = KeyCode.from_char(hotkey_stop)
        self.mouse = MouseController()
        self.auto_clicker_thread = None  # добавлено поле для потока

    def start_clicking(self):
        self.running = True
        while self.running:
            self.mouse.click(Button.left)
            time.sleep(self.interval)

    def stop_clicking(self):
        self.running = False

def start_auto_clicker():
    auto_clicker.auto_clicker_thread = threading.Thread(target=auto_clicker.start_clicking)
    auto_clicker.auto_clicker_thread.start()
    status_var.set("Running")

def stop_auto_clicker():
    auto_clicker.stop_clicking()
    if auto_clicker.auto_clicker_thread is not None:
        auto_clicker.auto_clicker_thread.join()  # Ждем завершения потока перед обновлением статуса
    status_var.set("Stopped")

def on_key_release(key):
    if key == auto_clicker.hotkey_start:
        start_auto_clicker()
    elif key == auto_clicker.hotkey_stop:
        stop_auto_clicker()

# Создаем графический интерфейс
root = tk.Tk()
root.title("AutoClicker")

auto_clicker = AutoClicker()

start_button = tk.Button(root, text=f"Start AutoClicker (Hotkey: {auto_clicker.hotkey_start})", command=start_auto_clicker)
start_button.pack()

stop_button = tk.Button(root, text=f"Stop AutoClicker (Hotkey: {auto_clicker.hotkey_stop})", command=stop_auto_clicker)
stop_button.pack()

# Добавляем обработчик отпускания клавиш с использованием библиотеки pynput
with KeyboardListener(on_release=on_key_release):
    # Добавляем метку для отображения состояния автокликера
    status_var = tk.StringVar()
    status_var.set("Stopped")
    status_label = tk.Label(root, textvariable=status_var)
    status_label.pack()

    root.mainloop()
