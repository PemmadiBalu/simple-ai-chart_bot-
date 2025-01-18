import tkinter as tk
from tkinter import messagebox
import time

# Dictionary of responses for the chatbot
responses = {
    "hi": ["Hey!, Hi! How can I help you?"],
    "hello": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great! What about you?", "All good! How can I assist you?"],
    "what is your name": ["I am called SparkBot.", "You can call me SparkBot.", "I go by the name SparkBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "what language are you written in": ["I am written in Python.", "Python is my language of choice."],
    "who are you": ["I am SparkBot, your friendly chatbot."]
}

# Function for basic preprocessing of user inputs
def preprocess_input(user_input):
    return user_input.lower()

# Function to get the chatbot response
def get_response(user_input):
    user_input = preprocess_input(user_input)
    return responses.get(user_input, ["I'm sorry, I don't understand. Can you please ask something else?"])[0]

# Function to simulate slow typing effect
def slow_type(text_widget, text, color="black"):
    text_widget.config(state=tk.NORMAL)  # Enable text widget for writing
    for char in text:
        text_widget.insert(tk.END, char, color)
        text_widget.see(tk.END)  # Scroll the text widget to the end
        text_widget.update_idletasks()  # Update the text widget immediately
        time.sleep(0.05)  # Adjust the delay time for slower or faster typing effect
    text_widget.config(state=tk.DISABLED)  # Disable text widget for writing

# Function to handle user input and chatbot response
def handle_user_input():
    user_input = input_entry.get().strip()
    input_entry.delete(0, tk.END)  # Clear the input field
    if user_input == "":
        return
    slow_type(chat_text, f"\nYou: {user_input}\n", "blue")
    response = get_response(user_input)
    slow_type(chat_text, f"Chatbot: {response}\n", "green")
    conversation_history.append((f"You: {user_input}", f"Chatbot: {response}"))

# Function to save the conversation to a file
def save_conversation():
    if not conversation_history:
        messagebox.showinfo("Save Conversation", "No conversation to save.")
        return

    file_name = "chatbot_conversation.txt"
    with open(file_name, "w") as file:
        for user_msg, bot_msg in conversation_history:
            file.write(user_msg + "\n")
            file.write(bot_msg + "\n")
    messagebox.showinfo("Save Conversation", f"Conversation saved as {file_name}.")

# Function to create and configure the GUI
def create_gui():
    global chat_window, input_entry, chat_text, conversation_history

    conversation_history = []

    chat_window = tk.Tk()
    chat_window.title("AI Chatbot Chat")
    chat_window.geometry("400x500")
    chat_window.configure(bg="#f0f8ff")

    chat_text = tk.Text(chat_window, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", fg="black", font=("Arial", 12))
    chat_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    scrollbar = tk.Scrollbar(chat_window, command=chat_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_text.config(yscrollcommand=scrollbar.set)

    input_frame = tk.Frame(chat_window, bg="#f0f8ff")
    input_frame.pack(fill=tk.X, padx=10, pady=5)

    input_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#e0ffff")
    input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
    input_entry.bind("<Return>", lambda event: handle_user_input())

    send_button = tk.Button(input_frame, text="Send", command=handle_user_input, bg="#add8e6", font=("Arial", 10))
    send_button.pack(side=tk.RIGHT, padx=5)

    menu_bar = tk.Menu(chat_window)
    chat_window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Save Conversation", command=save_conversation)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=chat_window.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    chat_window.mainloop()

# Run the chatbot GUI
create_gui()
