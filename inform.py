import telebot
import requests
import time

# 替换自己的 token
bot = telebot.TeleBot("TOKEN", parse_mode="MARKDOWN") # You can set parse_mode by default. HTML or MARKDOWN

def inform():
    web = requests.get("https://hvdb.me/")
    str = web.text
    a = str.find("register")

    if a != -1:
        # 替换自己的 chat_id
        bot.send_message("chat_id", "[hvdb](http://hvdb.me/) register start")
        
t = 0

while True:
    inform()
    # 每小时执行一次
    time.sleep(3600)
    # 计时是否执行了 24 小时
    t += 1
    # 每天提醒一次程序在执行
    if t == 24:
        t -= 24
        local_time = time.ctime(time.time())
        inform_str = "{} 已执行".format(local_time)
        # 替换自己的 chat_id
        bot.send_message("chat_id", inform_str)
