# AIChatTerminal
ai chat terminal for chatting but in terminal only :)

## Requirements to run an LLM ( for the app ):
If iMac, MacBook, Mac Studio, Mac Mini,... devices:
- Needs Apple Silicon ( M1 and above or M-series family, for installing the app )
- RAM: 8GB ram and above ( 16GB ram is recommended )
If Windows:
- Needs Windows 10 or Windows 11
- At least 16GB RAM ( 32GB ram is recommended for larger models )

## Instructions: 
1. Download at https://lmstudio.ai
2. After that, follow the instructions through the install process
3. Open the app, but not yet to run.
4. Go to this thing
   <img width="132" alt="Screenshot 2024-11-03 at 21 16 01" src="https://github.com/user-attachments/assets/de241ad5-0767-4486-accd-ea7df88bf012">
5. Choose any models, after that. Download one
6. After downloading, go to the Developer ( make sure the developer mode is turned on, it's at the bottom )
   <img width="148" alt="Screenshot 2024-11-03 at 21 16 49" src="https://github.com/user-attachments/assets/69c586d4-eef6-4df0-892e-a5cbea7b5cdf">
7. Press Start
   <img width="244" alt="Screenshot 2024-11-03 at 21 17 42" src="https://github.com/user-attachments/assets/230a750d-92b1-4dac-9360-effd7740d402">
   - NOTICE: Do NOT change the Server Port ( May send the error later )
   - don't turn on "Serve on Local network" ( May send the error later )

7.5:
- Before that, go to the folders MainGame -> CharAndYou, you could see there's CharInstructions.txt, press on that to edit your system instructions and save changes.
8. After that, type this in terminal or command prompt and make sure click "New terminal at Folder" ( if on Windows, drop the folders to the Command Prompt ) and type:
```
python3 main.py
```

## How it works:
- It works when you send a message, the bot will send the message back again like other AI assistants. But this time, it runs locally straight on your computer or laptop!
- It automactially saves memory using **json** files to remember accross chats and conversations that we had.

## Notice:
- It will be slowly longer because it saves memory and the bot has to process it. It means that it was processing on your computer or the laptop. The memories still may useful, not forgetting longer. But it may slower over time because texts are too much and processing is long.
