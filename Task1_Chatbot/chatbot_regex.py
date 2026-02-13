import re
import random
import datetime

print("RahulBot (regex Version)")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You : ").lower()

    #Greeting Pattern

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        print("RahulBot :" ,random.choice(["Hello Rahul !","Hey there"]))

    #Name Pattern

    elif re.search(r"your name", user_input):
        print("RahulBot : I am RahulBot ")
    
    #Time pattern

    elif re.search(r"time",user_input):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("RahulBot : Current time is ",current_time)

    # AI pattern

    elif re.search(r"\b(ai|artificial intelligenc)\b", user_input):
        print("RahulBot : AI means Artificial Intelligence")

    elif re.search(r"\b(bye|exit)\b",user_input):
        print("RahulBot : GoodBye rahul !")
        break

    else:
        print("RahulBot : Soory , I didn't understand.")