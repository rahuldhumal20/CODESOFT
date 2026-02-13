import tkinter as tk
import re
import datetime

def send_message():
    user_input = entry.get()
    chat_window.insert(tk.END , "You: "+ user_input +"\n")

    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        response = "Hello Rahul !"
    elif "time" in user_input:
        response = datetime.datetime.now().strftime("%H:%M:%S")
    elif "your name" in user_input:
        response = "I am RahulBot"
    elif "bye" in user_input:
        response = "GoodBye !"
        root.quit()
    
    else:
        response = " Sorry i dont understand."

    chat_window.insert(tk.END, "Bot : "+ response +"\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("RahulBot Chatbot")

chat_window= tk.Text(root , height=20, width=50)
chat_window.pack()

entry = tk.Entry(root , width=40)
entry.pack()

send_button = tk.Button(root, text="send", command=send_message)
send_button.pack()

root.mainloop()
