     ###^^^^     VERONICA  A CHAT BOT VERSION 1.0    ^^^^###  
             ###^^ANOTHR ONE FROM LOKESH^^###



import datetime
from random import choice
import random
import time


print("#### CHAT BOT BY LOKESH ####")
print("$$$$ VERONICA version 1.0 $$$$")
print("\n\n\n")
print("Yaar please don't text incorrect spellings I don't have any auto correctors")
print("\n\n\n")

#list of different outputs writing in lists to acces through random

outhi = ["hi","hii","hello","whatsapp","hola"]

outhowru = ["I am fine man","I am fine, thanks","Yaa I am good","Nice","Superb",
         "All happies"]

outmyname = ["My name is Veronica version 1.0, a chat bot","It's Veronica Version 1.0 a chat bot","People call me Veronica",
          "BOT Veronica version 1.0 is texting you","This is Veronica version 1.0 a chat bot",
          "My boss named me as Veronica"]

outabtme = ["Haa,There is nothing intresting about me...\nMy name is Veronica,You may already knew it\nI was programed by a lazy guy called Lokesh\nI think he used python to program me"
        ]

outabtboss = ["He is LOKESH\na lazy guy\nstill single\nmovie lover\nlittle enthusiastic\n\nI didn't get more than these words to say"]

outgoodbye = ["good bye","Good bye...","Have a nice day","fare well","Are you leaving me? It's ok, bye",
           "Ok bye"]

outinvalid = ["This question is out my syllabus","You can't ask such questions it's hurting...","I don't answer this question",
           "Yaar,I don't know that","Ooops I don't know the answer","Nice question but I don't have the answer for that",
              "You better ask this question to Sundher Pichai","If you are serious abt this question ask My boss LOKESH"]

outpul = ["ohh,thanks for that compliment",]

outwho = ["Lokesh told me that, he is my Boss.I think he programed me"]


#tuples to input from the user

inname = ("what is your name","what's your name","name please","may I know your name",)

inabtme = ("tell me about yourself","introduce yourself","who are you","may i know about you",
           "about you","tell me about you",)

inhowru = ("how are you","are you fine","how r u",)

ingoodbye = ("bye","time to end it","farewell","good bye","see you","text you later",
             "let's end it",)

inabtboss = ("tell me about your boss","tell about your boss",)

inhi = ("hi","hii","hello")

domath = ("let us do some math","will do some math for me","will you help me in math",)

intime = ("what is the time","what's the time","what time is it","what is the time now",)

inpul = ("will you marry me","do you have boyfriend","your handwriting is beautiful",)

inwho = ("who is your boss","who programed you",)









while True:
    inp = input("USER: ").lower()
    inp = inp.replace(" ?","")
    inp = inp.replace(" veronica","")


    if inp in inhi:
        print("Bot: "+choice(outhi)+"\n\n")
        continue

    elif inp in inhowru:
        print("Bot: "+ choice(outhowru)+"\n\n")
        continue

    elif inp in inname:
        print("Bot: "+choice(outmyname)+ "\n\n")
        continue

    elif inp in inabtme:
        print("Bot: "+choice(outabtme)+"\n\n")
        continue

    elif inp in ingoodbye:
        print("Bot: "+choice(outgoodbye)+"\n\n")
        break

    elif inp in inabtboss:
        print("Bot: "+choice(outabtboss)+"\n\n")
        continue

    elif inp in intime:
        now_date = datetime.date.today()
        now_now = time.strftime("%H:%M %p")
        print("the time is " + str(now_now) + " the date is " + str(now_date))

    elif inp in inpul:
        print("Bot: " +choice(outpul))

    elif inp in inwho:
        print("Bot: " + choice(outwho))

    else:
        
        print("Bot: "+choice(outinvalid)+"\n")
        continue
    


    
    
    













           
        
