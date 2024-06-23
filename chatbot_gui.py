import tkinter as tk
from tkinter import scrolledtext
from chatbot_logic import Chatbot

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        self.chatbot = Chatbot()

        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, state='disabled', wrap=tk.WORD)
        self.chat_display.pack(padx=10, pady=10)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(padx=10, pady=10)

        self.user_input = tk.Entry(self.entry_frame, width=50)
        self.user_input.pack(side=tk.LEFT, padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=10)

    def send_message(self, event=None):
        message = self.user_input.get()
        if message.strip():
            self.display_message("User", message)
            self.user_input.delete(0, tk.END)
            self.display_loading_animation()
            # Delay for 2-3 seconds before showing the response
            self.root.after(2000, self.show_response, message)

    def display_loading_animation(self):
        self.display_message("Bot", "...")

    def show_response(self, message):
        response = self.chatbot.get_response(message)
        # Remove the loading message before displaying the actual response
        self.remove_loading_animation()
        self.display_message("Bot", response)

    def remove_loading_animation(self):
        self.chat_display.config(state='normal')
        content = self.chat_display.get("1.0", tk.END)
        content = content.replace("Bot: ...\n", "")
        self.chat_display.delete("1.0", tk.END)
        self.chat_display.insert(tk.END, content)
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def display_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
