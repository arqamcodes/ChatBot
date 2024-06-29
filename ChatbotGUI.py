import tkinter as tk
from tkinter import scrolledtext
from chatbotLogic import Chatbot
import tkinter.font as tkFont
import threading
import time

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DUET Chatbot")
        self.root.geometry("700x700")
        self.root.configure(bg="#2E2E2E")

        self.font = tkFont.Font(family="Poppins", size=10)
        self.bold_font = tkFont.Font(family="Poppins", size=10, weight="bold")
        self.title_font = tkFont.Font(family="Poppins", size=14, weight="bold")

        self.chatbot = Chatbot(api_key="YOUR_API_KEY")

        self.chat_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame, state='disabled', wrap=tk.WORD, 
            bg="#3A3A3A", fg="white", font=self.font, 
            borderwidth=0, highlightthickness=0
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.entry_frame.pack(padx=10, pady=10, fill=tk.X)

        self.user_input = tk.Entry(
            self.entry_frame, width=50, 
            bg="#4A4A4A", fg="white", font=self.font, 
            insertbackground="white", borderwidth=1, relief=tk.FLAT, 
            highlightthickness=1, highlightcolor="#4CAF50", 
            highlightbackground="#4A4A4A"
        )
        self.user_input.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            self.entry_frame, text="Send", command=self.send_message, 
            bg="#4CAF50", fg="white", font=self.bold_font, 
            borderwidth=0, highlightthickness=0, padx=10, pady=5
        )
        self.send_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.load_faqs()

    def load_faqs(self):
        faqs = [
            "What is the admission test?",
            "Why is the admission test important?",
            "Who can take the admission test?",
            "When is the admission test?",
            "What are the important deadlines?",
            "How do I register for the admission test?",
            "What documents are required for registration?",
            "What is the format of the admission test?",
            "What subjects are covered in the admission test?",
            "How should I prepare for the admission test?",
            "Are there any recommended study materials?",
            "What should I bring on the test day?",
            "What time should I arrive at the test center?",
            "How will I receive my test results?",
            "What should I do after receiving my test results?",
        ]

        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "FAQs:\n", "title")
        for question in faqs:
            faq_button = tk.Button(
                self.chat_display, text=question, wraplength=500, 
                command=lambda q=question: self.display_answer(q),
                bg="#3A3A3A", fg="white", font=self.bold_font, 
                activebackground="#5A5A5A", activeforeground="white", 
                borderwidth=0, highlightthickness=0
            )
            self.chat_display.window_create(tk.END, window=faq_button)
            self.chat_display.insert(tk.END, "\n")
        self.chat_display.insert(tk.END, "\n")
        self.chat_display.tag_configure("title", font=self.title_font, foreground="white")
        self.chat_display.config(state='disabled')

    def display_answer(self, question):
        answer = self.chatbot.get_response(question)
        self.display_message("Bot", answer)

    def send_message(self, event=None):
        message = self.user_input.get()
        if message.strip():
            self.display_message("You", message)
            self.user_input.delete(0, tk.END)
            threading.Thread(target=self.get_response, args=(message,)).start()

    def display_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.tag_configure(sender.lower(), font=self.bold_font)
        self.chat_display.insert(tk.END, f"{sender}: ", sender.lower())
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def get_response(self, message):
        self.display_message("Bot", "Typing...")
        time.sleep(2)  # Simulate typing delay
        response = self.chatbot.get_response(message)
        self.update_last_message("Bot", response)

    def update_last_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.delete("end-2l", "end-1l")
        self.chat_display.tag_configure(sender.lower(), font=self.bold_font)
        self.chat_display.insert(tk.END, f"{sender}: ", sender.lower())
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
