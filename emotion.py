import os
from tkinter import *
import win32com.client as win32
import random
from tkinter import messagebox
from string import *
from collections import *
import matplotlib.pyplot as plt


def emotion():
    emot = open(names + "_emotion.txt", "w")
    emot.write(em.get(1.0, END))
    emot.close()

    text = open(names + "_emotion.txt", encoding="utf-8").read()
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', punctuation))
    tokenized_words = cleaned_text.split()

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                  "having", "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any",
                  "both",
                  "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same",
                  "so",
                  "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    emotion_list = []
    with open('nltk_emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)

    if os.stat(names+"_feelings.txt").st_size == 0:
        emote = open(names+"_feelings.txt", "w")
        for e in emotion_list:
            emote.write(e+"\n")
        emote.close()

    else:
        emote = open(names+"_feelings.txt", "a")
        for e in emotion_list:
            emote.write(e+"\n")
        emote.close()

    emote1 = open(names+"_feelings.txt", "r")
    w1 = emote1.read().split("\n")
    w = Counter(w1)
    del w['']

    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig(names+'_emotion.png')
    plt.show()


def success(name, ps):
    user.delete(0, END)
    pswd.delete(0, END)

    global names
    names = name

    list_files = os.listdir()

    if name in list_files:
        file = open(name, "r")
        values = file.read().splitlines()

        if ps in values:

            global into

            into = Tk()
            into.title("Jookate Tab")
            into.geometry("400x350")
            into.configure(bg="pink")

            global em

            Label(into, text="How was your Day..???", bg="pink").pack(padx=20, pady=(20, 15))
            em = Text(into, width=40, height=15)
            em.pack()
            Button(into, text="Ok..!!", bg="magenta", command=emotion).pack(pady=10, ipadx=120)

            into.mainloop()
        else:
            messagebox.showinfo("ALERT", "INCORRECT PASSWORD..!!!")
    else:
        messagebox.showinfo("ALERT", "Username not found")


def login():
    window2 = Tk()
    window2.title("Login")
    window2.geometry("400x350")
    window2.configure(bg="pink")

    global user
    global pswd

    Label(window2, text="    User Login", font=("century", 20), bg="pink").grid(row=0, column=0,
                                                                                columnspan=2)

    Label(window2, text="Username  : ", bg="pink", font=("century", 15)).grid(row=1, column=0, padx=(20, 0),
                                                                              pady=(40, 10))
    user = Entry(window2)
    user.grid(row=1, column=1, pady=(40, 10), ipadx=50)

    Label(window2, text="Password   : ", bg="pink", font=("century", 15)).grid(row=2, column=0, padx=(20, 0))
    pswd = Entry(window2)
    pswd.grid(row=2, column=1, ipadx=50)

    B = Button(window2, text="Login", bg="magenta", command=lambda: success(user.get(), pswd.get()))
    B.grid(row=3, column=0, columnspan=2, pady=40, padx=(20, 0), ipadx=150)

    window2.mainloop()


def check():
    global otp

    otp = Tk()
    otp.title("Otp Verification")
    otp.geometry("300x200")
    otp.configure(bg="pink")

    global ot

    Label(otp, text="Enter the otp sent to you...!!!!", bg="pink", font=("century", 14)).pack(pady=20)
    ot = Entry(otp)
    ot.pack(pady=(0, 40), ipadx=80)
    Button(otp, text="Verify", bg="magenta", command=verify).pack(ipadx=50)

    otp.mainloop()


def verify():
    one = ot.get()
    if one == ott:
        completed()
        messagebox.showinfo("Verification Done", "Registration success")
        otp.quit()
        window1.quit()
    else:
        messagebox.showinfo("Wrong Otp", "Check for the otp...!!!")


def otps():
    global ott

    Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

    outlook = win32.Dispatch('outlook.application')
    mails = outlook.CreateItem(0)
    mails.To = mail.get()
    ott = random.choice(Letters) + str(random.randint(10000, 99999))
    mails.HTMLBody = '<h2>' + ott + '</h2>'

    mails.Send()

    check()


def completed():
    name = user.get()
    ps = pswd.get()

    user.delete(0, END)
    pswd.delete(0, END)
    mail.delete(0, END)

    fil = open(name+"_feelings.txt", "w")
    fil.close()

    file = open(name, "w")
    file.write(name + "\n" + ps)
    file.close()


def signup():
    global window1

    window1 = Tk()
    window1.title("Registration")
    window1.geometry("400x350")
    window1.configure(bg="pink")

    global user
    global pswd
    global mail

    Label(window1, text="           User Registration", font=("century", 20), bg="pink").grid(row=0, column=0,
                                                                                              columnspan=2)

    l = Label(window1, text="Username  : ", bg="pink", font=("century", 15))
    l.grid(row=1, column=0, padx=(20, 0), pady=(40, 10))
    user = Entry(window1)
    user.grid(row=1, column=1, pady=(40, 10), ipadx=50)

    l2 = Label(window1, text="Email         : ", bg="pink", font=("century", 15))
    l2.grid(row=2, column=0, padx=(20, 0), pady=(0, 10))
    mail = Entry(window1)
    mail.grid(row=2, column=1, pady=(0, 10), ipadx=50)

    l1 = Label(window1, text="Password   : ", bg="pink", font=("century", 15))
    l1.grid(row=3, column=0, padx=(20, 0))
    pswd = Entry(window1)
    pswd.grid(row=3, column=1, ipadx=50)

    B1 = Button(window1, text="Register", bg="magenta", command=otps)
    B1.grid(row=4, column=0, columnspan=2, pady=40, padx=(20, 0), ipadx=150)

    window1.mainloop()


window = Tk()
window.title("Home Page")
window.geometry("400x350")
window.configure(bg="pink")

Label(window, text="JooKate", font=("century", 36), bg="pink").pack()

Button(window, text="Login", command=login).pack(pady=(80, 10), ipadx=200)
Button(window, text="Signup", command=signup).pack(ipadx=200)

window.mainloop()
