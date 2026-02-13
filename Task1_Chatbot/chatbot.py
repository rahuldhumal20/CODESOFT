import random
import datetime

print("RahulBot : Hello ! I am your Ai Assitant.")
print("Type 'bye' to exit. \n")

grettings = ["Hello Rahul!", "Hi there!" , "Hey Rahul"]
how_are_you = [
    "I am Functionning perfectly !",
    "All systems are operational !",
    "Ready to help you build AI !"
]

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("RahulBot:",random.choice(grettings))

    elif "how are you" in user_input:
        print ("RahulBot:",random.choice(how_are_you))

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("RahulBot : Current Time is : ", current_time )

    elif "your name" in user_input:
        print("RahulBot: I am RahulBot, created for CODESOFT internship.")

    elif "ai" in user_input:
        print("RahulBot: AI stands for Artificial Intelligence.")

    elif "bye" in user_input:
        print("RahulBot:GoodBye Rahul ! keep Codeing")
        break
    else:
        print("RahulBot: Sorry , I didn't understand that.")