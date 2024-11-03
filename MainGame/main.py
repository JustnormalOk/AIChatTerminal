# COPYRIGHT: @justnormal_o

from time import sleep as wait
import os
import requests
import json
import random

with open("UsuagePackages/instructions.txt", "r") as file:
    print(file.read())

input("Press Enter to continue...")

server_url = "http://localhost:1234/v1/chat/completions"
print("""

""")
wait(1)
for i in range(100):
    print(" ")

wait(1)
print("""
[ - CHAT WITH AI - ]
      
1. Start Chatting [A]
2. Quit [B]
3. Versions [C]
""")

intro = input("Your option: ")

def choosing():
    with open("MainGame/CharAndYou/CharInstructions.txt", "r") as file:
        CharInstructionsWritten = file.read()
        
    if intro == "A":
        wait(1)
        for i in range(100):
            print(" ")
            
        CharName = input("The bot's name: ")
        print(f"""Your character's instructions:
              {CharInstructionsWritten}
              """)
        print("Succeed made a bot.")
        
        wait(1)
        for i in range(100):
            print(" ")

        return CharInstructionsWritten, CharName

    elif intro == "B":
        print(".")
        return None, None

    elif intro == "C":
        with open("MainGame/Packages/Versions.txt") as file:
            print("Versions:")
            print(file.read())
        print("")
        return None, None

CharInstructionsWritten, CharName = choosing()

def Conversation():
    rand = random.randint(1, 10000)
    file_name = f"MainGame/Memories/memory_box_{rand}.json"

    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump([], file)

    def ask_local_model(prompt):
        with open(file_name, "r") as file:
            data9 = json.load(file)

        data = {
            "model": "local-model",
            "messages": [
                {"role": "system", "content": CharInstructionsWritten},
                {"role": "user", "content": prompt, "MemoryBox": data9}
            ]
        }

        response = requests.post(server_url, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            print("Error:", response.status_code, response.text)
            return None

    while True:
        user_input = input("You: ")
        response = ask_local_model(user_input)
        print(f"{CharName}:", response)

        if user_input.lower() == "!exit":
            print("System: Ending the chat.")
            break

        with open(file_name, "r") as file:
            chat_history = json.load(file)

        chat_history.append({"user": user_input, CharName: response})

        with open(file_name, "w") as file:
            json.dump(chat_history, file, indent=4)

Conversation()