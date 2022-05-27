import keyboard, requests
import time, random, os
import webbrowser

os.system("title t0x1c")

class Chat: 
    def write(text): 
        keyboard.press_and_release("t");time.sleep(0.1)
        keyboard.write(str(text))
        keyboard.press_and_release("enter")

class Api: 
    def __init__(self, token): 
        self.token = token
    def parseUser(self, username):
        linkApi = f"http://api.vimeworld.ru/user/name/{username}/session?token={self.token}" 
        req = requests.get(linkApi)
        return req.json()
    def getServer(self, username): 
        user = Api("DJSrOjGuEyM0F6keuh5fwzRTfH30fsx").parseUser(username)
        online = user["online"]
        if online["value"] == False: 
            return online["value"]
        return online["game"]

class Program: 
    def getToxic(): 
        words = [ # Здесь слова, которые будут выводиться. На релизе слов больше
            'ez',
            'ez4',
            0, # Числа можно указывать как int(), багаться не будет
            'уя',
            'соси',
            'clown',
            'клоун',
            'изи',
            'нуб',
            'скулина',
            'лалка',
            'дрыщ',
            'изверг',
            'гей',
            'лузер',
            'пипидастр',
            'дно'
        ]
        return words[random.randint(0, len(words) - 1)]
    def main(): 
        global ask
        ask = str(input("Введите ваш ник: "))
        vApi = Api("DJSrOjGuEyM0F6keuh5fwzRTfH30fsx")
        if vApi.getServer(ask): 
            print("t0x1c > Вы ввели ник: " + ask)
            print("t0x1c > Сейчас Вы на сервере: " + vApi.getServer(ask) )
            print("t0x1c > Ждём комбинацию клавиш: Alt + G")
            Program.start()
        else: 
            print("t0x1c > Вы офлайн!")
    def start(): 
        while True:
            keyboard.wait("Alt + G")
            word = Program.getToxic()
            print("t0x1c > " + word)
            server = Api("DJSrOjGuEyM0F6keuh5fwzRTfH30fsx").getServer(ask)
            Chat.write(Program.toChat(word, server))
    def toChat(word, server): 
        Yes = [# Сервера, на которых нужен "!" перед сообщением
            "EGGWARS",
            "BW",
            "PRISON",
            "ANN",
            "MW",
            "CP",
            "BRIDGE"
        ] 
        if server in Yes: 
            return "! " + word
        else: 
            return word

if __name__ == "__main__":
    webbrowser.open('http://vimetop.ru/player/Yumix', new=2)
    Program.main()