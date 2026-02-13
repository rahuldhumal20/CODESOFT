import re
import datetime

print(" RahulBot (with Chat lag)")
print("Type 'bye' to exit.\n")

log_file = open("chat_history.txt", "a")

while True:
    user_input = input("You : ").lower()

    log_file.write(f"You : {user_input}\n")

    if re.search(r"\b(hii|hello|hey)\b", user_input):
        response= "Hello Rahul !"

    elif "your name" in user_input:
        response ="Iam RahulBot"

    elif "how are you" in user_input:
        response ="I am Functionning perfectly !"

    elif "time" in user_input:
        response = datetime.datetime.now().strftime("%H:%M:%S")

    elif "bye" in user_input:
        response = "GoodBye Rahul !"
        print("RahulBot: ", response)
        log_file.write(f"Bot : {response}\n")
        break

    else:
        response = "Sorry , I don't understand."

    print("RahulBot: ", response)
    log_file.write(f"Bot : {response}\n")

log_file.close()
