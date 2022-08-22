from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import os
import speech_recognition
import threading


bot=ChatBot('Mybot')
trainer=ListTrainer(bot)
for files in os.listdir('data/english/'):
    data=open('data/english/'+files, 'r', encoding='utf-8').readlines()

trainer.train(data)

def botReply():
    question=questionfield.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END, 'You:'+ question+'\n')
    textarea.insert(END, 'Bot:'+ str(answer)+'\n')
    #pyttsx3.speak(answer)
    questionfield.delete(0,END)


'''def audiototext():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)
                questionfield.delete(0,END)
                questionfield.insert(0,query)
                botReply()
        except Exception as e:
            print(e)
'''


root = Tk()


root.geometry('500x570+100+30')
root.title('MyChatBot')
root.config(bg='black')


logopic = PhotoImage(file='pic.png')
logopiclabel=Label(root,image=logopic,bg='black')
logopiclabel.pack(pady=5)

centerframe=Frame(root)
centerframe.pack()

scrollbar=Scrollbar(centerframe)
scrollbar.pack(side='right')

textarea=Text(centerframe,font=('times new roman',20, 'bold'),height=10,yscrollcommand=scrollbar.set, wrap='word')
textarea.pack()
scrollbar.config(command=textarea.yview)


questionfield=Entry(root,font=('verdana',20,'bold'))
questionfield.pack(pady=15,fill=X)


askpic=PhotoImage(file='ask.png')
askbutton=Button(root,image=askpic,command=botReply)
askbutton.pack()

def click(event):
    askbutton.invoke()


root.bind('<Return>', click)

'''thread=threading.Thread(target=audiototext)
thread.setDaemon(True)
thread.start()'''



root.mainloop()


