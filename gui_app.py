import tkinter as tk
from tkinter import messagebox
import threading
from multi_lang_bot import multi_lang_bot

def run_bot_thread():
    status_label.config(text="🤖 Running... Say 'बंद' or 'bye' to exit.")
    start_button.config(state=tk.DISABLED)
    threading.Thread(target=multi_lang_bot).start()

# GUI window setup
root = tk.Tk()
root.title("Hindi Voice Agent")
root.geometry("400x200")
root.resizable(False, False)

title_label = tk.Label(root, text="Hindi Multilingual Voice Agent", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

status_label = tk.Label(root, text="Click 'Start Agent' to begin", font=("Helvetica", 12))
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Agent", font=("Helvetica", 12), bg="green", fg="white", command=run_bot_thread)
start_button.pack(pady=20)

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), bg="red", fg="white", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()

